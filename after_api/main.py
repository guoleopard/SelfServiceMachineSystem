from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI(title="医院自助机接口系统", version="1.0.0")

# 数据模型
class DeviceInfo(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    location: str
    status: str
    last_maintenance: Optional[str] = None

class HospitalInfo(BaseModel):
    hospital_id: str
    hospital_name: str
    address: str
    phone: str
    website: Optional[str] = None
    level: str

class ModuleInfo(BaseModel):
    module_id: str
    module_name: str
    module_type: str
    icon: Optional[str] = None
    description: Optional[str] = None
    order: int

# 模拟数据
mock_device_info = DeviceInfo(
    device_id="DEV001",
    device_name="门诊自助服务机",
    device_type="门诊服务",
    location="门诊大厅一楼",
    status="正常",
    last_maintenance="2023-10-01"
)

mock_hospital_info = HospitalInfo(
    hospital_id="HOS001",
    hospital_name="人民医院",
    address="北京市朝阳区健康路88号",
    phone="010-12345678",
    website="www.renminhospital.com",
    level="三级甲等"
)

mock_modules = {
    "DEV001": [
        ModuleInfo(module_id="MOD001", module_name="挂号服务", module_type="registration", icon="registration.png", description="门诊挂号、预约挂号", order=1),
        ModuleInfo(module_id="MOD002", module_name="缴费服务", module_type="payment", icon="payment.png", description="门诊缴费、住院缴费", order=2),
        ModuleInfo(module_id="MOD003", module_name="报告打印", module_type="report", icon="report.png", description="检验报告、检查报告打印", order=3),
        ModuleInfo(module_id="MOD004", module_name="预约查询", module_type="query", icon="query.png", description="预约信息查询、就诊记录查询", order=4),
        ModuleInfo(module_id="MOD005", module_name="健康咨询", module_type="consultation", icon="consultation.png", description="健康知识、就医指南", order=5)
    ],
    "DEV002": [
        ModuleInfo(module_id="MOD001", module_name="挂号服务", module_type="registration", icon="registration.png", description="门诊挂号、预约挂号", order=1),
        ModuleInfo(module_id="MOD002", module_name="缴费服务", module_type="payment", icon="payment.png", description="门诊缴费、住院缴费", order=2)
    ]
}

# 设备信息接口
@app.get("/api/device/info", response_model=DeviceInfo, summary="获取设备信息")
def get_device_info():
    """获取当前设备的详细信息"""
    return mock_device_info

# 医院信息接口
@app.get("/api/hospital/info", response_model=HospitalInfo, summary="获取医院信息")
def get_hospital_info():
    """获取医院的详细信息"""
    return mock_hospital_info

# 根据设备信息获取首页模块列表接口
@app.get("/api/device/modules", response_model=List[ModuleInfo], summary="获取设备首页模块列表")
def get_device_modules(device_id: Optional[str] = None):
    """根据设备ID获取该设备的首页功能模块列表"""
    if not device_id:
        device_id = mock_device_info.device_id
    
    if device_id in mock_modules:
        return mock_modules[device_id]
    else:
        raise HTTPException(status_code=404, detail=f"设备 {device_id} 未找到或没有配置模块")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)