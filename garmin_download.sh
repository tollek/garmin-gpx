#!/bin/bash

mv garmin.gpx garmin.gpx.backup
gpsbabel -w -r -t -i garmin,snwhite=0,get_posn=0,power_off=0,erase_t=0,resettime=0 -f usb: -o gpx,suppresswhite=0,logpoint=0,humminbirdextensions=0,garminextensions=0 -F garmin.gpx
mkdir garmin_data

