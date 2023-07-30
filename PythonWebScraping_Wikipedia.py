# 1- Importing libraries

from bs4 import BeautifulSoup
import requests


# 2- Connect to website and pull in data
URL = 'https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}


page = requests.get(URL, headers=headers)


soup1 = BeautifulSoup(page.content, 'html.parser')


soup2 = BeautifulSoup(soup1.prettify(),'html.parser')



# 3- Creating a list for each variable, and filling them using for loops
ranking = []
for i in range (0,100):
    rank = soup2.find_all('th', attrs = {'style': 'text-align:center;'})[i].text
    rank = rank.replace('\n','')
    rank = rank.strip()
    ranking.append(rank)
    
    
song_list = []
for i in range(0,500,5) :
    song = soup2.find_all('td')[i].text
    song = song.replace('\n','')
    song = song.replace('"','')
    song = song.strip()
    song = ' '.join(song.split())
    song_list.append(song)   
    
    
streams_list = []
for i in range(1,500,5) :
    streams = soup2.find_all('td')[i].text
    streams = streams.replace('\n','')
    streams = streams.strip()
    streams_list.append(streams)    
    
    
artist_list = []
for i in range(2,500,5):
    artist = soup2.find_all('td')[i].text
    artist = artist.replace('\n','')
    artist = artist.strip()
    artist = ' '.join(artist.split())
    artist_list.append(artist)
    
    
date_list = []
for i in range(3,500,5):
    date = soup2.find_all('td')[i].text
    date = date.replace('\n', '')
    date = date.strip()
    date_list.append(date)
    
# 4- Creating dictionary and assigning the filled variables
data = {
    'Rank' : ranking,
    'Song' : song_list,
    'Streams' : streams_list,
    'Artist' : artist_list,
    'Date' : date_list
}    

# 5- Importing pandas to create the DataFrame
import pandas as pd

df = pd.DataFrame(data)

# 6- Importing the data do .CSV
df.to_csv('Top100-MostStreamedSongs-Spotify.csv')