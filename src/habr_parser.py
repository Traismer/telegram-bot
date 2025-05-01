import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from sqlalchemy.orm import Session
from src.models.news import News

class HabrParser:
    BASE_URL = "https://habr.com"
    
    @staticmethod
    def get_news(db: Session, count: int = 2) -> List[Dict[str, str]]:
        """
        Получает указанное количество новых новостей с Хабра
        """
        try:
            response = requests.get(f"{HabrParser.BASE_URL}/ru/all/")
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article', class_='tm-articles-list__item')
            
            news_list = []
            for article in articles:
                if len(news_list) >= count:
                    break
                    
                title_elem = article.find('h2', class_='tm-title')
                link_elem = title_elem.find('a') if title_elem else None
                
                if title_elem and link_elem:
                    title = title_elem.text.strip()
                    link = f"{HabrParser.BASE_URL}{link_elem['href']}"
                    
                    # Получаем автора
                    author_elem = article.find('a', class_='tm-user-info__username')
                    author = author_elem.text.strip() if author_elem else "Неизвестный автор"
                    
                    # Получаем количество просмотров
                    views_elem = article.find('span', class_='tm-icon-counter__value')
                    views = views_elem.text.strip() if views_elem else "0"
                    
                    # Получаем URL изображения
                    image_elem = article.find('img', class_='tm-article-snippet__lead-image')
                    image_url = image_elem['src'] if image_elem else None
                    
                    # Проверяем, не отправляли ли мы уже эту новость
                    existing_news = db.query(News).filter(News.title == title).first()
                    if not existing_news:
                        news_list.append({
                            'title': title,
                            'link': link,
                            'author': author,
                            'views': views,
                            'image_url': image_url
                        })
            
            return news_list
        except Exception as e:
            print(f"Error while parsing Habr: {e}")
            return [] 