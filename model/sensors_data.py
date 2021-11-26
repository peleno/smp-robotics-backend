from marshmallow import Schema, fields, post_load
from sqlalchemy import Integer, Column, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SensorsData(Base):
    __tablename__ = 'sensors_data'
    timestamp = Column(DateTime, primary_key=True)
    robot_id = Column(Integer)
    speed = Column(Integer)
    battery = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)
    temperature = Column(Integer)


class SensorsDataSchema(Schema):
    __tablename__ = 'robot'
    timestamp = fields.DateTime()
    robot_id = fields.Integer()
    speed = fields.Integer()
    battery = fields.Integer()
    latitude = fields.Integer()
    longitude = fields.Integer()
    temperature = fields.Integer()

    @post_load
    def make_robot(self, data, **kwargs):
        return SensorsData(**data)
