from model.sensors_data import SensorsData
from db_access.session import get_session


def select_all_sensor_records(robot_id):
    session = get_session()
    return session.query(SensorsData).where(SensorsData.robot_id == robot_id).all()


def create_new_record(sensors_data: SensorsData):
    session = get_session()
    session.add(sensors_data)
    session.commit()
