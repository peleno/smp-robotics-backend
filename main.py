import os

from flask import Flask, request
from flask_cors import CORS

from cloud_functions.robot_controller import robot_controller
from cloud_functions.sensors_data_controller import get_all_records_for_robot, create_sensor_record

app = Flask(__name__)
CORS(app)


@app.route('/robot', methods=["GET", "POST"])
def robot_controller_handler():
    return robot_controller(request)


@app.route('/robot/<robot_id>/monitor', methods=["GET"])
def sensors_data_records_handler(robot_id):
    return get_all_records_for_robot(request)


@app.route('/sensor_data_record', methods=["POST"])
def create_sensor_handler():
    return create_sensor_record(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get("PORT", 8080)))
