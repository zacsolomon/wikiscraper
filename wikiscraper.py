#!/usr/bin/python


# we would like a dictionary of all the communities in the wiki page
# we want them will their links
# want the community names as keys, and the relative links as values

## It should look something like this:

## example = {
##    'University Heights' : '/wiki/University_Heights/',
##    'La Jolla' : '/wiki/La Jolla/'
## }

import requests
from bs4 import BeautifulSoup

sd_communities = 'https://en.wikipedia.org/wiki/List_of_communities_and_neighborhoods_of_San_Diego'

page = requests.get(sd_communities)
soup = BeautifulSoup(page.content, 'html.parser')

link_table = soup.select_one('table.multicol')

# create dictionary "communities"
communities = {}


# iterate through list 
# set community names as keys
# set links as values
 
for item in link_table.find_all('li'):
	communities[item.text] = item.find('a').attrs['href']
###
# now we want a dictionary with community names and their geo-locations
# 
###

base_wiki = 'https://en.wikipedia.org'
com_geo = {}

for key in communities:
	link = base_wiki + communities.get(key)
	print(link)
	if len(link) > 70:            
                continue
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')		
	if soup.select_one('title').text == 'List of communities and neighborhoods of San Diego - Wikipedia':	
		continue
	# try soup.select_one('span.geo-dec').text:
	#	except AttributeError:	
	com_geo[key] =  soup.select_one('span.geo-dec').text
	print(com_geo[key])	

print(com_geo) 




