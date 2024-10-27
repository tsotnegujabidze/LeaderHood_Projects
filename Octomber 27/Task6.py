# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

def switch_case(text):
    result = []
    for i in range(len(text)):
        if i == 0:
            result.append(text[i].lower())
        elif text[i].isupper():
            result.append('_')
            result.append(text[i].lower())
        elif text[i] == ' ':
            text[i] == ''
        else:
            result.append(text[i])
    return ''.join(result)

print(switch_case("TestController")) # "TestController"  -->  "test_controller"

print(switch_case("MoviesAndBooks")) # "MoviesAndBooks"  -->  "movies_and_books"

print(switch_case("App7 Test")) # "App7 Test"  -->  "app7_test

print(switch_case("1")) # 1  -->  "1"