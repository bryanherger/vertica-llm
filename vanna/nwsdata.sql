                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  export_objects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 

CREATE TABLE weather.nwsdata
(
    copyright_url varchar(78),
    credit varchar(136),
    credit_url varchar(54),
    dewpoint_c numeric(6,2),
    dewpoint_f numeric(6,2),
    dewpoint_string varchar(30),
    disclaimer_url varchar(78),
    icon_url_base varchar(92),
    icon_url_name varchar(90),
    latitude numeric(10,6),
    location varchar(92),
    longitude numeric(10,6),
    ob_url varchar(90),
    observation_time varchar(82),
    observation_time_rfc822 timestamptz,
    pressure_in numeric(7,3),
    pressure_mb numeric(8,2),
    pressure_string varchar(62),
    privacy_policy_url varchar(70),
    relative_humidity numeric(8,2),
    station_id varchar(20),
    suggested_pickup varchar(70),
    suggested_pickup_period numeric(6,2),
    temp_c numeric(6,2),
    temp_f numeric(7,3),
    temperature_string varchar(48),
    two_day_history_url varchar(96),
    visibility_mi numeric(7,3),
    weather varchar(60),
    wind_degrees numeric(6,2),
    wind_dir varchar(58),
    wind_kt numeric(6,2),
    wind_mph numeric(6,2),
    wind_string varchar(136),
    windchill_c numeric(6,2),
    windchill_f int,
    windchill_string varchar(22),
    wind_gust_kt numeric(6,2),
    wind_gust_mph numeric(6,2),
    heat_index_c varchar(92),
    heat_index_f varchar(20),
    heat_index_string varchar(22)
);


CREATE PROJECTION weather.nwsdata_super /*+basename(nwsdata),createtype(A)*/ 
(
 copyright_url,
 credit,
 credit_url,
 dewpoint_c,
 dewpoint_f,
 dewpoint_string,
 disclaimer_url,
 icon_url_base,
 icon_url_name,
 latitude,
 location,
 longitude,
 ob_url,
 observation_time,
 observation_time_rfc822,
 pressure_in,
 pressure_mb,
 pressure_string,
 privacy_policy_url,
 relative_humidity,
 station_id,
 suggested_pickup,
 suggested_pickup_period,
 temp_c,
 temp_f,
 temperature_string,
 two_day_history_url,
 visibility_mi,
 weather,
 wind_degrees,
 wind_dir,
 wind_kt,
 wind_mph,
 wind_string,
 windchill_c,
 windchill_f,
 windchill_string,
 wind_gust_kt,
 wind_gust_mph,
 heat_index_c,
 heat_index_f,
 heat_index_string
)
AS
 SELECT nwsdata.copyright_url,
        nwsdata.credit,
        nwsdata.credit_url,
        nwsdata.dewpoint_c,
        nwsdata.dewpoint_f,
        nwsdata.dewpoint_string,
        nwsdata.disclaimer_url,
        nwsdata.icon_url_base,
        nwsdata.icon_url_name,
        nwsdata.latitude,
        nwsdata.location,
        nwsdata.longitude,
        nwsdata.ob_url,
        nwsdata.observation_time,
        nwsdata.observation_time_rfc822,
        nwsdata.pressure_in,
        nwsdata.pressure_mb,
        nwsdata.pressure_string,
        nwsdata.privacy_policy_url,
        nwsdata.relative_humidity,
        nwsdata.station_id,
        nwsdata.suggested_pickup,
        nwsdata.suggested_pickup_period,
        nwsdata.temp_c,
        nwsdata.temp_f,
        nwsdata.temperature_string,
        nwsdata.two_day_history_url,
        nwsdata.visibility_mi,
        nwsdata.weather,
        nwsdata.wind_degrees,
        nwsdata.wind_dir,
        nwsdata.wind_kt,
        nwsdata.wind_mph,
        nwsdata.wind_string,
        nwsdata.windchill_c,
        nwsdata.windchill_f,
        nwsdata.windchill_string,
        nwsdata.wind_gust_kt,
        nwsdata.wind_gust_mph,
        nwsdata.heat_index_c,
        nwsdata.heat_index_f,
        nwsdata.heat_index_string
 FROM weather.nwsdata
 ORDER BY nwsdata.copyright_url,
          nwsdata.credit,
          nwsdata.credit_url,
          nwsdata.dewpoint_c,
          nwsdata.dewpoint_f,
          nwsdata.dewpoint_string,
          nwsdata.disclaimer_url,
          nwsdata.icon_url_base
SEGMENTED BY hash(nwsdata.dewpoint_c, nwsdata.dewpoint_f, nwsdata.latitude, nwsdata.longitude, nwsdata.observation_time_rfc822, nwsdata.pressure_in, nwsdata.pressure_mb, nwsdata.relative_humidity) ALL NODES;


SELECT MARK_DESIGN_KSAFE(0);

(1 row)
