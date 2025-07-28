import json
import random
import datetime

def generate_houston_infrastructure():
    """Generate critical infrastructure data for Houston area FloodGuard Analytics"""
    
    # Real Houston-area facilities with actual coordinates
    facilities = [
        # Major Hospitals - High Priority
        {"name": "Texas Medical Center", "type": "hospital", "lat": 29.7061, "lon": -95.3967, "capacity": 2000, "floors": 15},
        {"name": "Memorial Hermann Hospital", "type": "hospital", "lat": 29.7376, "lon": -95.3841, "capacity": 800, "floors": 12},
        {"name": "Houston Methodist Hospital", "type": "hospital", "lat": 29.7199, "lon": -95.3985, "capacity": 900, "floors": 14},
        {"name": "Texas Children's Hospital", "type": "hospital", "lat": 29.7094, "lon": -95.3967, "capacity": 600, "floors": 10},
        {"name": "MD Anderson Cancer Center", "type": "hospital", "lat": 29.7073, "lon": -95.3981, "capacity": 700, "floors": 16},
        
        # Major Schools - Medium-High Priority  
        {"name": "Rice University", "type": "university", "lat": 29.7174, "lon": -95.4018, "capacity": 4000, "floors": 3},
        {"name": "University of Houston", "type": "university", "lat": 29.7199, "lon": -95.3422, "capacity": 37000, "floors": 4},
        {"name": "Texas Southern University", "type": "university", "lat": 29.7199, "lon": -95.3578, "capacity": 9000, "floors": 5},
        {"name": "HISD Bellaire High School", "type": "school", "lat": 29.7058, "lon": -95.4615, "capacity": 3200, "floors": 3},
        {"name": "HISD Lamar High School", "type": "school", "lat": 29.7289, "lon": -95.4112, "capacity": 3100, "floors": 3},
        {"name": "HISD Carnegie Vanguard High", "type": "school", "lat": 29.7273, "lon": -95.3632, "capacity": 1800, "floors": 4},
        {"name": "Katy High School", "type": "school", "lat": 29.7858, "lon": -95.8244, "capacity": 2800, "floors": 2},
        
        # Elderly Care - High Priority
        {"name": "Riverside Senior Living Downtown", "type": "elderly_care", "lat": 29.7504, "lon": -95.3698, "capacity": 150, "floors": 8},
        {"name": "Atria Senior Living Kingwood", "type": "elderly_care", "lat": 29.7861, "lon": -95.2777, "capacity": 200, "floors": 6},
        {"name": "Brookdale Senior Living Medical", "type": "elderly_care", "lat": 29.7156, "lon": -95.3899, "capacity": 180, "floors": 5},
        {"name": "The Woodlands Senior Care", "type": "elderly_care", "lat": 30.1588, "lon": -95.4613, "capacity": 120, "floors": 4},
        
        # Emergency Services - Critical Priority
        {"name": "Houston Fire Department Station 8", "type": "fire_station", "lat": 29.7604, "lon": -95.3698, "capacity": 25, "floors": 2},
        {"name": "Houston Police Department Central", "type": "police_station", "lat": 29.7633, "lon": -95.3632, "capacity": 150, "floors": 3},
        {"name": "Harris County Emergency Operations", "type": "emergency_ops", "lat": 29.7604, "lon": -95.3698, "capacity": 100, "floors": 5}
    ]
    
    current_time = datetime.datetime.now()
    
    for facility in facilities:
        # Calculate base vulnerability score based on facility type
        base_vulnerability = {
            "hospital": 0.95,           # Highest priority - life critical
            "elderly_care": 0.90,       # High priority - vulnerable population  
            "fire_station": 0.85,       # High priority - emergency response
            "police_station": 0.85,     # High priority - emergency response
            "emergency_ops": 0.90,      # High priority - coordination center
            "university": 0.70,         # Medium-high - large population
            "school": 0.75              # Medium-high - children
        }
        
        # Adjust vulnerability based on location factors
        # Lower elevation areas (closer to downtown/coast) = higher risk
        elevation_risk = 0.0
        if facility["lat"] < 29.72:  # Lower elevation areas
            elevation_risk = random.uniform(0.15, 0.25)
        else:
            elevation_risk = random.uniform(0.05, 0.15)
        
        # Building age and construction factors
        building_age_risk = random.uniform(0.05, 0.20)
        
        # Evacuation difficulty based on capacity and floors
        evacuation_difficulty = min(0.3, (facility["capacity"] / 1000) * 0.1 + (facility["floors"] / 20) * 0.1)
        
        # Historical flooding in area (some areas more prone)
        historical_flood_risk = 0.0
        if "Downtown" in facility["name"] or facility["lat"] < 29.71:
            historical_flood_risk = random.uniform(0.10, 0.20)
        elif "Medical" in facility["name"]:
            historical_flood_risk = random.uniform(0.08, 0.15)
        else:
            historical_flood_risk = random.uniform(0.02, 0.10)
        
        # Calculate total vulnerability score (capped at 1.0)
        total_vulnerability = min(1.0, 
            base_vulnerability[facility["type"]] + 
            elevation_risk + 
            building_age_risk + 
            evacuation_difficulty + 
            historical_flood_risk
        )
        
        # Generate emergency contact info
        emergency_contacts = {
            "hospital": f"713-555-{random.randint(1000,9999)}",
            "elderly_care": f"713-555-{random.randint(1000,9999)}",
            "fire_station": "911",
            "police_station": "911", 
            "emergency_ops": f"713-555-{random.randint(1000,9999)}",
            "university": f"713-555-{random.randint(1000,9999)}",
            "school": f"713-555-{random.randint(1000,9999)}"
        }
        
        infrastructure_record = {
            "timestamp": current_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "facility_id": f"{facility['type']}_{hash(facility['name']) % 10000}",
            "name": facility["name"],
            "type": facility["type"], 
            "latitude": facility["lat"],
            "longitude": facility["lon"],
            "capacity": facility["capacity"],
            "floors": facility["floors"],
            "base_vulnerability": round(base_vulnerability[facility["type"]], 3),
            "elevation_risk": round(elevation_risk, 3),
            "building_age_risk": round(building_age_risk, 3),
            "evacuation_difficulty": round(evacuation_difficulty, 3),
            "historical_flood_risk": round(historical_flood_risk, 3),
            "total_vulnerability_score": round(total_vulnerability, 3),
            "status": "operational",
            "emergency_contact": emergency_contacts[facility["type"]],
            "evacuation_plan_status": random.choice(["current", "needs_update", "under_review"]),
            "backup_power": random.choice([True, False]),
            "flood_insurance": random.choice([True, False]),
            "last_inspection_date": (current_time - datetime.timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
        }
        
        print(json.dumps(infrastructure_record))

if __name__ == "__main__":
    generate_houston_infrastructure()
