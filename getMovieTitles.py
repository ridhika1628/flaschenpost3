# import requests and json module
import requests
import json


def getMovieTitles(substr):
    titles = []
    # Making a GET request
    data = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title= {}".format(substr))
    # check status code for response received
    # success code - 200
    #print(data)
    # Json content
    response = json.loads(data.content.decode('utf-8'))
    total_page = response["total_pages"]
    # print content of request
    #print(data.content)
    for page in range(0, response["total_pages"]):
        page_response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, page + 1))
        page_content = json.loads(page_response.content.decode('utf-8'))
        #print ('page_content', page_content, 'type(page_content)', type(page_content))
        for item in range(0, len(page_content["data"])):
            titles.append(str(page_content["data"][item]["Title"]))
    titles.sort()
    # Return statement to send the titles result back after sorting the Titles
    return titles
print(getMovieTitles("Superman"))
