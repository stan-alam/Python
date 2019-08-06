import math

class Point:
  "represents a point in 2 - dim geometric      coordinates"

  def __init__(self, x=0, y=0):
    """init the position of point. the x and y coordinates can be specified. if they are not, point defaults to the origin"""
    self.move(x, y)

  def move(self, x, y):
    "move the point to a new location in 2D space"
    self.x = x
    self.y = y

  def reset(self):
    "reset the point back to the geometric origins of 0, 0"
    self.move(0, 0)

  def calculate_distance(self, other_point):
    """calculate the distance from this point to 2nd point pass as a param."""
    return math.sqrt(
     (self.x - other_point.x) ** 2
     + (self.y - other_piont.y) ** 2
    )
