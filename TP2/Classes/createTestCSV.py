import numpy as np
import pandas as pd

print "\nCreo el archivo de test\n"

trips = pd.read_csv('trip_test.csv', low_memory=False)


# Para separar por anio , mes y dia
trips['year'] = pd.DatetimeIndex(trips['start_date']).year
trips['month'] = pd.DatetimeIndex(trips['start_date']).month
trips['day'] = pd.DatetimeIndex(trips['start_date']).day

weather = pd.read_csv('weather.csv', low_memory=False)
weather_94107 = weather.loc[weather['zip_code'] == 94107 , :]
weather_94107.date = pd.to_datetime(weather_94107.date, format='%m/%d/%Y')

# Para separar por anio , mes y dia
weather_94107['year'] = pd.DatetimeIndex(weather_94107['date']).year
weather_94107['month'] = pd.DatetimeIndex(weather_94107['date']).month
weather_94107['day'] = pd.DatetimeIndex(weather_94107['date']).day


trips_weather_94107 = pd.merge(trips,weather_94107,how='left',on=['year','month','day'])
trips_col= trips_weather_94107[['id','start_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches']]

#Relleno los NaN con el valor anterior de la columna, suponiendo que no varian tanto
# las velocidades maximas de las rafagas de viento entre un dia y el anterior
df_nuevo = trips_col.fillna(method='pad')

# Remplazo todas las T que hay en la columna
df_nuevo['precipitation_inches'].replace('T', 0 ,inplace=True)

# Paso la columna de object a int
df_nuevo.precipitation_inches= pd.to_numeric(df_nuevo.precipitation_inches, errors='coerce')

df_nuevo.to_csv("testEditado.csv", index=False)

print "\nCreado y guardado como testEditado.csv\n"
