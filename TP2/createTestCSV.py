import numpy as np
import pandas as pd

print "\nCreo el archivo de test\n"

trips = pd.read_csv('/Users/agustinpalmeira/Documents/Agus Varios/Facu/datos/tp2017/trip_test.csv', low_memory=False)


# Para separar por anio , mes y dia
trips['year'] = pd.DatetimeIndex(trips['start_date']).year
trips['month'] = pd.DatetimeIndex(trips['start_date']).month
trips['day'] = pd.DatetimeIndex(trips['start_date']).day

weather = pd.read_csv('/Users/agustinpalmeira/Documents/Agus Varios/facu/datos/TP2017/weather.csv', low_memory=False)
weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')

# Para separar por anio , mes y dia
weather['year'] = pd.DatetimeIndex(weather['date']).year
weather['month'] = pd.DatetimeIndex(weather['date']).month
weather['day'] = pd.DatetimeIndex(weather['date']).day
weather_94107 = weather.loc[weather['zip_code'] == 94107 , :]

trips_weather_94107 = pd.merge(trips,weather_94107,how='left',on=['year','month','day'])
trips_col= trips_weather_94107[['start_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph']]
trips_col.dropna(inplace=True) ##para eliminar los nulos y nan
trips_col.to_csv("testEditado.csv", index=False)

print "\nCreado y guardado como trainEditado.csv\n"