CREATE TABLE weather.nwsdata_improved
(
    dewpoint_c numeric(6,2),
    latitude numeric(10,6),
    location varchar(92),
    longitude numeric(10,6),
    observation_time_rfc822 timestamptz,
    pressure_mb numeric(8,2),
    relative_humidity numeric(8,2),
    station_id varchar(20),
    temp_c numeric(6,2),
    weather varchar(60),
    wind_degrees numeric(6,2),
    wind_dir varchar(58),
    wind_mph numeric(6,2),
    windchill_c numeric(6,2),
    wind_gust_mph numeric(6,2),
    heat_index_c varchar(92)
);

COMMENT ON TABLE weather.nwsdata_improved IS 'this is the new and improved weather data table';

COMMENT ON COLUMN weather.nwsdata_improved.location IS 'the location column is a string that may include city, airport name, state, and should be queried using ilike operator';

COMMENT ON COLUMN weather.nwsdata_improved.weather IS 'the weather column is a string that qualitatively describes the current weather conditions atthe obervation time';

COMMENT ON COLUMN weather.nwsdata_improved.observation_time_rfc822 IS 'the observation_time_rfc822 column is a timestamp when the current row of weather observations were recorded';
