# GetMovieTitles
Get HTTP Request to retrieve movie titles. Have written an HTTP GET method to retrieve information from a films database.

Function Description
Given a string substr, getMovieTitles() must perform the following tasks:
1.	Query https://jsonmock.hackerrank.com/api/movies/search/?Title=substr
2.	Initialize the titles array to store total string elements. Store the Title of each movie meeting the search criterion in the titles array
3.	Sort titles in ascending order and return it as your answer.

The query response from the website is JSON response with the following fields:
-	page: The current page
-	per_page: The maximum number of results per page. 
-	total: The total number of movies in the search result
-	total_pages: The total number of pages which must be queried to get all the results.
-	Data: An array of JSON objects containing movie information where the Title field denotes the title of the movie.

## Refer to word document answer sheet for Output screenshot.
