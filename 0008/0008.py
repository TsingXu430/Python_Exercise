import io

file = io.open('filtered_words.txt', 'r', encoding='utf-8')
filtered_list = []
for word in file.readlines():
    filtered_list.append(word.strip('\n'))

print(filtered_list)


def is_valid(user_word):
    for x in filtered_list:
        if user_word == x:
            return False
    return True


def change_word(user_word):
    for x in filtered_list:
        if user_word.find(x) != -1:
            user_word = user_word.replace(x, '**')
    return user_word


my_word = input('Please Input:')

'''if is_valid(my_word):
    print('Human Rights')
else:
    print('Freedom')'''

print(change_word(my_word))

file.close()
