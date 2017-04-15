#!/usr/bin/env python
import csv

def replace_hyphens (string):
	"""Funcion auxiliar para reemplazar guiones por barras en aquellas
	fechas que lo ameriten"""
	if "-" in string:
		return string.replace("-","/")
	return string


def main():
	counter = 0
	with open("status.csv", "r") as f:

		status = csv.reader(f)

		with open("status_red.csv", "w") as d:

			status_red = csv.writer(d)
			status_red.writerow(["station_id", "bikes_available", \
			"docks_available", "start_time", "end_time"])

			station_id_previous = ""
			bikes_available_previous = ""
			docks_available_previous = ""
			start_time_previous = ""
			end_time_previous = ""

			primer_registro = True
			status.next()

			for station_id, bikes_available, docks_available, time in \
			status:

				#counter = counter + 1

				if primer_registro == True:

					station_id_previous = station_id
					bikes_available_previous = bikes_available
					docks_available_previous = docks_available
					start_time_previous = replace_hyphens(time)
					end_time_previous = replace_hyphens(time)
					primer_registro = False

				else:

					if (station_id_previous == station_id and \
					bikes_available_previous == bikes_available and \
					docks_available_previous == docks_available):
						end_time_previous = replace_hyphens(time)

					else:
						status_red.writerow([station_id_previous, \
						bikes_available_previous, \
						docks_available_previous, start_time_previous, \
						end_time_previous])
						station_id_previous = station_id
						bikes_available_previous = bikes_available
						docks_available_previous = docks_available
						start_time_previous = replace_hyphens(time)
						end_time_previous = replace_hyphens(time)

				#if counter == 70:
					#break

			status_red.writerow([station_id_previous, \
			bikes_available_previous, docks_available_previous, \
			start_time_previous, end_time_previous])
					
	#print counter


main()
