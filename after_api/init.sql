-- 医院自助机系统 数据库初始化脚本
-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS self_service_machine DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE self_service_machine;

-- 设备信息表
CREATE TABLE IF NOT EXISTS device_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    device_id VARCHAR(50) NOT NULL UNIQUE COMMENT '设备唯一标识',
    device_name VARCHAR(100) NOT NULL COMMENT '设备名称',
    device_type VARCHAR(50) NOT NULL COMMENT '设备类型',
    location VARCHAR(200) NOT NULL COMMENT '设备位置',
    status VARCHAR(20) NOT NULL DEFAULT '正常' COMMENT '设备状态',
    last_maintenance DATE NULL COMMENT '上次维护时间',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='设备信息表';

-- 医院信息表
CREATE TABLE IF NOT EXISTS hospital_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    hospital_id VARCHAR(50) NOT NULL UNIQUE COMMENT '医院唯一标识',
    hospital_name VARCHAR(100) NOT NULL COMMENT '医院名称',
    address VARCHAR(200) NOT NULL COMMENT '医院地址',
    phone VARCHAR(20) NOT NULL COMMENT '联系电话',
    website VARCHAR(100) NULL COMMENT '医院官网',
    level VARCHAR(20) NOT NULL COMMENT '医院等级',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='医院信息表';

-- 模块信息表
CREATE TABLE IF NOT EXISTS module_info (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    module_id VARCHAR(50) NOT NULL UNIQUE COMMENT '模块唯一标识',
    module_name VARCHAR(100) NOT NULL COMMENT '模块名称',
    module_type VARCHAR(50) NOT NULL COMMENT '模块类型',
    icon VARCHAR(100) NULL COMMENT '模块图标',
    description VARCHAR(200) NULL COMMENT '模块描述',
    `order` INT NOT NULL DEFAULT 0 COMMENT '显示顺序',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='模块信息表';

-- 设备模块关联表
CREATE TABLE IF NOT EXISTS device_module (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    device_id VARCHAR(50) NOT NULL COMMENT '设备ID',
    module_id VARCHAR(50) NOT NULL COMMENT '模块ID',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    FOREIGN KEY (device_id) REFERENCES device_info(device_id) ON DELETE CASCADE,
    FOREIGN KEY (module_id) REFERENCES module_info(module_id) ON DELETE CASCADE,
    UNIQUE KEY uk_device_module (device_id, module_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='设备模块关联表';

-- 插入示例数据
-- 设备信息
INSERT INTO device_info (device_id, device_name, device_type, location, status, last_maintenance) VALUES
('DEV001', '门诊自助服务机', '门诊服务', '门诊大厅一楼', '正常', '2023-10-01'),
('DEV002', '住院部自助服务机', '住院服务', '住院部二楼', '正常', '2023-09-15');

-- 医院信息
INSERT INTO hospital_info (hospital_id, hospital_name, address, phone, website, level) VALUES
('HOS001', '人民医院', '北京市朝阳区健康路88号', '010-12345678', 'www.renminhospital.com', '三级甲等');

-- 模块信息
INSERT INTO module_info (module_id, module_name, module_type, icon, description, `order`) VALUES
('MOD001', '挂号服务', 'registration', 'registration.png', '门诊挂号、预约挂号', 1),
('MOD002', '缴费服务', 'payment', 'payment.png', '门诊缴费、住院缴费', 2),
('MOD003', '报告打印', 'report', 'report.png', '检验报告、检查报告打印', 3),
('MOD004', '预约查询', 'query', 'query.png', '预约信息查询、就诊记录查询', 4),
('MOD005', '健康咨询', 'consultation', 'consultation.png', '健康知识、就医指南', 5);

-- 设备模块关联
INSERT INTO device_module (device_id, module_id) VALUES
('DEV001', 'MOD001'),
('DEV001', 'MOD002'),
('DEV001', 'MOD003'),
('DEV001', 'MOD004'),
('DEV001', 'MOD005'),
('DEV002', 'MOD001'),
('DEV002', 'MOD002');