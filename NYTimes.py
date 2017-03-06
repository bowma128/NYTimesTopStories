#
# New York Times Top Stories API Example
#  Uses the requests module to get data from the New York Times Top Stories API.
#
#  @Author: Dylan Bowman
#  @Version: 0.1
#

import requests # For accessing the API.
import json # For parsing data.

def createURL(category, api_key):
    # All Top Stories API calls are in the form:
    # https://api.nytimes.com/svc/topstories/v2/<category>.json?api-key=<key>
    # Where <category> is a category from a list and <key> is an API Key
    #    Gotten from the NYT.
    # Takes as input the category to search and the API key, and returns
    #   a URL to make a request to.
    return "https://api.nytimes.com/svc/topstories/v2/"+category+".json?api-key="+api_key

def getRawData(category, api_key):
    ## Gets raw text from the API and returns it.
    ## Create a URL to request from.
    url = createURL(category, api_key)
    ## Use the requests module to get raw data from the API.
    r = requests.get(url)
    ## Check the status codes and return appropriately.
    if r.status_code == 200:
        return r.text
    elif r.status_code == 403:
        print ("The request was bad.")
        return False
    else:
        print ("Something went wrong.")
        return False

def showFullData(category, api_key):
    ## Gets the data, parses it (using the json module), and displays it.
    raw = getRawData(category, api_key)
    print (json.dumps(json.loads(raw),indent=4))

def showTopHeadlines(category, api_key):
    ## Gets headlines from the data and displays them.
    raw = getRawData(category, api_key)
    data = json.loads(raw)
    ## Iterate through the returned results, getting the headline and byline.
    for result in data["results"]:
        headline = result["title"]
        byline = result["byline"]
        print("\""+headline+"\", "+byline)

def showSingleTopHeadline(category, api_key):
    ## Gets headlines from the data and displays them.
    raw = getRawData(category, api_key)
    data = json.loads(raw)
    headline = data["results"][0]["title"]
    return headline

if __name__ == "__main__":
    api_key = "43e76232993f48ac848db26717a2b90d"
    ## Show the user the categories and ask which one to pick.
    categories = ['home', 'opinion', 'world', 'national', 'politics', 'upshot', 'nyregion', 'business', 'technology',
                  'science', 'health', 'sports', 'arts', 'books', 'movies', 'theater', 'sundayreview', 'fashion',
                  'tmagazine', 'food', 'travel', 'magazine', 'realestate', 'automobiles', 'obituaries', 'insider']
    print("Categories: "+", ".join(categories))
    category = str(input("Please input a category to test.")).lower()
    while category not in categories:
        print("I didn't understand that.")
        category = str(input("Please input a category to test.")).lower()

    print("\n\n")
    print("Example 1: "+category+" full data")
    input("Press enter to continue.")
    showFullData(category, api_key)

    print("\n\n")
    print("Example 2: "+category+" headlines and authors")
    input("Press enter to continue.")
    showTopHeadlines(category, api_key)

    print("\n\n")
    print("Example 3: Top headlines in multiple categories")
    print("Categories: "+", ".join(categories))
    categoryList = input("Please input a set of categories, separated by a space.").split(" ")
    for c in categoryList:
        if c not in categories:
            print (c+" is not a valid category.")
        else:
            print (c+": "+showSingleTopHeadline(c,api_key))
