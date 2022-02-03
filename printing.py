
def print_comparison(name, dates, times, original_data, computed_data):
    """
	Print a comparison of two time series (Original and Computed)
	Parameters:
	    name: A string name for the data being compared (limited to 9 characters in length)
		dates: List of strings representing dates for each data.
		times: List of string representing time for each data
		original_data: List of original data (floats)
		comouted_data: List of computed data (floats)
	"""
    #Output comparison of data
    print('                ORIGINAL  COMPUTED')
    print(f' DATE   TIME  {name.upper():>9} {name.upper():>9}WINDCHILL WINDCHILL DIFFERENCE') 
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6}  {orig:9.6f}  {comp:9.6f} {diff:10.6f}')