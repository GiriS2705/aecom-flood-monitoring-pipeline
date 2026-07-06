from api_client import get_all_stations
from s3_upload import upload_json
from datetime import datetime

def main():

    print("Fetching monitoring stations...")

    stations = get_all_stations()

    today = datetime.utcnow().strftime("%Y/%m/%d")

    object_key = f"flood-monitoring/raw/{today}/stations.json"

    upload_json(stations, object_key)

if __name__ == "__main__":
    main()