/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 31/01/2023 09:41:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for animal
-- ----------------------------
DROP TABLE IF EXISTS `animal`;
CREATE TABLE `animal`  (
  `type` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `animalname` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of animal
-- ----------------------------
INSERT INTO `animal` VALUES ('有毛发', '金钱豹');
INSERT INTO `animal` VALUES ('产奶', '虎');
INSERT INTO `animal` VALUES ('有羽毛', '长颈鹿');
INSERT INTO `animal` VALUES ('不会飞', '斑马');
INSERT INTO `animal` VALUES ('会下蛋', '鸵鸟');
INSERT INTO `animal` VALUES ('吃肉', '企鹅');
INSERT INTO `animal` VALUES ('有犬齿', '信天翁');
INSERT INTO `animal` VALUES ('有爪', NULL);
INSERT INTO `animal` VALUES ('眼盯前方', NULL);
INSERT INTO `animal` VALUES ('有蹄', NULL);
INSERT INTO `animal` VALUES ('反刍', NULL);
INSERT INTO `animal` VALUES ('黄褐色', NULL);
INSERT INTO `animal` VALUES ('有斑点', NULL);
INSERT INTO `animal` VALUES ('有黑色条纹', NULL);
INSERT INTO `animal` VALUES ('长脖', NULL);
INSERT INTO `animal` VALUES ('长腿', NULL);
INSERT INTO `animal` VALUES ('不会飞', NULL);
INSERT INTO `animal` VALUES ('会游泳', NULL);
INSERT INTO `animal` VALUES ('黑白二色', NULL);
INSERT INTO `animal` VALUES ('善飞', NULL);
INSERT INTO `animal` VALUES ('哺乳类', NULL);
INSERT INTO `animal` VALUES ('鸟类', NULL);
INSERT INTO `animal` VALUES ('食肉类', NULL);
INSERT INTO `animal` VALUES ('蹄类', NULL);

-- ----------------------------
-- Table structure for rule
-- ----------------------------
DROP TABLE IF EXISTS `rule`;
CREATE TABLE `rule`  (
  `rule` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `finally` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rule
-- ----------------------------
INSERT INTO `rule` VALUES ('产奶', '哺乳类');
INSERT INTO `rule` VALUES ('有羽毛', '鸟类');
INSERT INTO `rule` VALUES ('不会飞 会下蛋', '鸟类');
INSERT INTO `rule` VALUES ('食肉', '哺乳类');
INSERT INTO `rule` VALUES ('有犬齿 有爪 眼盯前方', '食肉类');
INSERT INTO `rule` VALUES ('有蹄 哺乳类', '蹄类');
INSERT INTO `rule` VALUES ('反刍', '哺乳类');
INSERT INTO `rule` VALUES ('不会飞 会游泳 黑白二色 鸟类', '企鹅');
INSERT INTO `rule` VALUES ('不会飞 长脖 长腿 鸟类', '鸵鸟');
INSERT INTO `rule` VALUES ('善飞 鸟类', '信天翁');
INSERT INTO `rule` VALUES ('有斑点 有黑色条纹 长脖 蹄类', '长颈鹿');
INSERT INTO `rule` VALUES ('有黑色条纹 蹄类', '斑马');
INSERT INTO `rule` VALUES ('黄褐色 有黑色条纹 哺乳类 食肉类', '虎');
INSERT INTO `rule` VALUES ('黄褐色 有斑点 哺乳类 食肉类', '金钱豹');
INSERT INTO `rule` VALUES ('有毛发', '哺乳类');

SET FOREIGN_KEY_CHECKS = 1;
