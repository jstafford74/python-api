from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import DeclarativeBase


# class Base(DeclarativeBase):
#     pass


# db = SQLAlchemy(model_class=Base)
db = SQLAlchemy()

migrate = Migrate()
