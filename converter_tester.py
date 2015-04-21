# ********************************************************************
# JiaYan Hu
#
# file: converter_tester.py
# Currently been tested on the addresses in Coffee spreadsheet cells 15
# through cell 69.
# *********************************************************************

import coordinates_converter as sc


def main():
    print("Testing coordinates retrieval...")
    sc.retrieve_coordinates("testing.txt", "latitude.txt", "longitude.txt")


main()