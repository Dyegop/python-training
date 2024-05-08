"""
Creates 35 different quizzes
Creates 50 multiple-choice questions for each quiz, in random order
Provides the correct answer and three random wrong answers for each question, in random order
Writes the quizzes to 35 text files
Writes the answer keys to 35 text files
"""

import random


# States and capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

quizzes = 35
questions = 50
path2 = 'C:\\Users\\ponce\\Downloads\\PyFolder\\'
path = 'C:\\Users\\Diego\\Downloads\\PyFolder\\'
answers = path + 'Answers\\'
header = 'Name:\n\nDate:\n\nPeriod:\n\n'


def answer_generator(true_ans):
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(true_ans)]
    return random.sample(wrong_answers, 3)

for quizNum in range(quizzes):
    # Create n number of quiz files
    with open(path+f'Quiz_{quizNum+1}.txt', 'w') as f:
        # Write header for each file
        f.write(header)
        f.write('-'*20 + f'State Capitals Quiz (Form{quizNum+1})'+'-'*20)
        f.write('\n\n\n')
        # Create list of States and shuffle them
        states = list(capitals.keys())
        random.shuffle(states)
        for question in range(questions):
            # Write question
            f.write(f'{question+1}. What is the capital of {states[question]}?')
            f.write('\n\n')
            # Get true answer - dictionary.get[list_of_keys[int]]
            true_answer = capitals.get(states[question])
            # Get list of answer options
            # adding [] to a variable to turn it into list object
            answer_options = answer_generator(true_answer) + [true_answer]
            random.shuffle(answer_options)
            for answer in range(4):
                f.write(f"    {'ABCD'[answer]}. {answer_options[answer]}\n")
                f.write('\n')
            f.write("\n")
        f.close()

    # Create n number of quiz files
    with open(answers+f'Answers_{quizNum+1}.txt', 'w') as f2:
        f2.write('-' * 20 + f'Answers for State Capitals Quiz (Form{quizNum + 1})' + '-' * 20)
        f2.write('\n\n\n')
        for question in range(questions):
            true_answer = capitals.get(states[question])
            f2.write(f'{question+1}. Correct answer: {true_answer}\n')
            f2.write('\n')
        f2.close()
