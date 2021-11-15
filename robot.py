from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, Time

from marshmallow import Schema, fields, post_load

Base = declarative_base()


class Robot(Base):
    __tablename__ = 'robot'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    route_id = Column(Integer)
    type = Column(String)
    patrolling_start = Column(Time)
    patrolling_end = Column(Time)

    def __repr__(self):
        return f"<Robot(name={self.name}, route={self.route_id}, type={self.type}," \
               f"patrolling_start={self.patrolling_start}, patrolling_end={self.patrolling_end})>"


class RobotSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    route_id = fields.Integer()
    type = fields.Str()
    patrolling_start = fields.Time()
    patrolling_end = fields.Time()

    @post_load
    def make_robot(self, data, **kwargs):
        return Robot(**data)
