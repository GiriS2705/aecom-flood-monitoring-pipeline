from datetime import datetime, timedelta, UTC

from api_client import get_all_stations, get_readings
from s3_upload import upload_json


def main():
    # Current date for S3 partitioning
    today = datetime.now(UTC)

    # Date range for one week's data
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=7)).strftime("%Y-%m-%d")

    print(f"Fetching stations...")
    stations = get_all_stations()

    station_key = (
        f"flood-monitoring/raw/stations/"
        f"year={today.year}/"
        f"month={today.strftime('%m')}/"
        f"day={today.strftime('%d')}/"
        f"stations.json"
    )

    upload_json(stations, station_key)

    print(f"Fetching readings from {start_date} to {end_date}...")

    readings = get_readings(start_date, end_date)

    print(f"Total Readings Retrieved: {len(readings['items'])}")

    reading_key = (
        f"flood-monitoring/raw/readings/"
        f"year={today.year}/"
        f"month={today.strftime('%m')}/"
        f"day={today.strftime('%d')}/"
        f"readings.json"
    )

    upload_json(readings, reading_key)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()