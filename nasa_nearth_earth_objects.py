#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import math
from datetime import date, timedelta
# this script will only return one object for each day (can be changed with a loop to return all object per day)


def get_response():  # function to get and returns JSON response from NASA

    # API data
    api_key = 'fSLlb6bffVRaYwWw80XHerQEm6FzHevc2WMgP3we'  # enter your API Key here. Available from: https://api.nasa.gov/

    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + date.today().strftime(
        '%Y-%m-%d') + '&api_key=' + api_key

    # API request
    response = requests.get(api_url).json()
    return response


def display_data(data):

    add_date = date.today()  # today's date to pass into path

    for neo in data['near_earth_objects']:  # iterate through list of near earth objects

        near_earth_object = data['near_earth_objects'][str(add_date)][0]  # location of first near earth object on specified day

        # naming and hazard info
        neo_id = near_earth_object['id']
        neo_name = near_earth_object['name']
        jpl_url = near_earth_object['nasa_jpl_url']

        # convert hazard bool to yes or no
        if near_earth_object['is_potentially_hazardous_asteroid']:
            potential_hazard = 'Yes'
        else:
            potential_hazard = 'No'

        # estimated diameter and approach date
        estimated_diameter = round(near_earth_object['estimated_diameter']['feet']['estimated_diameter_max'])
        estimated_approach_date = near_earth_object['close_approach_data'][0]['close_approach_date_full']
        relative_velocity = float(near_earth_object['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        add_date = add_date + timedelta(days=1)  # advance date by 1 to print next day in week

        # print out data
        print('')
        print('_____________________________________________________________DATA_BY_NASA_API_____')
        print('')
        print('Object Name:', neo_name)
        print('Object ID:', neo_id)
        print('Potentially hazardous?:', potential_hazard)
        print('Estimated Diameter:', "{:,}".format(estimated_diameter), 'feet')
        print('Estimated Approach Date and Time:', estimated_approach_date)
        print('Relative Velocity is', "{:,}".format(math.floor(relative_velocity)), "Kilometers/Hour")
        print('NASA Jet Propulsion Lab Url:', jpl_url)
        print('__________________________________________________________________________________')


display_data(get_response())  # Print out the data
