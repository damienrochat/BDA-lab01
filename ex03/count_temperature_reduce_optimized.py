#!/usr/bin/env python
#
# max_temperature_reduce.py - Count temperature from NCDC Global
#                             Hourly Data - Reducer part

import sys

last_key = None
count = 0
# loop through the input, line by line
for line in sys.stdin:
  # each line contains a key and a value separated by a tab character
  (key, val) = line.strip().split("\t")
  # Hadoop has sorted the input by key, so we get the values
  # for the same key immediately one after the other.
  # Test if we just got a new key, in this case output the count
  # temperature for the previous key and reinitialize the variables.
  # If not, keep counting temperature.
  if last_key and last_key != key:
    print "%s\t%s" % (last_key, count)
    count = int(val)
  else:
    count = count+int(val)
  last_key = key

# we've reached the end of the file, output what is left
if last_key:
  print "%s\t%s" % (last_key, count)
