# Dependencies
- [x] NumPy
- [x] Pygame

# TO DO
- [x] Clean up surrounding cells code in sim.py (Thank you @anominos)
- [x] Deal with update() method
- [ ] Clean up \__str__() (and \__repr__())
- [ ] File import (pattern) for sim.py

# AFTER FINISHED
- [ ] Remove default values in Grid constructor (for debugging purposes)
- [ ] Remove gg() function (creates glider in top-left corner)

## Urgent
- [x] Change get_cell method to unpack tuples
- [x] Deal with return list for surrounding cells method

## Ideas

- Use Numpy ndarray for grid state (can use BOOL data type) - True = Alive, False = Dead

numpy.ndarray --> (https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)

## Credits
- Thank you @anominos for surrounding_cells() code