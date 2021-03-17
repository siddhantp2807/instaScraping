import openpyxl as opl
import pandas as pd
from scraper import InstaScraper


#Url of instagram posts, this is just for demonstration purpose for a few posts
postUrls = ['https://www.instagram.com/tv/CMHzTJLJCVI/', 'https://www.instagram.com/p/CL3OqR8FeBH/', 'https://www.instagram.com/p/CMcwTEDAEbq/', 'https://www.instagram.com/p/CL7CEeBAdwy/', 'https://www.instagram.com/p/CMgn2x-HTKd/', 'https://www.instagram.com/p/CMO3mM9H8TT/']

#add data of post to a list
finalData = []
for i in postUrls :
    finalData.append(InstaScraper(i).parsedFinalData())

#add all data to an xlsx file 
pd.DataFrame.from_dict(finalData).to_excel('data.xlsx', index=False)






