import numpy as np
import pandas as pd
import gpxpy.geo

print "\nCreo el archivo de train\n"

trips = pd.read_csv('trip_train.csv', low_memory=False)
stations = pd.read_csv('station.csv', low_memory=False)
stations['start_station_id']=stations['id']
del stations['id']
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
trips_col= trips_weather_94107[['duration','start_station_id','end_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches']]
#############voy s buscar las 2 latitudes y longitudes################33
trips2=pd.merge(trips_col,stations,how='left',on=['start_station_id'])
trips3=trips2[['duration','start_station_id','end_station_id','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches','lat','long']]
trips3['lat1']=trips3['lat']
trips3['long1']=trips3['long']
del trips3['lat']
del trips3['long']

stations['end_station_id']=stations['start_station_id']
del stations['start_station_id']
trips4=pd.merge(trips3,stations,how='left',on=['end_station_id'])
trips5=trips4[['duration','mean_temperature_f','mean_wind_speed_mph','max_gust_speed_mph','precipitation_inches','lat1','long1','lat','long']]

trips5['lat2']=trips5['lat']
trips5['long2']=trips5['long']
del trips5['lat']
del trips5['long']
###########calculo la distancia de haversine#########################
print "\ncalculando distancias\n"
trips5['distancia'] = trips5.apply(lambda row: gpxpy.geo.haversine_distance(row['lat1'], row['long1'], row['lat2'], row['long2']), axis=1)

###################################################################



#trips_col.dropna(inplace=True) ##para eliminar los nulos y nan
trips5.replace(r'\s+', np.nan, regex=True)
trips5.convert_objects(convert_numeric=True)
trips5.fillna(0)
trips5.to_csv("trainEditado6.csv", index=False)

print "\nCreado y guardado como trainEditado6.csv\n"

