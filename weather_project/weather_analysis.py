import csv
from datetime import datetime

class WeatherData:
    def __init__(self, date, temperature, humidity):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.temperature = float(temperature)
        self.humidity = float(humidity)

    def __repr__(self):
        return f"WeatherData(date={self.date}, temperature={self.temperature}, humidity={self.humidity})"

def load_weather_data(filepath):
    weather_data = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            weather_data.append(WeatherData(row['date'], row['temperature'], row['humidity']))
    return weather_data

def calculate_average_temperature(weather_data):
    total_temp = sum(data.temperature for data in weather_data)
    return total_temp / len(weather_data)

def calculate_average_humidity(weather_data):
    total_humidity = sum(data.humidity for data in weather_data)
    return total_humidity / len(weather_data)
