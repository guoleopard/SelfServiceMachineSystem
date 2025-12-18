from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="医院自助机接口系统", version="1.0.0")

# 设备信息模型
class DeviceInfo(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    location: str
    status: str
    last_maintenance: str

# 医院信息模型
class HospitalInfo(BaseModel):
    hospital_id: str
    hospital_name: str
    address: str
    phone: str
    website: str
    level: str

# 首页模块模型
class HomeModule(BaseModel):
    module_id: str
    module_name: str
    module_type: str
    icon: str
    url: str
    order: int

# 设备信息接口
@app.get("/api/device/info", response_model=DeviceInfo, summary="获取设备信息")
def get_device_info():
    """获取医院自助机的设备信息"""
    return {
        "device_id": "DEV001",
        "device_name": "医院自助服务终端",
        "device_type": "多功能自助机",
        "location": "门诊大厅一楼",
        "status": "正常",
        "last_maintenance": "2023-10-15"
    }

# 医院信息接口
@app.get("/api/hospital/info", response_model=HospitalInfo, summary="获取医院信息")
def get_hospital_info():
    """获取医院的基本信息"""
    return {
        "hospital_id": "HOS001",
        "hospital_name": "人民医院",
        "address": "北京市朝阳区健康路88号",
        "phone": "010-12345678",
        "website": "http://www.renminhospital.com",
        "level": "三级甲等"
    }

# 根据设备信息获取首页模块列表接口
@app.get("/api/home/modules", response_model=list[HomeModule], summary="获取首页模块列表")
def get_home_modules(device_id: str = None):
    """根据设备信息获取首页模块列表"""
    modules = [
        {
            "module_id": "MOD001",
            "module_name": "挂号服务",
            "module_type": "service",
            "icon": "挂号图标",
            "url": "/api/register",
            "order": 1
        },
        {
            "module_id": "MOD002",
            "module_name": "缴费服务",
            "module_type": "service",
            "icon": "缴费图标",
            "url": "/api/payment",
            "order": 2
        },
        {
            "module_id": "MOD003",
            "module_name": "报告打印",
            "module_type": "service",
            "icon": "报告图标",
            "url": "/api/report",
            "order": 3
        },
        {
            "module_id": "MOD004",
            "module_name": "病历查询",
            "module_type": "service",
            "icon": "病历图标",
            "url": "/api/medical-records",
            "order": 4
        },
        {
            "module_id": "MOD005",
            "module_name": "医院介绍",
            "module_type": "info",
            "icon": "医院图标",
            "url": "/api/hospital/intro",
            "order": 5
        }
    ]
    
    # 如果提供了设备ID，可以根据设备ID返回不同的模块列表
    if device_id:
        # 这里可以添加根据设备ID定制模块的逻辑
        pass
    
    return modules

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)