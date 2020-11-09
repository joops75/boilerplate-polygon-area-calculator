import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return math.sqrt(self.width ** 2 + self.height ** 2)

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."

    else:
      picture = ""
      for i in range(0, self.height):
        picture += "*" * self.width + "\n"

      return picture

  def get_amount_inside(self, shape):
    can_fit_widths = math.floor(self.width / shape.width)
    can_fit_heights = math.floor(self.height / shape.height)

    return can_fit_widths * can_fit_heights

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return "Square(side={})".format(self.width)
