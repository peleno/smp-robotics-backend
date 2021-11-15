import flask
from flask import Flask, json, request
# from flask_mysqldb import MySQL
from flask_cors import CORS
# from cloud_functions_robot_controller import get_all_robots
from cloud_functions.get_all_robots import get_all_robots
from cloud_functions.robot_controller import robot_controller

app = Flask(__name__)
CORS(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'andrii'
# app.config['MYSQL_PASSWORD'] = 'Wireless802.11ac'
# app.config['MYSQL_DB'] = 'smp_robotics_db'

# mysql = MySQL(app)


# class Robot:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


@app.route('/')
def hello_world():
    return get_all_robots(request)
    # cur = mysql.connection.cursor()
    # cur.execute("select * from robot;")
    # robots = [Robot(rob[0], rob[1]) for rob in cur.fetchall()]
    # robots_dict = [{'id': robot.id, 'name': robot.name} for robot in robots]
    # print(robots_dict)
    # return json.dumps(robots_dict)


@app.route('/robot', methods=["GET", "POST"])
def robot_controller_handler():
    return robot_controller(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
