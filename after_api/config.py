# 数据库配置文件

class Config:
    """应用程序配置类"""
    # MySQL 数据库连接配置
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "password"
    MYSQL_DB = "self_service_machine"
    MYSQL_CHARSET = "utf8mb4"
    
    # 连接池配置
    POOL_SIZE = 5
    MAX_OVERFLOW = 10
    POOL_TIMEOUT = 30
    POOL_RECYCLE = 1800
    
    # 应用程序配置
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8000

# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True

# 生产环境配置
class ProductionConfig(Config):
    DEBUG = False
    MYSQL_HOST = "your_production_host"
    MYSQL_USER = "your_production_user"
    MYSQL_PASSWORD = "your_production_password"
    MYSQL_DB = "self_service_machine"

# 配置映射
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}