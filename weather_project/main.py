from weather_analysis import load_weather_data, calculate_average_temperature, calculate_average_humidity

def main():
    filepath = 'data/weather_data.csv'
    weather_data = load_weather_data(filepath)
    
    avg_temp = calculate_average_temperature(weather_data)
    avg_humidity = calculate_average_humidity(weather_data)
    
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")

if __name__ == "__main__":
    main()
