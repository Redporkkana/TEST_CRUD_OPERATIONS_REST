import requests
from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_by_id(self, id):
        self.response = requests.get(url=f'https://api.restful-api.dev/objects/{id}')
        self.response_json = self.response.json()

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id
