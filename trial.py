#read the data file
filename = "trial/precip.txt"
with open(filename, 'r') as datafile:
    data = datafile.read()

#DEBUG
print(type(data))
