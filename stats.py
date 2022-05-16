import requests
from bs4 import BeautifulSoup

def getstats():
 
   
  # URL for scrapping data
  url = 'https://www.fite.tv/fighter/saul-alvarez-canelo/1748/'
   
  # get URL html
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
   
  data = []
   
  # soup.find_all('td') will scrape every
  # element in the url's table
  data_iterator = iter(soup.find_all('td'))
   
  # data_iterator is the iterator of the table
  # This loop will keep repeating till there is
  # data available in the iterator
  while True:
      try:
          result = next(data_iterator).text
          opponent = next(data_iterator).text
          method = next(data_iterator).text
          r_t = next(data_iterator).text
          event = next(data_iterator).text
   
          # append to data list
          data.append((
              result,
              opponent,
              method,
              r_t,
              event
          ))
   
      # StopIteration error is raised when
      # there are no more elements left to
      # iterate through
      except StopIteration:
          break
  
  # create texttable object
  import texttable as tt
  table = tt.Texttable()
   
  # Add an empty row at the beginning for the headers
  table.add_rows(data)
  
  
    
  return table
  
  #print(table.draw())
  
  