from pydantic import BaseSettings
from pydantic import Field
import os
from logging import config as logging_config
from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

class RedisSettings(BaseSettings):
    host: str = Field(..., env="REDIS_HOST")
    port: int = Field(..., env="REDIS_PORT")

    class Config:
        env_file = '../../../config/.env.app'


class ESSettings(BaseSettings):
    es_host: str = Field(..., env="ELASTIC_HOST")
    es_port: int = Field(..., env="ELASTIC_PORT")

    class Config:
        env_file = '../../../config/.env.app'


class StateSettings(BaseSettings):
    project_name: str = Field(..., env="PROJECT_NAME")

    class Config:
        env_file = '../../../config/.env.app'

#
#
# PROJECT_NAME = os.getenv('PROJECT_NAME', 'movies')
#
# REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
# REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
#
# Elasticsearch
# ELASTIC_HOST = os.getenv('ELASTIC_HOST', '127.0.0.1')
# ELASTIC_PORT = int(os.getenv('ELASTIC_PORT', 9200))
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
