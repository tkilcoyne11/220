"""
Name: Tucker Kilcoyne
Lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = str(input("Enter a name in first-last order: "))
    name_split = name.split(' ')
    reverse = name_split[1] + ", " + name_split[0]
    print(reverse)


def company_name():
    url = str(input("Enter the three-part internet domain name: "))
    url_split = url.split('.')
    company = url_split[1]
    print(company)


def initials():
    n_students = int(input("Enter the number of students: "))
    for i in range(0, n_students):
        f_name = str(input("Enter the first name of student  "+str(i+1)+": "))
        l_name = str(input("Enter "+str(f_name)+"'s last name: "))
        print(str(f_name)+"'s initials are "+f_name[0]+l_name[0]+". ")


def names():
    full_names = str(input("Enter the names of all the students in the class, separated by commas: "))
    names_split = full_names.split(", ")
    print("The initials are:", end=" ")
    for name in names_split:
        name_splits = name.split(' ')
        f_name = name_splits[0]
        l_name = name_splits[1]
        print(f_name[0]+l_name[0], end=" ")
    print('')


def thirds():
    sentences = int(input("How many sentences will be input? "))
    for i in range(0, sentences):
        x = str(input("Enter the sentence: "))
        length = len(x)
        third = x[2:length:3]
        print(third)


def word_average():
    n = int(input("How many sentences will you input? "))
    for i in range(n):
        x = str(input("Enter the sentence: "))
        x_split = x.split()
        acc = 0
        total_words = len(x_split)
        for word in x_split:
            word_length = len(word)
            acc += word_length
        average_length = acc / total_words
        print(round(average_length, 4))


def pig_latin():
    sentence = str(input("Enter a sentence: "))
    words = sentence.split()
    for word in words:
        new_word = word[1:] + word[0] + "ay"
        new_word = new_word.lower()
        print(new_word, end=' ')
    print(' ')


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

main()
