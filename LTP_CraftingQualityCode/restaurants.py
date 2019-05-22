"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'C:\\Users\\Cuyler\\projects\\LTP_CraftingQualityCode\\restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    rating_list = []

    for restaurant in names_final:
        rating_list.append([name_to_rating[restaurant], restaurant])

    rating_list.sort()
    rating_list.reverse()

    return rating_list

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    Return a list of the restaurants in names_matching_price that serve at
    least one of the cuisines in cuisines_list according to cuisine_to_names.
    
    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

    # Initialize accumulator list
    matching_restaurants = []
    
    # Loop through each restaurant in names_matching price and then
    # each cuisine in cuisines_list.
    for restaurant in names_matching_price:
        for cuisine in cuisines_list:

    # If restaurant in cuisine_to_names[cuisine], add to accumulator list,
    # if it is not already there.
            if restaurant in cuisine_to_names[cuisine]:
                if restaurant not in matching_restaurants:
                    matching_restaurants.append(restaurant)
                    
    return matching_restaurants

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    # A list to accumulate the contents of the current restauarant being read
    # from the file.
    current_restaurant = []
    
    # Get the first line of the file
    current_line = file.readline()

    # Read each line of the file until the end of the file is reached.
    while current_line != '':

        # If the current line is not blank ('\n'), append the line to
        # current_restaurant.
        if not (current_line == '\n' or current_line == ''):
            current_restaurant.append(current_line.strip())
            current_line = file.readline()

            # If the next line is empty or the end of the file, add the relevant
            # data to each dictionary and clear current_restaurant.
            if current_line == '\n' or current_line == '':

                # Build name_to_rating
                name_to_rating[current_restaurant[0]] = current_restaurant[1]
                
                # Build price_to_names
                price_to_names[current_restaurant[2]].append(current_restaurant[0])
                
                # Build cuisine_to_names
                for cuis in separate_cuisines(current_restaurant[3]):
                    if cuis in cuisine_to_names:
                        cuisine_to_names[cuis].append(current_restaurant[0])
                    else:
                        cuisine_to_names[cuis] = [current_restaurant[0]]
                    
                current_restaurant.clear()
                current_line = file.readline()

    return name_to_rating, price_to_names, cuisine_to_names
        
def separate_cuisines(cuisines):
    """ (str) -> list of str

    Returns a list of cuisines from a comma-separated list of cuisines.

    >>> separate_cuisines('Chinese,Thai,Japanese')
    [['Chinese'], ['Thai'], ['Japanese']}
    >>> separate_cuisines('Canadian,Pub Food')
    [['Canadian'], ['Pub Food']]
    """
    
    return cuisines.split(",")
