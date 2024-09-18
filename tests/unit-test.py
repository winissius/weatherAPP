from routes import *
from weather import *
from unittest.mock import patch


# Create a cliant for tests, it's a native mode for tests in Flask
def client(self):
    self.app = app.test_client()
    self.app.test = True


def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # ok response
        print(response.status_code)


def test_weather_status():
    with app.test_client() as client:
        response = client.post('/weather', data={'city': 'London'})
        assert response.status_code == 200  # ok response


def test_get_weather_success():
    # data for run the funcion get_weather()
    expected_value = {'cod': 200,
                      'name': 'London',
                     'sys': {'country': 'GB'},
                      'main': {'temp': 15.5},
                     'weather': [{'main': 'Clouds'}]}
    expected_result = {
        'city': 'London',
        'country': 'GB',
        'temperature': 15.5,
        'weather': 'Clouds'
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = expected_value

        result = get_weather('London')
        assert result == expected_result
        # print(result)  # Apenas a primeira chamada dentro do mock
        # print(expected_result)


def test_get_weather_fail():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404  # Mock error HTTP
        mock_get.return_value.json.return_value = {'cod': '404', 'message': 'City not found'}

        result = get_weather('InvalidCity')
        assert result is None # if result is none get_weather received a invalid city


def test_info():
    with app.test_client() as client:
        response = client.get('/info')
        assert response.status_code == 200  # ok response
        print(response.status_code)
