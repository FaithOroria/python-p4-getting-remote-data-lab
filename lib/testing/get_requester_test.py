from GetRequester import GetRequester
import json
class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [{ 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' }, { 'name': 'Joe', 'occupation': 'WiFi Fixer' }, { 'name': 'Avi', 'occupation': 'DJ' }, { 'name': 'Howard', 'occupation': 'Mountain Legend' }]

import json

def test_get_response():
    '''get_response_body function returns response.'''
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    JSON_STRING = '[{"name": "Daniel","occupation": "LG Fridge Salesman"},' \
                  '{"name": "Joe","occupation": "WiFi Fixer"},' \
                  '{"name": "Avi","occupation": "DJ"},' \
                  '{"name": "Howard","occupation": "Mountain Legend"}]'

    requester = GetRequester(URL)
    response_body = requester.get_response_body()

    
    expected_data = json.loads(JSON_STRING)
    if response_body:
        obtained_data = json.loads(response_body)
        assert obtained_data == expected_data
    else:
        assert False, "Failed to retrieve response body"


def test_load_json():
        '''load_json function returns response.'''
        requester = GetRequester(URL)
        assert(requester.load_json() == CONVERTED_DATA)
