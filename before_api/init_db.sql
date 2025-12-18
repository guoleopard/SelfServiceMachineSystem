-- 创建医院自助服务系统数据库
CREATE DATABASE IF NOT EXISTS hospital_self_service DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hospital_self_service;

-- 创建设备信息表
CREATE TABLE IF NOT EXISTS device_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    device_id VARCHAR(50) NOT NULL UNIQUE COMMENT '设备唯一标识',
    device_name VARCHAR(100) NOT NULL COMMENT '设备名称',
    device_type VARCHAR(50) NOT NULL COMMENT '设备类型',
    location VARCHAR(200) NOT NULL COMMENT '设备位置',
    status VARCHAR(20) NOT NULL COMMENT '设备状态',
    last_maintenance DATE NOT NULL COMMENT '上次维护时间',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT = '设备信息表';

-- 创建医院信息表
CREATE TABLE IF NOT EXISTS hospital_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    hospital_id VARCHAR(50) NOT NULL UNIQUE COMMENT '医院唯一标识',
    hospital_name VARCHAR(100) NOT NULL COMMENT '医院名称',
    address VARCHAR(200) NOT NULL COMMENT '医院地址',
    phone VARCHAR(20) NOT NULL COMMENT '联系电话',
    website VARCHAR(100) NOT NULL COMMENT '医院官网',
    level VARCHAR(20) NOT NULL COMMENT '医院等级',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT = '医院信息表';

-- 创建首页模块表
CREATE TABLE IF NOT EXISTS home_modules (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    module_id VARCHAR(50) NOT NULL UNIQUE COMMENT '模块唯一标识',
    module_name VARCHAR(100) NOT NULL COMMENT '模块名称',
    module_type VARCHAR(50) NOT NULL COMMENT '模块类型',
    icon VARCHAR(100) NOT NULL COMMENT '模块图标',
    url VARCHAR(100) NOT NULL COMMENT '模块链接',
    `order` INT NOT NULL COMMENT '模块排序',
    device_id VARCHAR(50) NULL COMMENT '关联设备ID（可为空，表示通用模块）',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    FOREIGN KEY (device_id) REFERENCES device_info(device_id) ON DELETE SET NULL
) COMMENT = '首页模块表';

-- 插入设备信息测试数据
INSERT INTO device_info (device_id, device_name, device_type, location, status, last_maintenance) VALUES
('DEV001', '医院自助服务终端', '多功能自助机', '门诊大厅一楼', '正常', '2023-10-15');

-- 插入医院信息测试数据
INSERT INTO hospital_info (hospital_id, hospital_name, address, phone, website, level) VALUES
('HOS001', '人民医院', '北京市朝阳区健康路88号', '010-12345678', 'http://www.renminhospital.com', '三级甲等');

-- 插入首页模块测试数据
INSERT INTO home_modules (module_id, module_name, module_type, icon, url, `order`, device_id) VALUES
('MOD001', '挂号服务', 'service', '挂号图标', '/api/register', 1, NULL),
('MOD002', '缴费服务', 'service', '缴费图标', '/api/payment', 2, NULL),
('MOD003', '报告打印', 'service', '报告图标', '/api/report', 3, NULL),
('MOD004', '病历查询', 'service', '病历图标', '/api/medical-records', 4, NULL),
('MOD005', '医院介绍', 'info', '医院图标', '/api/hospital/intro', 5, NULL);