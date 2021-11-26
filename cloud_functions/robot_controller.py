from db_access.robot_repository import select_all_robots, create_robot
from model.robot import RobotSchema
import json
from flask import Response


def robot_controller(request):
    schema = RobotSchema()
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return Response(status=204, headers=headers)
    elif request.method == 'GET':
        robots = select_all_robots()
        robot_dicts = [schema.dump(robot) for robot in robots]
        response = Response(json.dumps(robot_dicts), status=200, headers=headers)
        return response
    elif request.method == 'POST':
        new_robot = schema.load(request.json)
        print(new_robot)
        print(type(new_robot))
        create_robot(new_robot)
        return Response(status=200, headers=headers)
