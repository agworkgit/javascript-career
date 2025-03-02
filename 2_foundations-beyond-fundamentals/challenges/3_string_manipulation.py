miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344

miles_float = float(miles) # number containing decimals
miles_to_km = miles_float * 1.61 # convert to km

print(str(miles_float) + ' miles is equal to ' + str(miles_to_km) + ' km') # print km by coverting nums to strings via str()