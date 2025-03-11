import requests
from bs4 import BeautifulSoup

def fetch_tvbs_news():
    url = 'https://news.tvbs.com.tw/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('div', class_='news_list')
        
        news_list = []
        for item in news_items:
            title = item.find('h2').text.strip()
            link = item.find('a')['href']
            news_list.append({'title': title, 'link': link})
        
        return news_list
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    news = fetch_tvbs_news()
    for idx, item in enumerate(news):
        print(f"{idx + 1}. {item['title']}\n   Link: {item['link']}")