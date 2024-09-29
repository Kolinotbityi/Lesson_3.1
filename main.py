
calls = 0

def count_calls():
    global calls
    calls = 1

def string_info(string):
    str_ = str(string)
    res_ = (len(str_), str_.upper(), str_.lower())
    return res_

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            res_ = True
            break
        else:
            res_ = False
            continue
    return res_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
