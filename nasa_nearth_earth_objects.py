#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import math
from datetime import date


# this script will only return one object for each day (can be changed with a loop to return all object per day)


def get_response():  # function to get and returns JSON response from NASA
    api_url = 'https://api.nasa.gov/neo/rest/v1/feed'
    parameters = {
        "start_date": str(date.today().strftime('%Y-%m-%d')),
        "api_key": ''
    }
    response = requests.get(api_url, params=parameters).json()
    return response


def prepare_for_display(data):
    result_list = []
    for neo in data['near_earth_objects']:  # iterate through list of near earth objects.
        near_earth_object = data['near_earth_objects'][neo][0]
        neo_id = near_earth_object['id']  # naming and hazard info
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
        relative_velocity = float(
            near_earth_object['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])

        header = '_____________________________________________________________DATA_BY_NASA_API_____'
        footer = '__________________________________________________________________________________'
        object_name = 'Object Name: ' + neo_name
        object_id = 'Object ID: ' + neo_id
        pot_haz = 'Potentially hazardous?: ' + potential_hazard
        est_diam = 'Estimated Diameter: ' + str("{:,}".format(estimated_diameter)) + 'feet'
        est_app = 'Estimated Approach Date and Time: ' + estimated_approach_date
        rel_vel = 'Relative Velocity is ' + str("{:,}".format(math.floor(relative_velocity))) + "Kilometers/Hour"
        jpl_url = 'NASA Jet Propulsion Lab Url: ' + jpl_url

        visualized = header + "\n" + \
                     " " + "\n" + \
                     object_name + "\n" + \
                     object_id + "\n" + \
                     pot_haz + "\n" + \
                     est_diam + "\n" + \
                     est_app + "\n" + \
                     rel_vel + "\n" + \
                     jpl_url + "\n"

        result_list.append(visualized)
    return result_list


neo_list = prepare_for_display(get_response())
for n in neo_list:
    print(n)
