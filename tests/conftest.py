import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        "id": "14",
        "name": "Apple iPad",
        "data": {
            "Generation": "7th",
            "Price": "799.99",
            "Capacity": "512 GB"
        }
    }
    create_object.new_object(payload)

    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])
