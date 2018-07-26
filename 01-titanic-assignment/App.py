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

    print(data['Sex'].value_counts())  # clear solution

    male = data[data.Sex == 'male'].__len__()
    female = data[data.Sex == 'female'].__len__()
    answer1 = male.__str__() + " " + female.__str__()
    print_answer(1, answer1)


data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print("start work with question1 : 01-titanic-assignment")

# question1()  # SOLVED!
