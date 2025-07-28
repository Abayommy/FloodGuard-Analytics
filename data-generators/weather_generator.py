import json
import random
import datetime

def generate_houston_weather():
    """Generate 30 days of realistic Houston weather data for FloodGuard Analytics"""
    
    # Houston area locations with real coordinates
    locations = [
        {"name": "Downtown_Houston", "lat": 29.7604, "lon": -95.3698},
        {"name": "Medical_Center", "lat": 29.7061, "lon": -95.3967}, 
        {"name": "Katy", "lat": 29.7858, "lon": -95.8244},
        {"name": "The_Woodlands", "lat": 30.1588, "lon": -95.4613},
        {"name": "Galveston", "lat": 29.3013, "lon": -94.7977},
        {"name": "Baytown", "lat": 29.7355, "lon": -94.9774},
        {"name": "Sugar_Land", "lat": 29.6196, "lon": -95.6349}
    ]
    
    # Start 30 days ago, generate hourly data
    base_time = datetime.datetime.now() - datetime.timedelta(days=30)
    
    for i in range(720):  # 30 days * 24 hours
        timestamp = base_time + datetime.timedelta(hours=i)
        
        for location in locations:
            # Create realistic weather patterns
            hour = timestamp.hour
            day_of_month = timestamp.day
            
            # Simulate storm events (Harvey-like conditions occasionally)
            is_major_storm = (day_of_month == 15 and hour >= 6 and hour <= 18)  # Simulate one major storm day
            is_minor_storm = random.random() < 0.08  # 8% chance of minor storm
            
            if is_major_storm:
                rainfall_rate = random.uniform(4.0, 12.0)  # Heavy rainfall like Harvey
                wind_speed = random.uniform(35, 75)
                river_level_pct = min(100, random.uniform(85, 98))
                barometric_pressure = random.uniform(28.5, 29.0)
            elif is_minor_storm:
                rainfall_rate = random.uniform(1.0, 4.0)
                wind_speed = random.uniform(20, 45)
                river_level_pct = min(100, random.uniform(60, 85))
                barometric_pressure = random.uniform(29.0, 29.5)
            else:
                rainfall_rate = random.uniform(0, 0.8)
                wind_speed = random.uniform(3, 25)
                river_level_pct = random.uniform(20, 65)
                barometric_pressure = random.uniform(29.5, 30.2)
            
            # Calculate soil saturation (accumulates over time)
            soil_saturation = min(100, rainfall_rate * 12 + random.uniform(10, 30))
            
            # Calculate flood risk score
            risk_components = [
                rainfall_rate / 12.0,  # Normalize to 0-1
                (river_level_pct - 20) / 80.0,  # Normalize to 0-1
                soil_saturation / 100.0,
                max(0, (wind_speed - 20) / 60.0)  # Wind component
            ]
            flood_risk_score = sum(risk_components) / len(risk_components)
            
            weather_event = {
                "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                "location": location["name"],
                "latitude": location["lat"],
                "longitude": location["lon"],
                "rainfall_rate_inches_per_hour": round(rainfall_rate, 2),
                "wind_speed_mph": round(wind_speed, 1),
                "river_level_percentage": round(river_level_pct, 1),
                "soil_saturation_percentage": round(soil_saturation, 1),
                "barometric_pressure": round(barometric_pressure, 2),
                "temperature_f": round(random.uniform(72, 95), 1),
                "humidity_percentage": round(random.uniform(45, 95), 1),
                "flood_risk_score": round(flood_risk_score, 3),
                "event_severity": "major_storm" if is_major_storm else ("minor_storm" if is_minor_storm else "normal"),
                "sensor_id": f"WX_{location['name']}_{random.randint(1000,9999)}"
            }
            
            print(json.dumps(weather_event))

if __name__ == "__main__":
    generate_houston_weather()
