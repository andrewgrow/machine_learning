import pandas
import os

# cd 01-titanic-assignment -- python3 App.py

real_path = os.path.dirname(os.path.realpath(__file__))

separator = '\\'


def check_separator_by_os():
    if '\\' not in real_path and '/' in real_path:
        global separator
        separator = '/'


def print_answer(answer_number: int, answer_value: str) -> None:
    print("save answer ", answer_number)
    check_separator_by_os()
    answer_path = real_path + separator + 'answers' + separator + 'a' + answer_number.__str__() + '.txt'
    answer_file = open(answer_path, 'w')
    answer_file.write(answer_value)
    answer_file.close()


def question1():
    # 1. How many men and women were traveling by ship?
    counts = data['Sex'].value_counts()
    answer1 = '{} {}'.format(counts['male'], counts['female'])
    print_answer(1, answer1)


def question2():
    # What part of the passengers managed to survive?
    survived_counts = data['Survived'].value_counts()
    all_passengers = survived_counts.sum()
    part_survived_percents = survived_counts[1] * 100 / all_passengers
    answer2 = '{:.2f}'.format(part_survived_percents)
    print_answer(2, answer2)


#
#
#

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print("start work with question1 : 01-titanic-assignment")
print(data.columns)
# print(data.describe())

# question1()
question2()
