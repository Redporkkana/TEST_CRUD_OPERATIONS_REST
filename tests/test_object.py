import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
        "id": "14",
        "name": "Apple iPad",
        "data": {
            "Generation": "7th",
            "Price": "799.99",
            "Capacity": "512 GB"
        }
    }


def test_create_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload)
    new_object_endpoint.check_name(payload['name'])
    new_object_endpoint.check_response_is_200()


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(obj_id)
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_response_id(obj_id)


def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_by_id(obj_id, payload)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_response_name(payload['name'])


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    delete_object_endpoint.check_response_is_200()
    delete_object_endpoint.check_response_is_404()
