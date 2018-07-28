import pandas
import os
import re

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


def question3():
    # What percentage of the first class passengers were among all passengers?
    classes_counts = data['Pclass'].value_counts()
    answer3 = '{:.2f}'.format(classes_counts[1] * 100 / classes_counts.sum())
    print_answer(3, answer3)


def question4():
    # What age were passengers? Calculate the average and the median.
    describe = data['Age'].describe()
    print_answer(4, '{:.2f} {:.2f}'.format(describe[1], describe[5]))


def question5():
    # Коррелируют ли число братьев/сестер с числом родителей/детей?
    # Посчитайте корреляцию Пирсона между признаками SibSp и Parch.

    # Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
    # Посчитайте корреляцию Пирсона между признаками SibSp и Parch.

    print_answer(5, '{:.2f}'.format(data['SibSp'].corr(data['Parch'])))


def question6():
    def clean_name(name):
        # Первое слово до запятой - фамилия
        s = re.search('^[^,]+, (.*)', name)
        if s:
            name = s.group(1)

        # Если есть скобки - то имя пассажира в них
        s = re.search('\(([^)]+)\)', name)
        if s:
            name = s.group(1)

        # Удаляем обращения
        name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)

        # Берем первое оставшееся слово и удаляем кавычки
        name = name.split(' ')[0].replace('"', '')

        return name

    names = data[data['Sex'] == 'female']['Name'].map(clean_name)
    name_counts = names.value_counts()
    print_answer(6, name_counts.head(1).index.values[0])


#
#
#

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print("start work with question1 : 01-titanic-assignment")
print(data.columns)
# print(data.describe())

# question1()
# question2()
# question3()
# question4()
# question5()
question6()
