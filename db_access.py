import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from robot import Robot

Session = sessionmaker()

db_user = os.environ["MYSQL_USER"]
db_pass = os.environ["MYSQL_PASSWORD"]
db_name = os.environ["MYSQL_DB"]
db_host = os.environ["MYSQL_HOST"]
db_port = os.environ["MYSQL_PORT"]


def get_session():
    engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_host,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 3306
            database=db_name,  # e.g. "my-database-name"
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800
    )
    session = Session(bind=engine)
    return session


def select_all_robots():
    session = get_session()
    return session.query(Robot).order_by(Robot.id).all()


def create_robot(robot: Robot):
    session = get_session()
    session.add(robot)
    session.commit()


def delete_robot(robot_id):
    session = get_session()
    session.query(Robot).filter(Robot.id == robot_id).delete()
    session.commit()


def update_robot(new_robot):
    session = get_session()
    if new_robot.id is None:
        raise Exception("Id of robot to be updated is not specified")
    robot_to_update = session.query(Robot).filter(Robot.id == new_robot.id).first()
    if new_robot.name is not None:
        robot_to_update.name = new_robot.name
    if new_robot.route_id is not None:
        robot_to_update.route_id = new_robot.route_id
    if new_robot.type is not None:
        robot_to_update.type = new_robot.type
    if new_robot.patrolling_start is not None:
        robot_to_update.patrolling_start = new_robot.patrolling_start
    if new_robot.patrolling_end is not None:
        robot_to_update.patrolling_end = new_robot.patrolling_end
    session.commit()


if __name__ == '__main__':
    # create_robot(Robot(name='robot-M',
    #                    route_id=1,
    #                    type='DW',
    #                    patrolling_start=datetime.time(hour=3),
    #                    patrolling_end=datetime.time(hour=22)))
    # delete_robot(2)
    # update_robot(Robot(id=3, type='BBBB'))
    print(select_all_robots())
