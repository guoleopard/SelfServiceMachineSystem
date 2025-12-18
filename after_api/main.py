from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import mysql.connector
from mysql.connector import pooling
from config import config

app = FastAPI(title="医院自助机接口系统", version="1.0.0")

# 数据库连接池
class DatabasePool:
    def __init__(self, config):
        self.pool = pooling.MySQLConnectionPool(
            pool_name="self_service_machine_pool",
            pool_size=config.POOL_SIZE,
            pool_reset_session=True,
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DB,
            charset=config.MYSQL_CHARSET
        )
    
    def get_connection(self):
        return self.pool.get_connection()

# 初始化数据库连接池
app_config = config["default"]
db_pool = DatabasePool(app_config)

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

# 设备信息接口
@app.get("/api/device/info", response_model=DeviceInfo, summary="获取设备信息")
def get_device_info(device_id: Optional[str] = "DEV001"):
    """获取设备的详细信息"""
    connection = None
    try:
        connection = db_pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT device_id, device_name, device_type, location, status, "
        query += "DATE_FORMAT(last_maintenance, '%Y-%m-%d') as last_maintenance "
        query += "FROM device_info WHERE device_id = %s"
        
        cursor.execute(query, (device_id,))
        result = cursor.fetchone()
        
        if result:
            return DeviceInfo(**result)
        else:
            raise HTTPException(status_code=404, detail=f"设备 {device_id} 未找到")
            
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    finally:
        if connection:
            connection.close()

# 医院信息接口
@app.get("/api/hospital/info", response_model=HospitalInfo, summary="获取医院信息")
def get_hospital_info(hospital_id: Optional[str] = "HOS001"):
    """获取医院的详细信息"""
    connection = None
    try:
        connection = db_pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT hospital_id, hospital_name, address, phone, website, level "
        query += "FROM hospital_info WHERE hospital_id = %s"
        
        cursor.execute(query, (hospital_id,))
        result = cursor.fetchone()
        
        if result:
            return HospitalInfo(**result)
        else:
            raise HTTPException(status_code=404, detail=f"医院 {hospital_id} 未找到")
            
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    finally:
        if connection:
            connection.close()

# 根据设备信息获取首页模块列表接口
@app.get("/api/device/modules", response_model=List[ModuleInfo], summary="获取设备首页模块列表")
def get_device_modules(device_id: Optional[str] = "DEV001"):
    """根据设备ID获取该设备的首页功能模块列表"""
    connection = None
    try:
        connection = db_pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT m.module_id, m.module_name, m.module_type, m.icon, m.description, m.`order` "
        query += "FROM module_info m JOIN device_module dm ON m.module_id = dm.module_id "
        query += "WHERE dm.device_id = %s ORDER BY m.`order` ASC"
        
        cursor.execute(query, (device_id,))
        results = cursor.fetchall()
        
        if results:
            return [ModuleInfo(**row) for row in results]
        else:
            raise HTTPException(status_code=404, detail=f"设备 {device_id} 未找到或没有配置模块")
            
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=app_config.HOST, port=app_config.PORT)