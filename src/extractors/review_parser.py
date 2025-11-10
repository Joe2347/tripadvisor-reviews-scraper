thonimport json
import requests

class ReviewParser:
    @staticmethod
    def parse_review_data(review_data):
        parsed_data = {
            'id': review_data.get('id'),
            'title': review_data.get('title'),
            'rating': review_data.get('rating'),
            'text': review_data.get('text'),
            'user': review_data.get('user'),
            'photos': review_data.get('photos'),
        }
        return parsed_data

    @staticmethod
    def parse_json_response(response_json):
        return [ReviewParser.parse_review_data(review) for review in response_json]