# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    data = datafile.read() #with the datafile open, I would want to print the data

