import numpy as np
import pandas as pd
import gpxpy.geo

print "\nCreo el archivo de test\n"

trips = pd.read_csv('trip_test.csv', low_memory=False)

stations = pd.read_csv('station.csv', low_memory=False)
stations['start_station_id']=stations['id']
del stations['id']


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
trips_col= trips_weather_94107[['id','start_station_id','end_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches']]

#############voy s buscar las 2 latitudes y longitudes################33
trips2=pd.merge(trips_col,stations,how='left',on=['start_station_id'])
trips3=trips2[['id','start_station_id','end_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches','lat','long']]
trips3['lat1']=trips3['lat']
trips3['long1']=trips3['long']
del trips3['lat']
del trips3['long']

stations['end_station_id']=stations['start_station_id']
del stations['start_station_id']
trips4=pd.merge(trips3,stations,how='left',on=['end_station_id'])
trips5=trips4[['id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches','lat1','long1','lat','long']]

trips5['lat2']=trips5['lat']
trips5['long2']=trips5['long']
del trips5['lat']
del trips5['long']
###########calculo la distancia de haversine#########################

print "\ncalculando distancias\n"
trips5['distancia'] = trips5.apply(lambda row: gpxpy.geo.haversine_distance(row['lat1'], row['long1'], row['lat2'], row['long2']), axis=1)

###################################################################

#Relleno los NaN con el valor anterior de la columna, suponiendo que no varian tanto
# las velocidades maximas de las rafagas de viento entre un dia y el anterior
df_nuevo = trips5.fillna(method='pad')

# Remplazo todas las T que hay en la columna
df_nuevo['precipitation_inches'].replace('T', 0 ,inplace=True)

# Paso la columna de object a int
df_nuevo.precipitation_inches= pd.to_numeric(df_nuevo.precipitation_inches, errors='coerce')
del df_nuevo['lat1']
del df_nuevo['lat2']
del df_nuevo['long1']
del df_nuevo['long2']

df_nuevo.to_csv("testEditado7.csv", index=False)

print "\nCreado y guardado como testEditado7.csv\n"
