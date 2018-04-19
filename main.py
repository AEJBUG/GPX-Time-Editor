import gpxpy
import datetime
import dateutil.parser
from pandas import DataFrame
from dateutil.relativedelta import relativedelta

userfile='./Night_Ride.gpx'

# Read in GPX file
gpx = gpxpy.parse(open(userfile))
track = gpx.tracks[0]
segment = track.segments[0]

# Read in gpx from file as TEXT
with open(userfile, 'r', encoding='utf8') as f:
    text = f.read()
f.closed

# Get user desired datetime
dateinput = '2016-03-04T23:00:00'
datetimedesired = dateutil.parser.parse(dateinput)

# Find first time stamp in file
startindex = text.find('<time>')
endindex = text.find('</time>')

# Add 6 to find start of datetime
startindex = startindex + 6

# Minus 1 to find end of datetime
endindex = endindex - 1

#Get datetime string based on index and convert
startdate = text[startindex:endindex]
datetimestart = dateutil.parser.parse(startdate)

print(relativedelta(datetimestart, datetimedesired))

#Find difference between start datetime and desired start datetime
timediff = datetimedesired - datetimestart
timediffsecs = timediff.seconds

# Loop through and change time based on user preference
for track_point in segment.points:
    #track_point.adjust_time(datetime.timedelta(seconds=timediffsecs))
    track_point.adjust_time(relativedelta(datetimedesired, datetimestart))

#data = []
#segment_length = segment.length_3d()
#for point_idx, point in enumerate(segment.points):
 #   data.append([point.longitude, point.latitude,
  #               point.elevation, point.time, segment.get_speed(point_idx)])

#columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
#df = DataFrame(data, columns=columns)
#print(df)

print(gpx.to_xml(), file=open("output.gpx", "a"))