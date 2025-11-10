thonfrom bs4 import BeautifulSoup

def parse_reviews(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    reviews = []
    review_elements = soup.find_all('div', class_='review-container')

    for element in review_elements:
        review = {
            'id': element.get('data-review-id'),
            'lang': element.find('span', class_='lang').text if element.find('span', class_='lang') else 'en',
            'location_id': element.find('a', class_='location').get('href').split('-')[-1],
            'published_date': element.find('span', class_='ratingDate').text.strip(),
            'rating': element.find('span', class_='ui_bubble_rating').get('class')[1].split('_')[1],
            'helpful_votes': element.find('span', class_='helpfulVotes').text.strip(),
            'url': 'https://www.tripadvisor.com' + element.find('a', class_='title').get('href'),
            'travel_date': element.find('div', class_='travel_date').text.strip() if element.find('div', class_='travel_date') else 'Unknown',
            'tripType': element.find('div', class_='trip_type').text.strip() if element.find('div', class_='trip_type') else 'Unknown',
            'text': element.find('p', class_='partial_entry').text.strip(),
            'title': element.find('span', class_='noQuotes').text.strip(),
            'user': {
                'user_id': element.find('span', class_='username').get('data-userid'),
                'name': element.find('span', class_='username').text.strip(),
                'username': element.find('span', class_='username').text.strip(),
                'avatar': element.find('img', class_='avatar').get('src') if element.find('img', class_='avatar') else ''
            },
            'photos': [
                {'id': photo.get('id'), 'url': photo.get('src')} for photo in element.find_all('img', class_='photo')
            ],
            'owner_response': {
                'id': element.find('div', class_='ownerResponse').get('id') if element.find('div', class_='ownerResponse') else '',
                'responder': element.find('span', class_='ownerResponseName').text if element.find('span', class_='ownerResponseName') else '',
                'text': element.find('span', class_='ownerResponseText').text.strip() if element.find('span', class_='ownerResponseText') else ''
            },
            'subratings': [
                {'name': subrating.find('span', class_='subrating-name').text.strip(), 'value': subrating.find('span', class_='subrating-value').text.strip()}
                for subrating in element.find_all('div', class_='subrating')
            ]
        }
        reviews.append(review)
    
    return reviews