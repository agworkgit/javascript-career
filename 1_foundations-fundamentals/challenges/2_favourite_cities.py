inputCity = input('What is my favourite city? ')

def favouriteCity(city):
    if (city == 'Santa Barbara'): # I know this is a bit silly, it will improve as I go
        print('You guessed it! My favoutite city is: ', city)
    else:
        print('You said ', city, ' that is not it.')

favouriteCity(inputCity)

# Edge cases:
# What if the city is in all lowercase letters?