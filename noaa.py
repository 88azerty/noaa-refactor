#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Recalculate NOAA statistics for another climates.')
parser.add_argument('-i', '--inputfile', help='Input File (required).', required=True, type=argparse.FileType('r'))
parser.add_argument('-o', '--outputfile', help='Output File (required).', required=True, type=argparse.FileType('w'))
parser.add_argument('-H','--highaverage', help='Average of High Temperatures in Celsius Degrees. Default = 36.0.', default=36.0, type=float)
parser.add_argument('-L','--lowaverage', help='Average of Low Temperatures in Celsius Degrees. Default = 11.0.', default=11.0, type=float)
args=parser.parse_args()

with args.inputfile as f:
	InputContent = f.readlines()		#cargar en memoria archivo de entrada y cerrarlo
	f.close()

with args.outputfile as g:
	g.writelines(InputContent[0:-6])	#rellenar archivo nuevo con contenido comun ubicado en [0:-6]

data = []

for i in InputContent[13:-9]:			#crear data array conociendo tipos de datos. datos estan en [13:-9]
	data.append([	int(i.split()[0]),	#DAY
			float(i.split()[1]),	#MEAN TEMP
			float(i.split()[2]),	#HIGH
			str(i.split()[3]),	#TIME
			float(i.split()[4]),	#LOW
			str(i.split()[5]),	#TIME
			float(i.split()[6]),	#HEAT DEG DAYS
			float(i.split()[7]),	#COOL DEG DAYS
			float(i.split()[8]),	#RAIN
			float(i.split()[9]),	#AVG WIND SPEED
			float(i.split()[10]),	#HIGH
			str(i.split()[11]),	#TIME
			str(i.split()[12])	#DOM DIR
		   ])

#print([el[2] for el in data])

OverHighCount = 0
UnderLowCount = 0

for i in [el[2] for el in data]:		#cantidad de dias con maxima por encima del promedio de maximas
	if i > args.highaverage:
		OverHighCount += 1

for i in [el[4] for el in data]:
	if i < args.lowaverage:
		UnderLowCount += 1

print(OverHighCount,UnderLowCount)
