#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Recalculate NOAA statistics for another climates.')
parser.add_argument('-i', '--inputfile',   help='Input File (required).',  required = True, type = argparse.FileType('r'))
parser.add_argument('-o', '--outputfile',  help='Output File (required).', required = True, type = argparse.FileType('w'))
parser.add_argument('-H', '--highaverage', help='Average of High Temperatures in Celsius Degrees. Default = 29.4.', default = 29.4, type = float)
parser.add_argument('-L', '--lowaverage',  help='Average of Low Temperatures in Celsius Degrees. Default = 19.2.',  default = 19.2, type = float)
parser.add_argument('-A', '--average',     help='Overall Mean Temperature in Celsius Degrees. Default = 23.8.', default = 23.8, type = float)
args=parser.parse_args()

with args.inputfile as f:
	InputContent = f.readlines()		#cargar en memoria archivo de entrada y cerrarlo
	f.close()

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

OverHighCount = 0
UnderLowCount = 0
MinOverAverage = 0
MaxUnderAverage = 0

for i in [el[2] for el in data]:		#cantidad de dias con maxima por encima del promedio de maximas
	if i >= args.highaverage:
		OverHighCount += 1

for i in [el[4] for el in data]:		#cantidad de dias con minima por debajo del promedio de minimas
	if i <= args.lowaverage:
		UnderLowCount += 1

for i in [el[2] for el in data]:		#cantidad de dias con maxima por debajo del promedio general
	if i <= args.average:
		MaxUnderAverage += 1

for i in [el[4] for el in data]:		#cantidad de dias con minima por encima del promedio general
	if i >= args.average:
		MinOverAverage += 1

with args.outputfile as g:
	g.writelines(InputContent[0:-6])	#rellenar archivo nuevo con contenido comun ubicado en [0:-6]
	g.write("Max >=" + str(args.highaverage).rjust(7) + ":" + str(OverHighCount).rjust(3)+'\n')	#dias con max por encima de promedio de max
	g.write("Max <=" + str(args.average).rjust(7) + ":" + str(MaxUnderAverage).rjust(3)+'\n')	#dias con max por debajo del promedio general
	g.write("Min >=" + str(args.average).rjust(7) + ":" + str(MinOverAverage).rjust(3)+'\n')	#dias con min por encima del promedio general
	g.write("Min <=" + str(args.lowaverage).rjust(7) + ":" + str(UnderLowCount).rjust(3)+'\n')	#dias con min por debajo de promedio de min
	g.write(InputContent[-2])
	g.write(InputContent[-1])
	g.close()
