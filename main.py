"""Driver script for the Superconductive technical challenge
author: Jarod Beardsley
version: 06/28/2021
"""
import astropy.coordinates as ap
from astropy.time import Time
import requests


def solar_longitude(time):
    """Returns the solar longitude coordinates, given a UTC time in ISO format"""
    return ap.get_sun(time).to_string().split(" ")[0]


if __name__ == '__main__':
    try:
        times = requests.get("http://127.0.0.1:5000/").text.split(",")
        if len(times) < 2:
            t = Time(times[0], format='iso', scale='utc')
            print("Solar longitude at " + str(t) + " is: " + solar_longitude(t) + " degrees.")
        else:
            print("More than one time detected, please provide only one time per call.")
    except Exception as e:
        print("Something went wrong: " + str(e))
