# ymdhms_to_jd.py

# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converting from ecef to sez origin positions

# Parameters:
#  year : int
#   year
#  month : int
#   month
#  day : int
#   day
#  hour : int
#   hour
#  minute : int
#   minute
#  second : float
#   second

# Output:
#  julian_date : float
#   s position of 3D position vector

# Written by Riley Parsons

import sys

# "constants"

# helper functions  

# main function
def ymdhms_tojd(y : int, m : int, d: int, hr: int, min: int, sec: float):

  jd = d - 32075 \
      + int(1461 * (y + 4800 + int((m - 14)/12))/4) \
      + int(367 * (m - 2 - int((m-14)/12) * 12)/12) \
      - int(3 * int(((y + 4900 + int((m-14)/12))/100))/4)
  
  jd_midnight = jd - 0.5
  d_frac = (sec + 60 * (min + 60 * hr ))/86400
  jd_frac = jd_midnight + d_frac

  print(jd_frac)
  return (jd_frac)

# initialize script arguments
year = None
month = None
day = None
hour = None
min = None
sec = None

# parse script arguments
if len(sys.argv)==7:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  min = int(sys.argv[5])
  sec = float(sys.argv[6])
else:
  print('Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  ymdhms_tojd(year, month, day, hour, min, sec)
else:
  ymdhms_tojd(year, month, day, hour, min, sec)