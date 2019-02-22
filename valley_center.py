import pandas as pd
import numpy as np 

# read in file
valley_center2018 = pd.read_csv('ValleyCenter2018.csv')
valley_center2017 = pd.read_csv('ValleyCenter2017.csv')
valley_center2016 = pd.read_csv('ValleyCenter2016.csv')
valley_center2015 = pd.read_csv('ValleyCenter2015.csv')
valley_center2014 = pd.read_csv('ValleyCenter2014.csv')
valley_center2013 = pd.read_csv('ValleyCenter2013.csv')
valley_center2012 = pd.read_csv('ValleyCenter2012.csv')

# create dataframes

# for 2018
valley_center2018_df = pd.DataFrame(valley_center2018 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2017
valley_center2017_df = pd.DataFrame(valley_center2017 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2016
valley_center2016_df = pd.DataFrame(valley_center2016 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2015
valley_center2015_df = pd.DataFrame(valley_center2015 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2014
valley_center2014_df = pd.DataFrame(valley_center2014 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2013
valley_center2013_df = pd.DataFrame(valley_center2013 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

# for 2012
valley_center2012_df = pd.DataFrame(valley_center2012 , columns = ['ACCIDENT_YEAR' , 'PRIMARY_RD' , 'SECONDARY_RD' , 'DISTANCE' , 'DIRECTION' , 'INTERSECTION' , 'NUMBER_KILLED' , 'NUMBER_INJURED' , 'ALCOHOL_INVOLVED' , 'COUNT_PED_KILLED' , 'COUNT_BICYCLE_KILLED' , 'COUNT_MC_KILLED'])

#print(valley_center2018_df.head())

# display overview of primary road column
primary_road = valley_center2018_df['PRIMARY_RD'].value_counts()
#print(primary_road)

# display overview of secondary raod column
secondary_road = valley_center2018_df['SECONDARY_RD'].value_counts()
#print(secondary_road)

# clean up 2018 primary road category
valley_center2018_df['PRIMARY_RD'] = valley_center2018_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2018 secondary road category
valley_center2018_df['SECONDARY_RD'] = valley_center2018_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2018 = valley_center2018_df.loc[(valley_center2018_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2018_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2018)

# find the total number of crashes in 2018
total_crashes2018 = collision_location2018['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2018' , total_crashes2018)

# find total number of injuries in 2018 crashes
total_injuries2018 = collision_location2018['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2018' , total_injuries2018)

# find total deaths in 2018 crashes
total_deaths2018 = collision_location2018['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2018' , total_deaths2018)

# clean up 2017 primary road category
valley_center2017_df['PRIMARY_RD'] = valley_center2017_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2017 secondary road category
valley_center2017_df['SECONDARY_RD'] = valley_center2017_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2017 = valley_center2017_df.loc[(valley_center2017_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2017_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2017)

# find the total number of crashes in 2017
total_crashes2017 = collision_location2017['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2017' , total_crashes2017)

# find total number of injuries in 2017 crashes
total_injuries2017 = collision_location2017['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2017' , total_injuries2017)

# find total deaths in 2017 crashes
total_deaths2017 = collision_location2017['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2017' , total_deaths2017)

# clean up 2016 primary road category
valley_center2016_df['PRIMARY_RD'] = valley_center2016_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2016 secondary road category
valley_center2016_df['SECONDARY_RD'] = valley_center2016_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2016 = valley_center2016_df.loc[(valley_center2016_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2016_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2016)

# find the total number of crashes in 2016
total_crashes2016 = collision_location2016['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2016' , total_crashes2016)

# find total number of injuries in 2016 crashes
total_injuries2016 = collision_location2016['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2016' , total_injuries2016)

# find total deaths in 2016 crashes
total_deaths2016 = collision_location2016['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2016' , total_deaths2016)


# clean up 2015 primary road category
valley_center2015_df['PRIMARY_RD'] = valley_center2015_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up secondary 2015 road category
valley_center2015_df['SECONDARY_RD'] = valley_center2015_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2015 = valley_center2015_df.loc[(valley_center2015_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2015_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2015)

# find the total number of crashes in 2015
total_crashes2015 = collision_location2015['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2015' , total_crashes2015)

# find total number of injuries in 2015 crashes
total_injuries2015 = collision_location2015['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2015' , total_injuries2015)

# find total deaths in 2015 crashes
total_deaths2015 = collision_location2015['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2015' , total_deaths2015)

# clean up 2014 primary road category
valley_center2014_df['PRIMARY_RD'] = valley_center2014_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2014 secondary road category
valley_center2014_df['SECONDARY_RD'] = valley_center2014_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2014 = valley_center2014_df.loc[(valley_center2014_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2014_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2014)

# find the total number of crashes in 2014
total_crashes2014 = collision_location2014['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2014' , total_crashes2014)

# find total number of injuries in 2014 crashes
total_injuries2014 = collision_location2014['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2014' , total_injuries2014)

# find total deaths in 2014 crashes
total_deaths2014 = collision_location2014['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2014' , total_deaths2014)

# clean up 2013 primary road category
valley_center2013_df['PRIMARY_RD'] = valley_center2013_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2013 secondary road category
valley_center2013_df['SECONDARY_RD'] = valley_center2013_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2013 = valley_center2013_df.loc[(valley_center2013_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2013_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2013)

# find the total number of crashes in 2013
total_crashes2013 = collision_location2013['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2013' , total_crashes2013)

# find total number of injuries in 2013 crashes
total_injuries2013 = collision_location2013['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2013' , total_injuries2013)

# find total deaths in 2013 crashes
total_deaths2013 = collision_location2013['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2013' , total_deaths2013)

# clean up 2012 primary road category
valley_center2012_df['PRIMARY_RD'] = valley_center2012_df['PRIMARY_RD'].replace({'VALLEY CENTER ROAD': 'VALLEY CENTER RD' , 'VALLEY CENTER RD S/B': 'VALLEY CENTER RD' , 'VALLEY CENTER RD N/B': 'VALLEY CENTER RD' , 'VALLEY CENTER ROAD N/B': 'VALLEY CENTER RD'})

# clean up 2012 secondary road category
valley_center2012_df['SECONDARY_RD'] = valley_center2012_df['SECONDARY_RD'].replace({'N LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD RD': 'LAKE WOHLFORD RD' , 'N. LAKE WOHLFORD': 'LAKE WOHLFORD RD' , 'NORTH LAKE WOHLFORD ROAD': 'LAKE WOHLFORD RD' , 'LAKE WOHLFORD RD.': 'LAKE WOHLFORD RD'})

# find only entries for same collision location
collision_location2012 = valley_center2012_df.loc[(valley_center2012_df['PRIMARY_RD'] == 'VALLEY CENTER RD') & (valley_center2012_df['SECONDARY_RD'] == 'LAKE WOHLFORD RD'),:]

print(collision_location2012)

# find the total number of crashes in 2012
total_crashes2012 = collision_location2012['ACCIDENT_YEAR'].count()
print('TOTAL CRASHES IN 2012' , total_crashes2012)

# find total number of injuries in 2012 crashes
total_injuries2012 = collision_location2012['NUMBER_INJURED'].sum()
print('TOTAL INJURIES IN 2012' , total_injuries2012)

# find total deaths in 2012 crashes
total_deaths2012 = collision_location2012['NUMBER_KILLED'].sum()
print('TOTAL DEATHS IN 2012' , total_deaths2012)

print('BREAK')

# total crashes over seven year period
total_crashes = (total_crashes2018 + total_crashes2017 + total_crashes2016 + total_crashes2015 + total_crashes2014 + total_crashes2013 + total_crashes2012)
print('TOTAL CRASHES OVER SEVEN YEARS' , total_crashes)

# total injuries over seven year period
total_injuries = (total_injuries2018 + total_injuries2017 + total_injuries2016 + total_injuries2015 + total_injuries2014 + total_injuries2013 + total_injuries2012)
print('TOTAL INJUIRES OVER SEVEN YEAR PERIOD' , total_injuries)

# total deaths over seven year period
total_deaths = (total_deaths2018 + total_deaths2017 + total_deaths2016 + total_deaths2015 + total_deaths2014 + total_deaths2013 + total_deaths2012)
print('TOTAL DEATHS OVER SEVEN YEAR PERIOD' , total_deaths)