from datetime import datetime, timedelta, UTC

from api_client import get_all_stations, get_readings
from s3_upload import upload_json
from metadata import get_last_successful_load, update_last_successful_load


def main():
    # Current date for S3 partitioning
    today = datetime.now(UTC)
    timestamp = today.strftime("%Y%m%d_%H%M%S")

    # Date range for one week's data
    end_date = today.strftime("%Y-%m-%d")
    start_date = get_last_successful_load()

    print(f"Incremental Load")
    print(f"Start Date : {start_date}")
    print(f"End Date   : {end_date}")

    print(f"Fetching stations...")
    stations = get_all_stations()

    station_key = (
    f"flood-monitoring/raw/stations/"
    f"year={today.year}/"
    f"month={today.strftime('%m')}/"
    f"day={today.strftime('%d')}/"
    f"stations_{timestamp}.json"
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
    f"readings_{timestamp}.json"
)

    upload_json(readings, reading_key)

    print("\nPipeline completed successfully.")

    update_last_successful_load()
    print("Metadata updated successfully.")


if __name__ == "__main__":
    main()