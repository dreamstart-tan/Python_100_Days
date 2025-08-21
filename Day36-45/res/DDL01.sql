-- 如果存在名为school的数据库就删除它
DROP DATABASE IF EXISTS `school`;

-- 创建名为school的数据库并设置默认的字符集和排序方式
CREATE DATABASE `school` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- 切换到school数据库上下文环境
USE `school`;

-- 创建学院表
CREATE TABLE `tb_college`
(
`col_id`    int unsigned AUTO_INCREMENT      COMMENT '编号',
`col_name`  varchar(50)  NOT NULL            COMMENT '名称',
`col_intro` varchar(500) NOT NULL DEFAULT '' COMMENT '介绍',
PRIMARY KEY (`col_id`)
);

-- 创建学生表
CREATE TABLE `tb_student`
(
`stu_id`    int unsigned NOT NULL           COMMENT '学号',
`stu_name`  varchar(20)  NOT NULL           COMMENT '姓名',
`stu_sex`   boolean      NOT NULL DEFAULT 1 COMMENT '性别',
`stu_birth` date         NOT NULL           COMMENT '出生日期',
`stu_addr`  varchar(255) DEFAULT ''         COMMENT '籍贯',
`col_id`    int unsigned NOT NULL           COMMENT '所属学院',
PRIMARY KEY (`stu_id`),
CONSTRAINT `fk_student_col_id` FOREIGN KEY (`col_id`) REFERENCES `tb_college` (`col_id`)
);

-- 创建教师表
CREATE TABLE `tb_teacher`
(
`tea_id`    int unsigned NOT NULL                COMMENT '工号',
`tea_name`  varchar(20)  NOT NULL                COMMENT '姓名',
`tea_title` varchar(10)  NOT NULL DEFAULT '助教' COMMENT '职称',
`col_id`    int unsigned NOT NULL                COMMENT '所属学院',
PRIMARY KEY (`tea_id`),
CONSTRAINT `fk_teacher_col_id` FOREIGN KEY (`col_id`) REFERENCES `tb_college` (`col_id`)
);

-- 创建课程表
CREATE TABLE `tb_course`
(
`cou_id`     int unsigned NOT NULL COMMENT '编号',
`cou_name`   varchar(50)  NOT NULL COMMENT '名称',
`cou_credit` int          NOT NULL COMMENT '学分',
`tea_id`     int unsigned NOT NULL COMMENT '授课老师',
PRIMARY KEY (`cou_id`),
CONSTRAINT `fk_course_tea_id` FOREIGN KEY (`tea_id`) REFERENCES `tb_teacher` (`tea_id`)
);

-- 创建选课记录表
CREATE TABLE `tb_record`
(
`rec_id`   bigint unsigned AUTO_INCREMENT COMMENT '选课记录号',
`stu_id`   int unsigned    NOT NULL       COMMENT '学号',
`cou_id`   int unsigned    NOT NULL       COMMENT '课程编号',
`sel_date` date            NOT NULL       COMMENT '选课日期',
`score`    decimal(4,1)                   COMMENT '考试成绩',
PRIMARY KEY (`rec_id`),
CONSTRAINT `fk_record_stu_id` FOREIGN KEY (`stu_id`) REFERENCES `tb_student` (`stu_id`),
CONSTRAINT `fk_record_cou_id` FOREIGN KEY (`cou_id`) REFERENCES `tb_course` (`cou_id`),
CONSTRAINT `uk_record_stu_cou` UNIQUE (`stu_id`, `cou_id`)
);
