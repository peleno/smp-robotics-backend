from db_access import select_all_robots
from robot import RobotSchema
import json


def get_all_robots(request):
    robots = select_all_robots()
    schema = RobotSchema()
    response = [schema.dump(robot) for robot in robots]
    return json.dumps(response)
