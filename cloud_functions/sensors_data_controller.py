from db_access.sensors_data_repository import select_all_sensor_records
from model.sensors_data import SensorsDataSchema
from json import dumps
from flask import Response


def sensors_data_controller(request):
    schema = SensorsDataSchema()
    print(f'robot id: {request.view_args["robot_id"]}')
    sensor_records = select_all_sensor_records(request.view_args['robot_id'])
    sensor_record_dicts = [schema.dump(sensor_record) for sensor_record in sensor_records]
    response = Response(dumps(sensor_record_dicts), status=200)
    return response
