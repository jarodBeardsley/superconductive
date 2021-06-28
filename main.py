"""Driver script for the Superconductive technical challenge

author: Jarod Beardsley
version: 06/28/2021
"""
import astropy
import astropy.coordinates
from astropy.time import Time
import requests

def solar_longitude(time):
    """Returns the solar longitude coordinates, given a UTC time"""
    try:
        return astropy.coordinates.get_sun(time)
    except Exception as e:
        print("Something went wrong: " + str(e))


if __name__ == '__main__':
    times = requests.get("http://127.0.0.1:5000/").text.split(",")
    if len(times) < 2:
        t = Time(times[0], format='isot', scale='utc')
        print("solar longitude at " + times[0] + " is: " + str(solar_longitude(t)))
    else:
        print("More than one time detected, please input only one time per call.")
