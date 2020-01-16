import random

class Parent:

    def number():
        number = str(random.randint(1,9))
        return number

    def lowercase_letter():
        lettter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return random.choice(lettter_list)

    def uppercase_letter():
        letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return random.choice(letter_list)

    def symbols():
        symbol_list = ['!','@','#','$','%','^','&','*','(',')']
        return random.choice(symbol_list)


class Default(Parent):

    def password():
        lists = [Default.number(),Default.uppercase_letter(),Default.lowercase_letter(),Default.symbols()]
        password =[]
        for i in range(1,9):
            if len(lists)>=2:
                random_select = random.choice(lists)
                if(random_select==Default.lowercase_letter()):
                    password.append(random_select)
                else:
                    password.append(random_select)
                    lists.remove(random_select)
            else:
                password.append(Default.lowercase_letter())
        password_string = ''.join(password)
        return password_string
    

