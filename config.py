import os
from sqlalchemy import create_engine  # Corrección en la importación
import urllib

class Config(object):
    SECRET_KEY = 'Clave nueva'
    SESSION_COOKIE_SECURE = False  # Corrección en el nombre del atributo

class DevelopmentConfig(Config):  # Corrección en el nombre de la clase
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mt88xfire@localhost/bdidgs801'  # Corrección en la URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
