from typing import List
import requests
import random

class Fetch:
    def __init__(self, url, fetched_response):
        self.url = url
        self.fetched_response = fetched_response
    def fetch_request(self):
        try:
            response = requests.get(self.url, timeout=10)
            data = response.json()
            return data[self.fetched_response]
        except requests.RequestException as e:
            print('Error fetching data', e)
            return []


class UserChoice:
    def __init__(self):
        self.category = ''
        self.difficulty = ''
        self.type = ''
        self.question_type = ['multiple', 'boolean']
  
    def get_user_category_choices(self):
        print('-------Select a category based on the number---------')

        fetch_category = Fetch('https://opentdb.com/api_category.php', 'trivia_categories')
        category = fetch_category.fetch_request()
        for i in range(len(category)):
            item_name = category[i]['name']
            print(f'{i + 1}.{item_name}')
        usr_inp = int(input('select a category: '))
        self.category = category[usr_inp - 1]['id']


    def get_user_difficulty(self):
        print('----- select difficulity -----')
        difficulty_type = ['easy', 'medium', 'hard']

        while True:
            ##loop through difficulty_type
            for i in range(len(difficulty_type)):
                print(f'{i + 1}.{difficulty_type[i]}')
            difficulty_input = input('Enter the difficulty level: use number 1-3: ')

            ##Check weather the user input is within the range of the array(difficulty_type)
            if not difficulty_input.isdigit():
                print('please enter a number')
                continue

            difficulty_input = int(difficulty_input)

            if difficulty_input > len(difficulty_type) or difficulty_input < 1:
                print('Please enter a valid number')
                continue
            else:
                self.difficulty = difficulty_type[difficulty_input - 1]
                break

    def get_question_type(self):
        print('------ select the type of you question --------')

        while True:
            
            question_type_input = int(input('For multiple choice enter 1, For true/false enter 2: '))

            if question_type_input > len(self.question_type):
                print('please choose 1 or 2: ')
                continue
            else:
                self.type = self.question_type[question_type_input - 1]
                break


class Game(UserChoice):
    def __init__(self):
        super().__init__()
        self.score = 0
    
    def fetch_quiz_questions(self):
        fetch_questions = Fetch(f'https://opentdb.com/api.php?amount=10&category={self.category}&difficulty={self.difficulty}&type={self.type}','results')
        fetched_data = fetch_questions.fetch_request()
        if self.type == 'boolean':
            for i in range(len(fetched_data)): 
                question = fetched_data[i]['question']
                correct_answer = fetched_data[i]['correct_answer']
                ans = input(question + ': ')
                self.check_answer(ans, correct_answer)

        # For multiple choice
        else:
            for i in range(len(fetched_data)):
                question = fetched_data[i]['question']
                correct_answer = fetched_data[i]['correct_answer']
                multiple_choice = fetched_data[i]['incorrect_answers'] + [correct_answer]
                random.shuffle(multiple_choice)

                print(f'{i + 1}) {question}')
                for j in range(len(multiple_choice)):
                    print(f'{j + 1},{multiple_choice[j]}')

                ans = int(input(': '))
                self.check_answer(multiple_choice[ans - 1], correct_answer)
        
    def check_answer(self, ans, correct_answer):
            if ans.strip().lower() in correct_answer.strip().lower():
                self.score += 1

    def show_score(self):
        print('Your score out of 10 is: ', self.score)

start_game = Game()
while True:
    start_game.get_user_category_choices()
    start_game.get_user_difficulty()
    start_game.get_question_type()
    start_game.fetch_quiz_questions()
    start_game.show_score()

    inp = input('Do you want to play again? (Y/n): ').lower()
    if inp == 'n':
        break
    elif inp == 'y' or inp == '':
        start_game.score = 0
        continue
    else:
        print("Invalid input. Please enter 'Y' or 'n'.")
