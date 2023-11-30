import requests
from bs4 import BeautifulSoup

MS_URL = r'https://www.ey.com/en_uk/managed-services'

def scrapeEyManagedServicesWebPage():

  html = getHtml(MS_URL)
  bs = convertToBeautifulSoup(html)

  thought_articles = getThoughtArticles(bs)

def getHtml(url: str) -> str:
  r = requests.get(url)
  html = r.text
  return html

def convertToBeautifulSoup(html: str) -> BeautifulSoup:
  return BeautifulSoup(html)


def getThoughtArticles(bs: BeautifulSoup) -> list:
  
  

  
  
