import numpy as np
import quaternion


class Cubelet:

  def __init__(self, name, input_index):
    # Every cubelet is associated with an index, and a color-name
    self.index = input_index
    self.name = name

    # Hard-coded initial orientation state for every cubelet
    self.px = np.quaternion(0, 1, 0, 0)
    self.py = np.quaternion(0, 0, 1, 0)
    self.pz = np.quaternion(0, 0, 0, 1)

  # Print name and index
  def id(self):
    print(self.name, self.index)

  # Print current state of orientation
  def state(self):
    print(self.px, self.py, self.pz)

    
# Returns initial cubelets array
def create_cubelets():
  
  names_indexes = dict()
  names = [
    'wbo', 'wb', 'wbr', 'wo', 'wr', 'wgo', 'wg', 'wgr', 'bo', 'br', 'go', 'gr',
    'ybo', 'yb', 'ybr', 'yo', 'yr', 'ygo', 'yg', 'ygr'
  ]
  indexes = [int(x) for x in range(20)]
  cubelets = []

  for i in range(len(names)):
    names_indexes[names[i]] = indexes[i]

  for i in names_indexes:
    c = Cubelet(i, names_indexes[i])
    cubelets.append(c)

  return cubelets


# Returns data relevant to index's changes during rotations of layers
def create_rotations_indexes():

  # Final dictionary
  rotations_indexes = dict()

  # Data
  letters = [
    'u', 'u\'', 'd', 'd\'', 'r', 'r\'', 'f', 'f\'', 'b', 'b\'', 'l', 'l\''
  ]
  current_indexes = [
    [0, 2, 7, 5, 1, 4, 6, 3], [2, 7, 5, 0, 4, 6, 3, 1], [17, 19, 14, 12, 18, 16, 13, 15], [19, 14, 12, 17, 16, 13, 15, 18], [7, 2, 14, 19, 4, 9, 16, 11], [2, 14, 19, 7, 9, 16, 11, 4], [5, 7, 19, 17, 6, 11, 18, 10], [7, 19, 17, 5, 11, 18, 10, 6], [2, 0, 12, 14, 1, 8, 13, 9], [0, 12, 14, 2, 8, 13, 9, 1], [0, 5, 17, 12, 3, 10, 15, 8], [5, 17, 12, 0, 10, 15, 8, 3]
  ]
  next_indexes = [
    [2, 7, 5, 0, 4, 6, 3, 1], [0, 2, 7, 5, 1, 4, 6, 3],[19, 14, 12, 17, 16, 13, 15, 18], [17, 19, 14, 12, 18, 16, 13, 15], [2, 14, 19, 7, 9, 16, 11, 4], [7, 2, 14, 19, 4, 9, 16, 11], [7, 19, 17, 5, 11, 18, 10, 6], [5, 7, 19, 17, 6, 11, 18, 10], [0, 12, 14, 2, 8, 13, 9, 1], [2, 0, 12, 14, 1, 8, 13, 9], [5, 17, 12, 0, 10, 15, 8, 3], [0, 5, 17, 12, 3, 10, 15, 8]
  ]
  
  # For each letter, subarray of currents, and subarray of nexts
  for i in range(len(letters)):

    # Create the dictionary entry of that data
    temp_letter = letters[i]
    temp_current_indexes = current_indexes[i]
    temp_next_indexes = next_indexes[i]
  
    temp_entry = []
    
    # For each element in the sub_arrays
    for j in range(len(temp_current_indexes)):

      # Combine the elements into a single array, and append it to the entry
      temp_current_index = temp_current_indexes[j]
      temp_next_index = temp_next_indexes[j]
      
      temp_entry.append([temp_current_index, temp_next_index])

    # Create dictionary entry with key as letter and value and combined dictionary
    rotations_indexes[temp_letter] = temp_entry
  
  return rotations_indexes


