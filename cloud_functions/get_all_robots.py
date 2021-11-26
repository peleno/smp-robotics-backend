from db_access.robot_repository import select_all_robots
from model.robot import RobotSchema
import json


def get_all_robots(request):
    robots = select_all_robots()
    schema = RobotSchema()
    response = [schema.dump(robot) for robot in robots]
    return json.dumps(response)
