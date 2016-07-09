#!/usr/bin/python

import os
from bs4 import BeautifulSoup

GPX_FILE = 'garmin.gpx'
OUTPUT_DIR = 'garmin_data'

def split_gpx():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
  
    # Find .gpx header - all lines until the first 'trk'
    header = open(GPX_FILE, 'r').readlines()
    for idx, header_line in enumerate(header):
        if 'trk' in header_line:
            header = header[:idx]
            break            

    # Build single .gpx file for every 'trk' section.
    with open(GPX_FILE, 'r') as gpx_file:
        soup = BeautifulSoup(gpx_file, 'lxml')
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

