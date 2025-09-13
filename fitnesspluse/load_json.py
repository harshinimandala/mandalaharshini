import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def load_fitness_data(json_file):
    """Load fitness data from a JSON file"""
    with open(r"C:\Users\harsh\OneDrive\Desktop\2205A42028\fitnesspluse\sample_fitness_data.json", 'r') as f:
        data = json.load(f)
    return data
fitness_data = load_fitness_data(r"C:\Users\harsh\OneDrive\Desktop\2205A42028\fitnesspluse\sample_fitness_data.json")
print(f"Loaded fitness data for user: {fitness_data['user_id']}")
print(f"Data types available: {fitness_data['data_types']}")
print(f"Total heart rate readings: {len(fitness_data['heart_rate_data'])}")
print(f"Total step readings: {len(fitness_data['step_data'])}")
