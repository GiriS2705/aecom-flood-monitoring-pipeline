import requests

BASE_URL = "https://environment.data.gov.uk/flood-monitoring"

def get_all_stations():
    url = f"{BASE_URL}/id/stations"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()

def get_latest_readings():
    url = f"{BASE_URL}/data/readings"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()