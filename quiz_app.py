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



class Game:
    def __init__(self):
        self.category = ''
        self.difficulty = ''
        self.type = False
  
    def get_user_category_choices(self):
        fetch_category = Fetch('https://opentdb.com/api_category.php', 'trivia_categories')
        category = fetch_category.fetch_request()
        for item in category:
            item_id = item['id']
            item_name = item['name']
            print(f"{item_id}, {item_name}")
        self.category = input('Select a category: ')
    
    def get_user_difficulty(self):
        print('----- select difficulity -----')
        self.difficulty = input('Easy, Medium, Hard: ').lower()

    def get_user_type(self):
        print('------ select the type of you question: Multiple choice or True/false --------')
        self.type = input()





start_game = Game()
start_game.get_user_category_choices()
start_game.get_user_difficulty()