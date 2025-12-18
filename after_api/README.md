# 医院自助机接口系统

基于 FastAPI 构建的医院自助服务机接口系统，提供设备信息、医院信息和首页模块列表等服务。

## 项目结构

```
after_api/
├── venv/                 # Python 虚拟环境
├── main.py               # 项目主文件，包含所有接口定义
├── requirements.txt      # 项目依赖包列表
└── README.md             # 项目说明文档
```

## 功能接口

### 1. 设备信息接口
- **路径**: `GET /api/device/info`
- **功能**: 获取当前设备的详细信息
- **返回格式**: JSON 格式的设备信息对象

### 2. 医院信息接口
- **路径**: `GET /api/hospital/info`
- **功能**: 获取医院的详细信息
- **返回格式**: JSON 格式的医院信息对象

### 3. 首页模块列表接口
- **路径**: `GET /api/device/modules`
- **功能**: 根据设备ID获取该设备的首页功能模块列表
- **参数**: `device_id` (可选，默认使用当前设备ID)
- **返回格式**: JSON 格式的模块信息列表

## 环境配置

### 1. 虚拟环境创建
```bash
python -m venv venv
```

### 2. 依赖包安装
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
- 所有接口均支持 JSON 格式的请求和响应
- 项目采用虚拟环境管理依赖，确保环境隔离

## 注意事项

- 在生产环境中，请确保关闭调试模式
- 建议使用 HTTPS 协议进行数据传输
- 请根据实际需求修改和扩展接口功能
- 定期维护和更新依赖包，确保系统安全和稳定性