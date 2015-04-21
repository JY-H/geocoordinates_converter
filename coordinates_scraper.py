# ********************************************************************
# JiaYan Hu
#
# file: coordinates_scraper.py
# *********************************************************************

from pygeocoder import Geocoder
import time

def retrieve_coordinates(infile, latitude_outfile_name, longitude_outfile_name):
    """
    Retrieves coordinates using pygeocoder and writes the latitude and longitude
    to separate files
    :param infile: infile name
    :param latitude_outfile_name: latitude outfile name
    :param longitude_outfile_name: longitude outfile name
    :return:
    """

    # Reading file
    file = open(infile, "r")
    addresses = []
    for line in file:
        addresses.append(line.strip() + ", NY")
    del addresses[-1]
    print(addresses)

    # Retrieve coordinates and write to file
    lat_outfile = open(latitude_outfile_name, "w")
    long_outfile = open(longitude_outfile_name, "w")
    for i in range(len(addresses)):
        # Time delay to avoid violating query limit (at 10/sec)
        if (i % 10 == 0 and i != 0):
            time.sleep(2)
        results = Geocoder.geocode(addresses[i])

        # Formatting coordinates into separate files to make copying
        # into excel easier
        coordinates = str(results[0].coordinates).split(",")
        coordinates[0] = coordinates[0].lstrip("(")
        coordinates[1] = coordinates[1].rstrip(")")

        # Write to files
        lat_outfile.write(coordinates[0] + "\n")
        long_outfile.write(coordinates[1] + "\n")

    # close files
    file.close()
    lat_outfile.close()
    long_outfile.close()

