import numpy as np
import pandas as pd

print "\nCreo el archivo de train\n"

trips = pd.read_csv('trip_train.csv', low_memory=False)
trips_menos_1 = trips.loc[trips.duration < 86400,:]

# Para separar por anio , mes y dia
trips_menos_1['year'] = pd.DatetimeIndex(trips_menos_1['start_date']).year
trips_menos_1['month'] = pd.DatetimeIndex(trips_menos_1['start_date']).month
trips_menos_1['day'] = pd.DatetimeIndex(trips_menos_1['start_date']).day

weather = pd.read_csv('weather.csv', low_memory=False)
weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')

# Para separar por anio , mes y dia
weather['year'] = pd.DatetimeIndex(weather['date']).year
weather['month'] = pd.DatetimeIndex(weather['date']).month
weather['day'] = pd.DatetimeIndex(weather['date']).day
weather_94107 = weather.loc[weather['zip_code'] == 94107 , :]

trips_weather_94107 = pd.merge(trips_menos_1,weather_94107,how='left',on=['year','month','day'])
trips_col= trips_weather_94107[['duration','start_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches']]
#trips_col.dropna(inplace=True) ##para eliminar los nulos y nan
trips_col.replace(r'\s+', np.nan, regex=True)
trips_col.convert_objects(convert_numeric=True)
trips_col.fillna(0)
trips_col.to_csv("trainEditado5.csv", index=False)

print "\nCreado y guardado como trainEditado5.csv\n"

