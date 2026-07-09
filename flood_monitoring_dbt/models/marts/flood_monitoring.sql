SELECT

    r.STATION_REFERENCE,
    s.STATION_NAME,
    s.RIVER_NAME,
    s.CATCHMENT_NAME,
    s.TOWN,
    s.LATITUDE,
    s.LONGITUDE,
    r.READING_TIME,
    r.WATER_LEVEL

FROM {{ ref('stg_readings') }} r

LEFT JOIN {{ ref('stg_stations') }} s

ON r.STATION_REFERENCE = s.STATION_REFERENCE