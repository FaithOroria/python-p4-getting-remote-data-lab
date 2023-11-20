import requests 

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Request failed with status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                json_data = eval(response_body)  
                return json_data
            except Exception as e:
                print(f"Error loading JSON: {e}")
        return None


def test_get_response():
    '''get_response_body function returns response.'''
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    JSON_STRING = '[{"name": "Daniel","occupation": "LG Fridge Salesman"},' \
                  '{"name": "Joe","occupation": "WiFi Guy"},' \
                  '{"name": "Avi","occupation": "DJ"},' \
                  '{"name": "Howard","occupation": "Mountain Legend"}]'

    requester = GetRequester(URL)
    response_body = requester.get_response_body()
    assert response_body == JSON_STRING


if __name__ == "__main__":
    test_get_response()

