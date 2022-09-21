import requests
import json

def getMovieTitles(substr):
titles = []  
data = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr))  
print(data)
print(data.content)
response = json.loads(data.content.decode('utf-8'))    
for page in range(0, response["total_pages"]):       
    page_response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, page + 1))    
    page_content = json.loads(page_response.content.decode('utf-8'))
    print ('page_content', page_content, 'type(page_content)', type(page_content))    
    for item in range(0, len(page_content["data"])):           
         titles.append(str(page_content["data"][item]["Title"]))  
titles.sort()  
return titles

print(getMovieTitles("Superman"))


 