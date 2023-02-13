/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : SQLite
 Source Server Version : 3017000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3017000
 File Encoding         : 65001

 Date: 12/02/2023 18:35:12
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE IF EXISTS "USER";
CREATE TABLE "USER" (
  "id" INT,
  "name" TEXT,
  "age" INT,
  "height" DOUBLE(50),
  "weight" DOUBLE(50),
  "createTime" DATETIME,
  "updateTime" DATETIME,
  "deleteTime" DATETIME,
  "flag" BOOLEAN,
  "trainer" TEXT,
  PRIMARY KEY ("id")
);

PRAGMA foreign_keys = true;
