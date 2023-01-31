import tkinter
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QAction
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLabel,QTextBrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import pymysql
Animals = [] 
Feature = [] 
Rules = [] 
data = []
testture = []  
testall = []  
num = []  
mid = []
c=''
conn=pymysql.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1
        ,user = 'root' # 用户名
        ,passwd='123456' # 密码
        ,port= 3306 # 端口，默认为3306
        ,db='test' # 数据库名称
        ,charset='utf8' # 字符编码
        )
class GUI(): 
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(1500,470)
        self.window.move(300, 310)
        self.window.setWindowTitle('产生式系统')
        self.textEdit = QPlainTextEdit(self.window)

        self.lb1 = QLabel('输入框',self.window)
        self.lb1.move(230,0)
        self.lb2 = QLabel('事实库',self.window)
        self.lb2.move(680,0)
        self.lb3 = QLabel('规则库',self.window)
        self.lb3.move(1180,0)
        self.lb4 = QLabel('软件202-权泽睿-20002370',self.window)
        self.lb4.move(1180,400)
        self.lb4.resize(300,100)
        self.lb5 = QLabel('加入规则:\n 可以一次输入多个规则，每条规则的\n第一行输入条件，每个条件之间用空\n格隔开，然后换行输入结论。如需要\n输入第二段规则则需要换行然后输入\n',self.window)
        self.lb5.move(60,230)
        self.lb5.resize(300,200)
        self.lb6 = QLabel('删除规则:\n 只需输入规则前的序号就可删除 ',self.window)
        self.lb6.move(60,300)
        self.lb6.resize(300,200)
        self.textEdit.setPlaceholderText("请输入已有特征信息的序号")
        self.textEdit.move(50, 25)
        self.textEdit.resize(400,200)
        self.text = QTextBrowser(self.window)
        self.text.move(500, 25)
        self.text.resize(400,200)
        self.text1 = QTextBrowser(self.window)
        self.text1.move(1000, 25)
        self.text1.resize(400,200)
        self.button1 = QPushButton('输入完成', self.window)
        self.button1.move(380, 320)
        self.button1.clicked.connect(self.handle)
        self.button2 = QPushButton('数据库', self.window)
        self.button2.move(500, 320)
        self.button2.clicked.connect(self.fun_show)
        self.button3 = QPushButton('加入规则', self.window)
        self.button3.move(620, 320)
        self.button3.clicked.connect(self.add)
        self.button3.clicked.connect(self.fun_show)
        self.button7 = QPushButton('加入规则', self.window)
        self.button7.move(620, 320)
        self.button7.clicked.connect(self.add1)
        self.button7.clicked.connect(self.read1)
        self.button7.hide()
        self.button4 = QPushButton('删除规则', self.window)
        self.button4.move(740, 320)
        self.button4.clicked.connect(self.delete)
        self.button4.clicked.connect(self.fun_show)
        self.button8 = QPushButton('删除规则', self.window)
        self.button8.move(740, 320)
        self.button8.clicked.connect(self.delete1)
        self.button8.clicked.connect(self.read1)
        self.button8.hide()
        self.button5 = QPushButton('读入文件', self.window)
        self.button5.move(860, 320)
        self.button5.clicked.connect(self.read)
        self.button5.clicked.connect(self.read1)
        self.button6 = QPushButton('将规则保存', self.window)
        self.button6.move(980, 320)
        self.button6.clicked.connect(self.save)
    def handle(self):
        global num
        before = [] 
        info = self.textEdit.toPlainText()
        num = list(map(int, info.split()))
        for i in num:  
            data.append(Feature[i - 1])
            before.append(Feature[i - 1])
        infer = inference()
        QMessageBox.about(
            self.window, '结果', f'''前提条件为：\n{' '.join(before)}\n{''.join(mid)}\n结果是\n{infer}''')
    def add(self):
        SQL="INSERT into rule values (%s,%s) "
        before = []
        result=[]
        result1=[]
        cur = conn.cursor()
        info = self.textEdit.toPlainText()
        before=info.splitlines()
        for i in range(len(before))[::2]:
            if i + 1 < len(before):
                result=((before[i], before[i + 1]))
            else:
                QMessageBox.about(self.window,'1','规则输入格式不对')
            try:
                cur.execute(SQL,(result[0],result[1]))
                conn.commit()
            except:
                conn.rollback()
        cur.close()
    def delete(self):
        SQL="delete from rule where rule=%s "
        sql = "SELECT * FROM rule"
        info = self.textEdit.toPlainText()
        cur1 = conn.cursor() 
        cur1.execute(sql) 
        rule1 = cur1.fetchall()
        cur1.close()
        cur=conn.cursor()
        result=info.split()
        for i in result:
            j=int(i)
            j=rule1[j-1][0]
            try:
                cur.execute(SQL,j)
                conn.commit()
            except:
                conn.rollback()
        cur.close()
    def delete1(self):
        d=1
        info = self.textEdit.toPlainText()
        result=info.split()
        for i in result:
            j=int(i)
            j=Rules[j-1]
            Rules.remove(j)
        global c
        with open(c,'w',encoding='utf8') as f:
            for i in Rules:
                if d!=1:
                    f.write("\n")
                for j in i:
                    f.write(str(j))
                    f.write(" ")
                d=d+1
        f.close()
    def add1(self):
        info = self.textEdit.toPlainText()
        before=info.splitlines()
        for i in range(len(before))[::2]:
            if i + 1 < len(before):
                result=((before[i], before[i + 1]))
            else:
                QMessageBox.about(self.window,'1','规则输入格式不对')
                break
            with open(c,'a',encoding='utf8') as f:
                f.write('\n')
                f.write(result[0])
                f.write(' ')
                f.write(result[1])
            f.close()
    def read(self):
        temp1 = ""
        count1=1
        temp=""
        count=1
        root = tkinter.Tk()
        root.withdraw() # 隐藏窗口
        global c
        c = filedialog.askopenfilename() # 打开一个新窗口选择文件
    def read1(self):
        temp1 = ""
        count1=1
        temp=""
        count=1
        Feature1=[]
        Animals1=[]
        global c
        global Rules
        Rules=[]
        with open(c, 'r', encoding='utf8') as f3:
            for line in f3:
                line = line.split()
                Rules.append(line)
        f3.close()
        for j in Rules:
            Feature1.extend(j[0:-1])
        for j in Rules:
            Animals1.append(j[-1])
        b={}
        b=b.fromkeys(Feature1)
        global Feature
        global Animals
        Feature=list(b.keys())
        b=b.fromkeys(Animals1)
        Animals=list(b.keys())
        for i in Feature:
            temp1 += str(count1) + "." + i+"\n"
            count1 += 1
        self.text.setPlainText(temp1)
        for i in Rules:
            temp +=str(count)+"."
            for j in i:
                temp +=j+' '
            temp+="\n"
            count += 1
        self.text1.setPlainText(temp)
        self.button3.hide()
        self.button4.hide()
        self.button7.show()
        self.button8.show()
    def save(self):
        a=1
        with open("规则一.txt",'w',encoding='utf8') as f:
            for i in Rules:
                if a!=1:
                    f.write("\n")
                a=a+1
                for j in i:
                    f.write(str(j))
                    f.write(" ")
        f.close()
    def fun_show(self):
        global Rules
        Rules=[]
        Feature1=[]
        Animals1=[]
        SQL = "SELECT * FROM rule"
        cur = conn.cursor()
        cur.execute(SQL)
        count = 1
        count1=1
        temp = ""
        temp1 = ""
        for i in cur.fetchall():
            temp += str(count) + "." + i[0]+' '+i[1] + "\n"
            count += 1
        self.text1.setPlainText(temp)
        cur.close() # 关闭游标
        cur1 = conn.cursor() # 生成游标对象
        cur1.execute(SQL) # 执行SQL语句
        rule1 = cur1.fetchall()
        for i in rule1:
            list2=list(i)
            list3=list2[0].split()
            list3.append(list2[1])
            Rules.append(list3)
        for j in Rules:
            Feature1.extend(j[0:-1])
        for j in Rules:
            Animals1.append(j[-1])
        b={}
        b=b.fromkeys(Feature1)
        global Feature
        global Animals
        Feature=list(b.keys())
        b=b.fromkeys(Animals1)
        Animals=list(b.keys())
        for i in Feature:
            temp1 += str(count1) + "." + i+"\n"
            count1 += 1
        self.text.setPlainText(temp1)
        cur1.close()
        self.button7.hide()
        self.button8.hide()
        self.button3.show()
        self.button4.show()
def inference(): 
    flag = 1  
    flag1=1
    s = "推理过程如下:"  
    while (flag):
        if (data[-1] in Animals): 
            return data[-1]
        else:
            testture = []
            for i in range(len(Rules)):
                if (Rules[i] in testall):
                    pass
                else:
                    sub = Rules[i][:-1]
                    for j in sub:
                        if (j not in data): 
                            break
                        if (j == sub[-1]):
                            if (Rules[i][-1] not in data):
                                data.append(Rules[i][-1])
                            for g in Rules[i]:
                                s += g
                                s += ' '
                            s+='\n'
                            global  mid
                            mid=s
                            testture.append(Rules[i])
                            testall.append(Rules[i])
            if (testture == []):
                flag = 0  
                return False
app = QApplication([])
gui = GUI()
gui.window.show()
app.exec_()

