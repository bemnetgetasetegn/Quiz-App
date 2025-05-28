from typing import List
import requests

class Fetch:
    def __init__(self, url, fetched_response):
        self.url = url
        self.fetched_response = fetched_response
    def fetch_request(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data[self.fetched_response] 
        except requests.RequestException as e:
            print('Error fetching data', e)
            return []


class Quiz_details:
    def __init__(self, category, difficulty, type):
        self.category = category
        self.type = type
        self.difficulty = difficulty
    
class Game:
    def get_user_choices(self):
        fetch_category = Fetch('https://opentdb.com/api_category.php', 'trivia_categories')
        category = fetch_category.fetch_request()
        for items in category:
            print(f"{items.id}, {items.name}")

start_game = Game()
start_game.get_user_choices()