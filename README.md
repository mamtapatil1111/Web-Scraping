# Web-Scraping
Data extraction from website

Web Scraping is a technique used to extract data from the websites. 

# Objective
In the Rate My Professor website every professor will have his/her respected tags such as (hilarious, heavy homework, study hard or fail, etc.), we will just try to extra these tags.

# Steps for web scraping in this project:
1. Importing the required libraries.
2. Getting the URL and storing it in a variable.
3. Making a request to the website using the requests library.
4. Using the Beautiful Soup library to get the HTML (raw) data from the website.
5. Using soup.findAll method to get the respected tag that we are looking for.
6. Removing all the HTML tags and converting it to a plain text format.
   
