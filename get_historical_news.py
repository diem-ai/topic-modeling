from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

if __name__ == "__main__":
    
    title_array = []
    headline_text  = []
#    links = []
#    articles = []
#    scores = []
    pageSize = 10
    n_pages = 500

    for p in range(1, n_pages):
            
        url = 'https://www.reuters.com/news/archive/mcbreakingviews?view=page&page=' + str(p) + '&pageSize=' + str(pageSize)
        soup = bs(requests.get(url).text, 'html.parser')
        titles = soup.find_all('h3', class_ = 'story-title')
        contents = soup.find_all('div', class_ ='story-content')

        #print(contents)

        for t in titles:
            title  = t.get_text()
            title = title.replace('Breakingviews - ', '')
            title = title.replace("\t", "")
            title = title.replace('\n', '')
            title_array.append(title)
        
        for content in contents:
            if content.find('p') is not None:
                headline_text.append(content.find('p').string)
                """
            link = content.find('a').get('href')
            if(link is not None) :
                links.append(link)
                scores.append(get_sentiment_score(link))
"""

    data = list(zip(title_array, headline_text))
    df = pd.DataFrame(data, columns = ['title', 'headline_text'])
    df.to_csv('data/breakingnews.csv', header=True, index=False, index_label=None)
    print("pulling breakingnews is completed.")
