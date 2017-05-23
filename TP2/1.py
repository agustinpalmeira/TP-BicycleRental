import pandas as pd
import numpy as np
#trips = pd.read_csv('trip_train.csv', low_memory=False)
#trips_menos_1 = trips.loc[trips.duration < 86400,:]
# Para separar por anio , mes y dia
#trips_menos_1['year'] = pd.DatetimeIndex(trips_menos_1['start_date']).year
#trips_menos_1['month'] = pd.DatetimeIndex(trips_menos_1['start_date']).month
#trips_menos_1['day'] = pd.DatetimeIndex(trips_menos_1['start_date']).day
#chunks2=pd.read_csv('weather.csv',sep=',',iterator=True,chunksize=3000)
#weather = pd.concat([chunk for chunk in chunks2])
#weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')
# Para separar por anio , mes y dia
#weather['year'] = pd.DatetimeIndex(weather['date']).year
#weather['month'] = pd.DatetimeIndex(weather['date']).month
#weather['day'] = pd.DatetimeIndex(weather['date']).day
#weather_94107 = weather.loc[weather['zip_code'] == 94107 , :]
#trips_weather_94107 = pd.merge(trips_menos_1,weather_94107,how='left',on=['year','month','day'])
#trips_weather_94107.to_csv("joineado.csv", index=False)



chunks=pd.read_csv('joineado.csv',sep=',',iterator=True,chunksize=3000)
joineado = pd.concat([chunk for chunk in chunks])

keep_col= ['duration','mean_temperature_f']
new_f = joineado[keep_col]
new_f.to_csv("trainEditado.csv", index=False)
