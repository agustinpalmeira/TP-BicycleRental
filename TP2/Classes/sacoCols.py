import numpy as np
import pandas as pd

trips = pd.read_csv('testEditado7.csv', low_memory=False)
del trips['lat1']
del trips['long1']
del trips['lat2']
del trips['long2']

trips.to_csv("testEditadoConDistancia.csv", index=False)

print "\nCreado y guardado como trainEditadoConDistancia.csv\n"

