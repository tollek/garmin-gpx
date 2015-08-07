#!/usr/bin/python

import os
from bs4 import BeautifulSoup

GPX_FILE = 'garmin.gpx'
GPX_HEADER_LINES = 30
OUTPUT_DIR = 'garmin_data'

def split_gpx():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    header = open(GPX_FILE, 'r').readlines()[:GPX_HEADER_LINES]
    with open(GPX_FILE, 'r') as gpx_file:
        soup = BeautifulSoup(gpx_file)
        trks = soup.findAll('trk')
        for trk in trks:
            start_time = trk.find('time').string.replace(':', '_')
            print start_time
            outfile = open('{}/{}.gpx'.format(OUTPUT_DIR, start_time), 'w')
            outfile.write(''.join(header))
            outfile.write(str(trk))
            outfile.write('\n</gpx>\n')
            outfile.close()
               

if __name__ == "__main__":
    split_gpx()

