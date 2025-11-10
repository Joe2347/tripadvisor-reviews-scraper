thonimport requests
from bs4 import BeautifulSoup
import json
import csv
import os
from datetime import datetime

class TripadvisorScraper:
    def __init__(self, url, max_reviews=10):
        self.url = url
        self.max_reviews = max_reviews
        self.reviews = []
    
    def scrape_reviews(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        review_elements = soup.find_all('div', class_='review-container')
        
        for review_element in review_elements[:self.max_reviews]:
            review = self.extract_review_data(review_element)
            self.reviews.append(review)
        
        return self.reviews
    
    def extract_review_data(self, review_element):
        review = {}
        review['id'] = review_element.find('div', class_='prw_rup prw_reviews_rating').get('data-review-id')
        review['url'] = self.url
        review['title'] = review_element.find('span', class_='noQuotes').text
        review['lang'] = 'en'
        review['publishedDate'] = review_element.find('span', class_='ratingDate')['title']
        review['rating'] = review_element.find('span', class_='ui_bubble_rating')['class'][1].split('_')[-1]
        review['helpfulVotes'] = review_element.find('span', class_='helpfulVotes').text.strip()
        review['text'] = review_element.find('p', class_='partial_entry').text.strip()
        review['user'] = {
            'username': review_element.find('span', class_='scrname').text,
            'location': review_element.find('span', class_='location').text,
            'avatar': review_element.find('img', class_='avatar')['src'],
            'link': 'https://www.tripadvisor.com' + review_element.find('span', class_='scrname').find_parent('a')['href']
        }
        return review
    
    def save_to_file(self, filename='scraped_reviews.json'):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.reviews, file, ensure_ascii=False, indent=4)

    def save_to_csv(self, filename='scraped_reviews.csv'):
        keys = self.reviews[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.reviews)