import requests

BASE_URL = "https://environment.data.gov.uk/flood-monitoring"


def get_all_stations():
    response = requests.get(f"{BASE_URL}/id/stations", timeout=30)
    response.raise_for_status()
    return response.json()


def get_readings(start_date, end_date):

    params = {
        "startdate": start_date,
        "enddate": end_date,
        "_limit": 10000
    }

    response = requests.get(
        f"{BASE_URL}/data/readings",
        params=params,
        timeout=60
    )

    response.raise_for_status()

    return response.json()