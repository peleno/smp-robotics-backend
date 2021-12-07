import base64
import json

from db_access.sensors_data_repository import select_all_sensor_records, create_new_record
from model.sensors_data import SensorsDataSchema
from json import dumps
from flask import Response


def get_all_records_for_robot(request):
    schema = SensorsDataSchema()
    sensor_records = select_all_sensor_records(request.view_args['robot_id'])
    sensor_record_dicts = [schema.dump(sensor_record) for sensor_record in sensor_records]
    response = Response(dumps(sensor_record_dicts), status=200)
    return response


def create_sensor_record(request):
    envelope = request.get_json()
    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = envelope["message"]

    sensor_record_json = {}
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        sensor_record_string = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
        sensor_record_json = json.loads(sensor_record_string)

    schema = SensorsDataSchema()
    new_record = schema.load(sensor_record_json)
    create_new_record(new_record)
    return Response(status=204)
