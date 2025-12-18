# 医院自助机接口系统

基于 FastAPI 构建的医院自助服务机接口系统，提供设备信息、医院信息和首页模块列表等服务，使用 MySQL 数据库进行数据存储。

## 项目结构

```
after_api/
├── venv/                 # Python 虚拟环境
├── main.py               # 项目主文件，包含所有接口定义
├── config.py             # 数据库和应用配置文件
├── init.sql              # 数据库初始化脚本
├── requirements.txt      # 项目依赖包列表
└── README.md             # 项目说明文档
```

## 功能接口

### 1. 设备信息接口
- **路径**: `GET /api/device/info`
- **功能**: 获取设备的详细信息
- **参数**: `device_id` (可选，默认 "DEV001")
- **返回格式**: JSON 格式的设备信息对象

### 2. 医院信息接口
- **路径**: `GET /api/hospital/info`
- **功能**: 获取医院的详细信息
- **参数**: `hospital_id` (可选，默认 "HOS001")
- **返回格式**: JSON 格式的医院信息对象

### 3. 首页模块列表接口
- **路径**: `GET /api/device/modules`
- **功能**: 根据设备ID获取该设备的首页功能模块列表
- **参数**: `device_id` (可选，默认 "DEV001")
- **返回格式**: JSON 格式的模块信息列表

## 环境配置

### 1. MySQL 数据库配置
1. 安装 MySQL 数据库（版本 5.7+）
2. 创建数据库用户并赋予相应权限
3. 修改 `config.py` 中的数据库连接配置：
   ```python
   MYSQL_HOST = "localhost"
   MYSQL_PORT = 3306
   MYSQL_USER = "root"
   MYSQL_PASSWORD = "your_password"
   MYSQL_DB = "self_service_machine"
   ```

### 2. 数据库初始化
1. 登录 MySQL 数据库
2. 执行初始化脚本：
   ```bash
   mysql -u root -p < init.sql
   ```
3. 脚本将创建数据库、表结构并插入示例数据

### 3. 虚拟环境创建
```bash
python -m venv venv
```

### 4. 依赖包安装
```bash
venv\Scripts\pip install -r requirements.txt
```

## 项目运行

### 启动开发服务器
```bash
venv\Scripts\uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 访问接口文档
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 数据模型

### DeviceInfo (设备信息)
- `device_id`: 设备ID
- `device_name`: 设备名称
- `device_type`: 设备类型
- `location`: 设备位置
- `status`: 设备状态
- `last_maintenance`: 上次维护时间

### HospitalInfo (医院信息)
- `hospital_id`: 医院ID
- `hospital_name`: 医院名称
- `address`: 医院地址
- `phone`: 联系电话
- `website`: 医院官网
- `level`: 医院等级

### ModuleInfo (模块信息)
- `module_id`: 模块ID
- `module_name`: 模块名称
- `module_type`: 模块类型
- `icon`: 模块图标
- `description`: 模块描述
- `order`: 显示顺序

## 开发说明

- 本项目使用 Python 3.7+ 和 FastAPI 框架
- 使用 Pydantic 进行数据验证和模型定义
- 使用 MySQL 数据库进行数据存储
- 实现了数据库连接池，提高性能和资源利用率
- 所有接口均支持 JSON 格式的请求和响应
- 项目采用虚拟环境管理依赖，确保环境隔离

## 注意事项

- 在生产环境中，请确保关闭调试模式
- 建议使用 HTTPS 协议进行数据传输
- 请根据实际需求修改和扩展接口功能
- 定期维护和更新依赖包，确保系统安全和稳定性
- 确保数据库连接信息的安全性，避免泄露敏感信息
- 建议为数据库操作添加适当的异常处理和日志记录