#!/usr/bin/python
# -*- coding: utf-8 -*-


#The Google Maps provides web services as an interface for requesting Google maps data for use within your applications. These services may only be used in conjunction with a Google map; using data from these services without displaying them on a Google map is prohibited
#Use of the Google Maps APIs web services is subject to specific limits on the amount of requests per 24 hour period. Requests sent in excess of these limits will receive an error message.
#If you exceed the usage limits you will get an OVER_QUERY_LIMIT status code as a response.This means that the web service will stop providing normal responses and switch to returning only status code OVER_QUERY_LIMIT until more usage is allowed again.

import time
import requests
import json
import geocoder


def get_current_location():
    attempts = 0
    success = False
    while success != True and attempts < 20:
        try:
            #Locate and identify website visitors by IP address
            send_url = 'http://freegeoip.net/json'
            response = requests.get(send_url)
            attempts += 1
            # Consider any status other than 2xx an error
            if not response.status_code // 100 == 2:
                print "Error: Unexpected response {}".format(response)   
            json_response = json.loads(response.text)
        except requests.exceptions.RequestException as e:
            # A serious problem happened, like an SSLError or InvalidURL
            print 'A serious problem happened, like an SSLError or InvalidURL'
        else:
            # gets current latitude and longitude 
            latitude = json_response['latitude']
            longitude = json_response['longitude']
            google_geocode = geocoder.google(
                [latitude, longitude], method='reverse')
            status = google_geocode.status
            if status == "OVER_QUERY_LIMIT":
                print 'Googlemaps API - OVER_QUERY_LIMIT-Error was received because your application sent too many requests per second.Retrying again..'
                #sleep for 2secs
                time.sleep(2)
                # retry
                continue
            success = True
            location = "{},{}".format(
                google_geocode.street, google_geocode.city)
            ctx = [latitude, longitude, location]
            return ctx
    if attempts == 20:
        # send an alert as this means that the daily limit has been reached
        print "Daily limit has been reached"


if __name__ == "__main__":
    get_current_location()



#another method to get address from geolocation


# from pygeocoder import Geocoder

# g = Geocoder.reverse_geocode(12.9833,77.5833)
# location = "{},{}".format(g.route,g.city)
# print location