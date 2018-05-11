#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json

# imported functions from file
from capture_image_find_faces import capture_image_find_faces
from get_location import get_current_location
from send_twilio_sms import send_sms

#created a json file with all location details like name,longitude,latitude etc
#first location in json file is taken as starting location
#last location in json file is taken as ending location

def main():
	#loading json files using json module
	data = json.load(open('initial_data.json'))
	#initialized starting location from initial.json file
	starting_location_longitude = data[0].get('longitude')
	#get location id from initial.json
	location_id = data[0].get('pk')
	#initializing ending location from initial.json
	ending_location_longitude = data[-1].get('longitude')
	#initialized total passenger
	total_passenger = 60
	while True:
		geo_data = get_current_location()
		#initializing geo_data from get_data list
		latitide = geo_data[0]
		longitude = geo_data[1]
		location = geo_data[2]
		#checks if longitude of starting location is equalto current longitude and location_id
		if float(starting_location_longitude) == float(longitude) and location_id == 0 :
			faces_found = capture_image_find_faces()
			vacant_seat = total_passenger - int(faces_found)
			print 'Bus is at the starting station'
			send_sms(location,vacant_seat)
			total_passenger = int(faces_found)
			time.sleep(10)
			location_id += 1
		elif location_id != 0 and location_id < 7:
			if float(starting_location_longitude) == float(longitude):#checks if bus is moving or not.if it returns true ,it will find next location from initial_data.json file
				print "Bus is at the same location or Bus is not moving"
				time.sleep(10)
				print "Getting next location manually from the database"
				#find next location from initial_data.json
				location_name = data[location_id].get('location')
				faces_found = capture_image_find_faces()
				vacant_seat = total_passenger - int(faces_found)
				send_sms(location_name,vacant_seat)
				time.sleep(10)
				total_passenger = int(faces_found)
				location_id += 1#incrementing location id by one
			elif data[location_id].get('longitude') == float(longitude):#checks if longitude is equalto current longitude
				location_name = data[location_id].get('location')
				print location_name
				faces_found = capture_image_find_faces()
				vacant_seat = total_passenger - int(faces_found)
				send_sms(location_name,vacant_seat)
				time.sleep(10)
				total_passenger = int(faces_found) 
				location_id += 1
			else:
			    return None		
		elif float(ending_location_longitude) == float(longitude) or location_id == 7:#statement to find endlocation reached or not 
			location_name = data[-1].get('location')
			print location_name
			faces_found = capture_image_find_faces()
			vacant_seat = total_passenger - int(faces_found)
			total_passenger = int(faces_found)
			send_sms(location_name,vacant_seat)
			print "Bus reached at end station"
			break 
		else:
		   break   
	return None   



if __name__ == "__main__":
   main()
