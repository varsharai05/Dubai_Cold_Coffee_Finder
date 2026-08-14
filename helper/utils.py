from geopy.distance import geodesic
from datetime import datetime

def calculate_distance(user_location , spot_location):
  dis = round(geodesic(user_location , spot_location).km , 2)
  return dis
current_time = datetime.now().strftime("%H:%M")


def is_open_spot(row):
  open_time = row['opening_time']
  close_time = row['closing_time']
  is_open = open_time <= current_time <= close_time
  if is_open:
    return 'Open'
  else:
    return 'Closed'
  
  
icons = ["🏠" ,"🛒","🚚"]

def get_spot_icon(spot_type):
  if spot_type == 'cafe':
    spot_type = icons[0]
  elif spot_type == 'cart':
    spot_type = icons[1]
  else:
    spot_type = icons[2]
    
  return spot_type

