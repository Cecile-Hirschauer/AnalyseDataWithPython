train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#Turn up the Temperature
def f_to_c(f_temp):
  """
  Convert temperature in Farenheit to temperature in Celsius
  """
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  """
  Convert temperature in Celsius to temperature in Farenheit
  """
  f_temp = c_temp * (9/5) + 32
  return f_temp 

# Use the Force
def get_force(mass, acceleration):
  """
  Return mass multiplied by acceleration
  """
  return mass * acceleration


def get_energy(mass, c = 3*10**8):
  """
  c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. 
  Return mass multiplied by c squared.
  """
  return mass * c ** 2

# Do the Work
def get_work(mass, acceleration, distance):
  """
  Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance.
  """
  return get_force(mass, acceleration) * distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
print(f100_in_celsius)
print(c0_in_fahrenheit)

train_force = get_force(train_mass, train_acceleration)
print('The GE train supplies {} Newtons of force.'.format(train_force))

bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies {} Joules.'.format(bomb_energy))

train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE train does {} Joules of work over {} meters.'.format(train_work, train_distance))




