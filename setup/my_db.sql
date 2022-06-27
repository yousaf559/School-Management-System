-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema sms
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sms
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sms` DEFAULT CHARACTER SET utf8mb3 ;
USE `sms` ;

-- -----------------------------------------------------
-- Table `sms`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`admin` (
  `username` VARCHAR(10) NOT NULL,
  `password` VARCHAR(10) NULL DEFAULT NULL,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `address` VARCHAR(150) NULL DEFAULT NULL,
  `phone` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`subjects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`subjects` (
  `subject_id` INT NOT NULL,
  `subject_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`subject_id`),
  UNIQUE INDEX `subject_id_UNIQUE` (`subject_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`teachers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`teachers` (
  `teacher_id` INT NOT NULL AUTO_INCREMENT,
  `teacher_name` VARCHAR(50) NOT NULL,
  `teacher_address` MEDIUMTEXT NOT NULL,
  `teacher_phone` VARCHAR(15) NULL DEFAULT NULL,
  `tch_email` VARCHAR(100) NULL DEFAULT NULL,
  `tch_password` VARCHAR(20) NULL DEFAULT NULL,
  `subject_taught` INT NULL DEFAULT NULL,
  `salary` INT NULL DEFAULT NULL,
  PRIMARY KEY (`teacher_id`),
  UNIQUE INDEX `teacher_id_UNIQUE` (`teacher_id` ASC) VISIBLE,
  UNIQUE INDEX `tch_email` (`tch_email` ASC) VISIBLE,
  INDEX `subject_taught` (`subject_taught` ASC) VISIBLE,
  CONSTRAINT `teachers_ibfk_1`
    FOREIGN KEY (`subject_taught`)
    REFERENCES `sms`.`subjects` (`subject_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`assignments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`assignments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  `resource` VARCHAR(100) NULL DEFAULT NULL,
  `teacher_id` INT NULL DEFAULT NULL,
  `marks_alloted` INT NULL DEFAULT NULL,
  `subject` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `teacher_id` (`teacher_id` ASC) VISIBLE,
  INDEX `subject` (`subject` ASC) VISIBLE,
  CONSTRAINT `assignments_ibfk_1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `sms`.`teachers` (`teacher_id`),
  CONSTRAINT `assignments_ibfk_2`
    FOREIGN KEY (`subject`)
    REFERENCES `sms`.`subjects` (`subject_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`students` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `student_name` VARCHAR(50) NOT NULL COMMENT 'Student\'s full name',
  `student_address` MEDIUMTEXT NOT NULL,
  `student_age` INT NOT NULL,
  `student_phone` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE INDEX `student_id_UNIQUE` (`student_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`std_attendance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`std_attendance` (
  `student_id` INT NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `status` VARCHAR(15) NULL DEFAULT NULL,
  INDEX `student_id` (`student_id` ASC) VISIBLE,
  CONSTRAINT `std_attendance_ibfk_1`
    FOREIGN KEY (`student_id`)
    REFERENCES `sms`.`students` (`student_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`student_br_teacher`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`student_br_teacher` (
  `student_id` INT NULL DEFAULT NULL,
  `teacher_id` INT NULL DEFAULT NULL,
  `class_name` VARCHAR(20) NULL DEFAULT NULL,
  `class_id` INT NOT NULL AUTO_INCREMENT,
  `class_year` YEAR NOT NULL DEFAULT year(curdate()),
  PRIMARY KEY (`class_id`),
  UNIQUE INDEX `unq_t_parent_name` (`student_id` ASC, `teacher_id` ASC) VISIBLE,
  UNIQUE INDEX `unq_t_student_year` (`student_id` ASC, `class_year` ASC) VISIBLE,
  INDEX `teacher_id` (`teacher_id` ASC) VISIBLE,
  CONSTRAINT `student_br_teacher_ibfk_1`
    FOREIGN KEY (`student_id`)
    REFERENCES `sms`.`students` (`student_id`),
  CONSTRAINT `student_br_teacher_ibfk_2`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `sms`.`teachers` (`teacher_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`student_subjects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`student_subjects` (
  `student_id` INT NOT NULL,
  `subject_id` INT NOT NULL,
  PRIMARY KEY (`student_id`, `subject_id`),
  INDEX `fk_student_subjects_students1_idx` (`student_id` ASC) INVISIBLE,
  INDEX `fk_student_subjects_subjects1_idx` (`subject_id` ASC) VISIBLE,
  CONSTRAINT `fk_student_subjects_students1`
    FOREIGN KEY (`student_id`)
    REFERENCES `sms`.`students` (`student_id`),
  CONSTRAINT `fk_student_subjects_subjects1`
    FOREIGN KEY (`subject_id`)
    REFERENCES `sms`.`subjects` (`subject_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`students_asses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`students_asses` (
  `student_id` INT NULL DEFAULT NULL,
  `ass_id` INT NULL DEFAULT NULL,
  `grade` INT NULL DEFAULT NULL,
  INDEX `student_id` (`student_id` ASC) VISIBLE,
  INDEX `ass_id` (`ass_id` ASC) VISIBLE,
  CONSTRAINT `students_asses_ibfk_1`
    FOREIGN KEY (`student_id`)
    REFERENCES `sms`.`students` (`student_id`),
  CONSTRAINT `students_asses_ibfk_2`
    FOREIGN KEY (`ass_id`)
    REFERENCES `sms`.`assignments` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`tch_attendance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`tch_attendance` (
  `teacher_id` INT NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `status` VARCHAR(15) NULL DEFAULT NULL,
  INDEX `teacher_id` (`teacher_id` ASC) VISIBLE,
  CONSTRAINT `tch_attendance_ibfk_1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `sms`.`teachers` (`teacher_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sms`.`transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sms`.`transactions` (
  `transaction_id` INT NOT NULL AUTO_INCREMENT,
  `transaction_date` DATE NOT NULL,
  `amount` INT NULL DEFAULT NULL,
  `type` VARCHAR(10) NOT NULL,
  `description` VARCHAR(45) NOT NULL,
  `teacher_id` INT NULL DEFAULT NULL,
  `student_id` INT NULL DEFAULT NULL,
  `status` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  UNIQUE INDEX `transaction_id_UNIQUE` (`transaction_id` ASC) VISIBLE,
  INDEX `teacher_id_idx` (`teacher_id` ASC) VISIBLE,
  INDEX `student_id_idx` (`student_id` ASC) VISIBLE,
  CONSTRAINT `student_id`
    FOREIGN KEY (`student_id`)
    REFERENCES `sms`.`students` (`student_id`),
  CONSTRAINT `teacher_id`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `sms`.`teachers` (`teacher_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 35
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
