import requests

api_key = "af8f22d60626d4f49517880b08738f7c"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Tashkent"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print('API response recieved successfully')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        raise


# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Tashkent, Uzbekistan', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Tashkent', 'country': 'Uzbekistan', 'region': 'Toshkent', 'lat': '41.317', 'lon': '69.250', 'timezone_id': 'Asia/Tashkent', 'localtime': '2026-04-06 12:52', 'localtime_epoch': 1775479920, 'utc_offset': '5.0'}, 'current': {'observation_time': '07:52 AM', 'temperature': 22, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:58 AM', 'sunset': '06:53 PM', 'moonrise': '11:38 PM', 'moonset': '07:39 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 86}, 'air_quality': {'co': '214.85', 'no2': '17.85', 'o3': '26', 'so2': '3.15', 'pm2_5': '11.75', 'pm10': '12.65', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 6, 'wind_degree': 224, 'wind_dir': 'SW', 'pressure': 1005, 'precip': 0, 'humidity': 37, 'cloudcover': 9, 'feelslike': 22, 'uv_index': 6, 'visibility': 10, 'is_day': 'yes'}}