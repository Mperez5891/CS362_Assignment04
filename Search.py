# Author:
# Date:
# Purpose: This is the restaurant search functions. Should
# return the restaurant name and rating based on what the 
# user searches for.

# Businesses search = https://api.yelp.com/v3/businesses/search
import requests
import YelpAPI_Key
from YelpAPI_Key import getAPIKey

#print(bisIndex.keys())    

def convertToMeters(radius):
    # yelp max radius is 40000m
    if(int(radius) == 25):
        return 40000
    else: 
        # conversion is 1 miles = 1609.34 m
        return int(radius * 1609.34)
    
# Get the results based on the term 
def getResults(term, radius, location):
    # My API key, define the endpoint, and define the header
    API_KEY = getAPIKey()
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % API_KEY}
    
    # convert radius from miles to m
    radius = convertToMeters(radius)
    
    # Define the parameters
    PARAMETERS = {'term': term,
                  'limit': 50,
                  'radius': radius,
                  'offset': 50,
                  'location': location}
    
    # Make a request to the yelp API
    response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
    
    # Convert the JSON to a Dict
    data = response.json()

    return data

def getResultsLangLong(term, lat, long, location):
        # My API key, define the endpoint, and define the header
    API_KEY = getAPIKey()
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % API_KEY}
    
    # Define the parameters
    PARAMETERS = {'term': term,
                  'limit': 50,
                  'latitude': lat,
                  'longitude': long,
                  'offset': 50,
                  'location': location}
    
    # Make a request to the yelp API
    response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
    
    # Convert the JSON to a Dict
    data = response.json()

    return data

def printResults(results): 
    for resultsIndex in results['businesses']:
        print('===================================================================')
        print('= Name: ',resultsIndex['name'])
#       print(resultsIndex['image_url'])
        print('= URL: ',resultsIndex['url'])
        print('= Rating: ',resultsIndex['rating'])
        
        if 'price' in resultsIndex:
            print('= Price: ',resultsIndex['price'])
        
        # Handle the address
        print('= Address: ',resultsIndex['location']['address1'])
        if resultsIndex['location']['address2'] != '' and resultsIndex['location']['address2'] != 'None':
            print('=',resultsIndex['location']['address2'])
            if resultsIndex['location']['address3'] != '' and resultsIndex['location']['address3'] != 'None':
                print('=',resultsIndex['location']['address3'])
                
        print('= City: ',resultsIndex['location']['city'])
        print('= Zip: ',resultsIndex['location']['zip_code'])
        print('= Country: ',resultsIndex['location']['country'])
        print('= State: ',resultsIndex['location']['state'])
        print('= Phone: ',resultsIndex['phone'])
        print('===================================================================')
        