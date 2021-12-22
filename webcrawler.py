from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#Package to read config file
import configparser
import pandas as pd

class WebCrawler:

	def read_ini(self,file_path):
	    config = configparser.ConfigParser()
	    config.read(file_path)
	    return config

	

	def get_title(self,my_url):

			#Requesting URL and getting response
			uClient = uReq(my_url)
			#getting response and reading data
			page_html = uClient.read()
			#Closing URL Client Connection
			uClient.close()
			#Parsing using HTML parser and beautiful soap
			page_soup = soup(page_html, "html.parser")

			return page_soup

	def find_title(self,page_soup):

		#Finding all title
		title=page_soup.findAll("title")

		#Creating a list of all titles found on the page
		list_title=[]

		#iterating through the list and eliminating the first 12 character to remove "Top Story -" and get final top stories into a list
		for i in range(1,len(list_title)):
		    
# 		    print(title[i].get_text()[12:])
		    list_title.append(title[i].get_text()[12:])

	def create_CSV(self,list_title,file_name):

	
		# Create the pandas DataFrame with Top Story as one of the columnn
		df = pd.DataFrame(list_title, columns = ['Top Story'])

		#Storing the result into a CSV file
		df.to_csv()


if __name__ == '__main__':
	#initialise a Class and 
	WebCrawler=WebCrawler()
	#Reading the configuration file
	config=WebCrawler.read_ini("config.ini")
	#Reading the URL to be parsed
	my_url=config["DEV_URL"]["URL"]
	#Get the title from the page
	page_soup=WebCrawler.get_title(my_url)
	#finding all title from the RSSfeed received as response
	list_title=WebCrawler.find_title(page_soup)
	#Creating a CSV using the file name of user's choice
	file_name=config["FILE_NAME"]["NAME"]
	#Using Pandas to_csv function to create a CSV file as output of the response received
	WebCrawler.create_CSV(list_title,file_name)