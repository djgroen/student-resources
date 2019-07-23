import sys
import csv
from datetime import datetime
from datetime import timedelta

def subtract_dates(date1, date2):
  """
  Takes two dates %Y-%m-%d format. Returns date1 - date2, measured in days.
  """
  date_format = "%Y-%m-%d"
  a = datetime.strptime(date1, date_format)
  b = datetime.strptime(date2, date_format)
  delta = a - b
  #print(date1,"-",date2,"=",delta.days)
  return delta.days
