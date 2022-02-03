from readdata import read_data
from printing import print_comparison
from computation import compute_windchill

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill' : 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed' :float, 'windchill' :float}
#types= {'date': float}


#Read data from file
data = read_data(columns, types=types)

# compute the wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v ** 0.16

    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci 

#Running the function to compute windchill index WCI
windchill =[]
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

#DEBUG
#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f}{wc_comp:.5f} {wc_data - wc_comp:.5f}')


#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i, j)

#Output comparison data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)
