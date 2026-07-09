SELECT

    VALUE:stationReference::STRING AS STATION_REFERENCE,

    IFF(IS_ARRAY(VALUE:label),
        VALUE:label[0]::STRING,
        VALUE:label::STRING) AS STATION_NAME,

    VALUE:riverName::STRING AS RIVER_NAME,

    VALUE:catchmentName::STRING AS CATCHMENT_NAME,

    VALUE:town::STRING AS TOWN,

    IFF(IS_ARRAY(VALUE:lat),
        VALUE:lat[0]::FLOAT,
        VALUE:lat::FLOAT) AS LATITUDE,

    IFF(IS_ARRAY(VALUE:long),
        VALUE:long[0]::FLOAT,
        VALUE:long::FLOAT) AS LONGITUDE,

    IFF(IS_ARRAY(VALUE:easting),
        VALUE:easting[0]::NUMBER,
        VALUE:easting::NUMBER) AS EASTING,

    IFF(IS_ARRAY(VALUE:northing),
        VALUE:northing[0]::NUMBER,
        VALUE:northing::NUMBER) AS NORTHING,

    IFF(IS_ARRAY(VALUE:status),
        VALUE:status[0]::STRING,
        VALUE:status::STRING) AS STATUS

FROM {{ source('raw','bronze_stations') }},
LATERAL FLATTEN(input => RAW_JSON:items)

WHERE VALUE:stationReference IS NOT NULL