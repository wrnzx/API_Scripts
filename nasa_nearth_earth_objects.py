import requests
import math
from datetime import date, timedelta
# This script will only print 1 object for each day of the week


def get_response():  # Function get and returns JSON response
    # API Data
    api_key = ' '
    starting_date = date.today()

    api_url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + starting_date.strftime(
        '%Y-%m-%d') + '&api_key=' + api_key
    # API Request
    response = requests.get(api_url).json()
    return response  


data = get_response()  # returns API Response in JSON format
start_date = date.today()  # Today's date to pass into path

for each_entry in data['near_earth_objects']:  # Iterate through list of near earth objects

    near_earth_object = data['near_earth_objects'][str(start_date)][0]  # Path to first [0] object on specified day

    # Naming and hazard info
    neo_id = near_earth_object['id']
    neo_name = near_earth_object['name']
    jpl_url = near_earth_object['nasa_jpl_url']

    # Convert hazard bool to yes or no
    if near_earth_object['is_potentially_hazardous_asteroid']:
        potential_hazard = 'Yes'
    else:
        potential_hazard = 'No'

    # Estimated diameter and approach date
    estimated_diameter = round(near_earth_object['estimated_diameter']['feet']['estimated_diameter_max'])
    estimated_approach_date = near_earth_object['close_approach_data'][0]['close_approach_date_full']
    relative_velocity = float(near_earth_object['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])

    # Print out data
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

    start_date = start_date + timedelta(days=1)