# Returns data relevant to orientation changes during rotation of layers
def create_rotations_quaternions():
  
  # Final Dictionary
  rotations_quaternions = dict()
  
  # Data
  letters = [
    'u', 'd', 'f', 'b', 'r', 'l', 'u\'', 'd\'', 'f\'', 'b\'', 'r\'', 'l\''
  ]
  v = np.sqrt(2)/2
  q_values = [
    np.quaternion(v, 0, 0, -v), np.quaternion(v, 0, 0, v), np.quaternion(v, 0, v, 0), np.quaternion(v, 0, -v, 0), np.quaternion(v, -v, 0, 0), np.quaternion(v, v, 0, 0), np.quaternion(v, 0, 0, v), np.quaternion(v, 0, 0, -v), np.quaternion(v, 0, -v, 0), np.quaternion(v, 0, v, 0), np.quaternion(v, v, 0, 0), np.quaternion(v, -v, 0, 0)
  ]
  
  # For each letter and q_value
  for i in range(len(letters)):
    # Associate that letter with its quaternion, and append to dictionary
  
    temp_letter = letters[i]
    temp_quaternion = q_values[i]
    rotations_quaternions[temp_letter] = temp_quaternion
  
  return rotations_quaternions


def create_rotations_affected():
  
  # Final dictionary
  rotations_affected = dict()
  
  # Data
  letters = [
    ['u', 'u\''], ['d', 'd\''], ['f', 'f\''], ['b', 'b\''], ['r', 'r\''], ['l', 'l\'']
  ]
  affected_indexes = [
    [0, 1, 2, 3, 4, 5, 6, 7], [12, 13, 14, 15, 16, 17, 18, 19], [5, 6, 7, 10, 11, 17, 18, 19], [0, 1, 2, 8, 9, 12, 13, 14], [2, 4, 7, 9, 11, 14, 16, 19], [0, 3, 5, 8, 10, 12, 15, 17]
  ]
  
  # For each letter array and array of affected indexes
  for i in range(len(letters)):
    
    # Associate each letter of the letter array with its affected indexes array, and append to dictionary

    temp_letters = letters[i]
    temp_affected = affected_indexes[i]

    for j in temp_letters:
      rotations_affected[j] = temp_affected
  
  return rotations_affected


# Deprecated
# Returns a rubiks cube rotated by the specified layer
def rotate_rubiks(layer, input_rubiks):
  
  output_rubiks = input_rubiks
  
  indexes = create_rotations_indexes()[layer]
  q = create_rotations_quaternions()[layer]
  affected = create_rotations_affected()[layer]

  # For every cubelet in the rubiks cube
  for c in output_rubiks:

    # If the cubelet is positioned in an affected index
    if c.index in affected:
      
      # Rotate the points of the cubelet
      c.px = q * c.px * q.conjugate()
      c.py = q * c.py * q.conjugate()
      c.pz = q * c.pz * q.conjugate()

      # Change the index of the cubelet 
      # For each pair of indexes (current and next)
      for i in indexes:
        
        # If the current member of the pair matches the index of the cubelet, change index of the cubelet
        if i[0] == c.index:
          c.index = i[1]
          break

  return output_rubiks


# Deprecated
# Prints the state of an input rubiks cube
def print_rubiks(input_rubiks):

  # For each cubelet, print its state
  for c in input_rubiks:
    c.id()
    print("    ", end="")
    c.state()
  
  print("\n\n\n")


class Rubiks:
  
  def __init__(self):
    self.cubelets = create_cubelets()
    self.rot_i = create_rotations_indexes()
    self.rot_q = create_rotations_quaternions()
    self.rot_a = create_rotations_affected()

  def rotate(self, layer):
    output_rubiks = self.cubelets

    indexes = self.rot_i[layer]
    q = self.rot_q[layer]
    affected = self.rot_a[layer]

    # For every cubelet in the rubiks cube
    for c in output_rubiks:
  
      # If the cubelet is positioned in an affected index
      if c.index in affected:
        
        # Rotate the points of the cubelet
        c.px = q * c.px * q.conjugate()
        c.py = q * c.py * q.conjugate()
        c.pz = q * c.pz * q.conjugate()
  
        # Change the index of the cubelet 
        # For each pair of indexes (current and next)
        for i in indexes:
          
          # If the current member of the pair matches the index of the cubelet, change index of the cubelet
          if i[0] == c.index:
            c.index = i[1]
            break

    self.cubelets = output_rubiks

  def current(self):
    for c in self.cubelets:
      c.id()
      print("    ", end="")
      c.state()

