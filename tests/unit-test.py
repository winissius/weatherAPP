from routes import *
from weather import *
from unittest.mock import patch


# Create a client for tests, it's a native mode for tests in Flask
def client(self):
    self.app = app.test_client()
    self.app.test = True


def test_index(): # test index/homepage
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # ok response
        print(response.status_code)


def test_weather_status(): # test rendering page with post method for data
    with app.test_client() as client:
        response = client.post('/weather', data={'city': 'London'})
        assert response.status_code == 200  # ok response


def test_get_weather_success():
    # data for run the funcion get_weather() - data input
    expected_value = {'cod': 200,
                      'name': 'London',
                     'sys': {'country': 'GB'},
                      'main': {'temp': 15.5},
                     'weather': [{'main': 'Clouds'}]}
    # result expected - data output
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

def test_get_weather_fail():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'cod': '404', 'message': 'City not found'}
        result = get_weather('InvalidCity')
        assert result == {'error': 'City not found'} # if result is none get_weather received a invalid city


def test_get_weather_invalid_city_empty(): # check empity field
    result = get_weather('')
    assert result == {'error': 'City not found'}


def test_get_weather_invalid_city_non_string(): # check numeric field
    result = get_weather(123)
    assert result == {'error': 'City not found'}


def test_info(): # test info page
    with app.test_client() as client:
        response = client.get('/info')
        assert response.status_code == 200  # ok response
