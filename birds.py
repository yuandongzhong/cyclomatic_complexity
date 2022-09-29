class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    if self.extinct:
      return -1 # we do not care about extinct bird speeds
    else:
      if self.flightless:
        if self.name == 'Ostrich':
          return 15
        elif self.name == 'Chicken':
          return 7
        elif self.name == 'Flamingo':
          return 8
        else:
          return -1 # bird name not implemented
      else:
        if self.name == 'Gold Finch':
          return 12
        elif self.name == 'Bluejay':
          return 10
        elif self.name == 'Robin':
          return 14
        elif self.name == 'Hummingbird':
          return 16
        else:
          return -1 # bird not implemented