from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from datetime import datetime

# 加载环境变量
load_dotenv()

# 数据库连接配置
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# 创建数据库连接
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="医院自助机接口系统", version="1.0.0")

# 数据库模型定义
class DeviceInfoDB(Base):
    __tablename__ = "device_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device_id = Column(String(50), unique=True, index=True, nullable=False)
    device_name = Column(String(100), nullable=False)
    device_type = Column(String(50), nullable=False)
    location = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False)
    last_maintenance = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

class HospitalInfoDB(Base):
    __tablename__ = "hospital_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hospital_id = Column(String(50), unique=True, index=True, nullable=False)
    hospital_name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=False)
    website = Column(String(100), nullable=False)
    level = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

class HomeModuleDB(Base):
    __tablename__ = "home_modules"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    module_id = Column(String(50), unique=True, index=True, nullable=False)
    module_name = Column(String(100), nullable=False)
    module_type = Column(String(50), nullable=False)
    icon = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)
    order = Column(Integer, nullable=False)
    device_id = Column(String(50), ForeignKey("device_info.device_id"), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

# Pydantic 模型定义（用于 API 响应）
class DeviceInfo(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    location: str
    status: str
    last_maintenance: str

    class Config:
        orm_mode = True

class HospitalInfo(BaseModel):
    hospital_id: str
    hospital_name: str
    address: str
    phone: str
    website: str
    level: str

    class Config:
        orm_mode = True

class HomeModule(BaseModel):
    module_id: str
    module_name: str
    module_type: str
    icon: str
    url: str
    order: int

    class Config:
        orm_mode = True

# 获取数据库会话

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 设备信息接口
@app.get("/api/device/info", response_model=DeviceInfo, summary="获取设备信息")
def get_device_info(db: SessionLocal = Depends(get_db)):
    """获取医院自助机的设备信息"""
    device = db.query(DeviceInfoDB).first()
    if device:
        return DeviceInfo(
            device_id=device.device_id,
            device_name=device.device_name,
            device_type=device.device_type,
            location=device.location,
            status=device.status,
            last_maintenance=str(device.last_maintenance)
        )
    return None

# 医院信息接口
@app.get("/api/hospital/info", response_model=HospitalInfo, summary="获取医院信息")
def get_hospital_info(db: SessionLocal = Depends(get_db)):
    """获取医院的基本信息"""
    hospital = db.query(HospitalInfoDB).first()
    if hospital:
        return HospitalInfo(
            hospital_id=hospital.hospital_id,
            hospital_name=hospital.hospital_name,
            address=hospital.address,
            phone=hospital.phone,
            website=hospital.website,
            level=hospital.level
        )
    return None

# 根据设备信息获取首页模块列表接口
@app.get("/api/home/modules", response_model=list[HomeModule], summary="获取首页模块列表")
def get_home_modules(device_id: str = None, db: SessionLocal = Depends(get_db)):
    """根据设备信息获取首页模块列表"""
    if device_id:
        # 查询特定设备的模块和通用模块
        modules = db.query(HomeModuleDB).filter(
            (HomeModuleDB.device_id == device_id) | (HomeModuleDB.device_id == None)
        ).order_by(HomeModuleDB.order).all()
    else:
        # 查询通用模块
        modules = db.query(HomeModuleDB).filter(HomeModuleDB.device_id == None).order_by(HomeModuleDB.order).all()
    
    result = []
    for module in modules:
        result.append(HomeModule(
            module_id=module.module_id,
            module_name=module.module_name,
            module_type=module.module_type,
            icon=module.icon,
            url=module.url,
            order=module.order
        ))
    
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)