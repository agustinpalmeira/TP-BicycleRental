import numpy as np
import pandas as pd

print "\nCreo el archivo de test\n"

trips = pd.read_csv('/home/barbarasanchez/Desktop/TP2-_DATOS/trip_test.csv', low_memory=False)


# Para separar por anio , mes y dia
trips['year'] = pd.DatetimeIndex(trips['start_date']).year
trips['month'] = pd.DatetimeIndex(trips['start_date']).month
trips['day'] = pd.DatetimeIndex(trips['start_date']).day

weather = pd.read_csv('/home/barbarasanchez/Desktop/TP2-_DATOS/weather.csv', low_memory=False)
weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')

# Para separar por anio , mes y dia
weather['year'] = pd.DatetimeIndex(weather['date']).year
weather['month'] = pd.DatetimeIndex(weather['date']).month
weather['day'] = pd.DatetimeIndex(weather['date']).day
weather_94107 = weather.loc[weather['zip_code'] == 94107 , :]

trips_weather_94107 = pd.merge(trips,weather_94107,how='left',on=['year','month','day'])
trips_col= trips_weather_94107[['id','start_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches']]
trips_col.replace(r'\s+', np.nan, regex=True)
trips_col.convert_objects(convert_numeric=True)
trips_col.fillna(0)
trips_col.to_csv("testEditado5.csv", index=False)

print "\nCreado y guardado como testEditado.csv\n"
