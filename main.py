
email = input('Please enter your Email ID: ').lower()

if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if email[-4] == "." or email[-3] == ".":
                print(email)

            else:
                print('wrong email 4')
        else:
            print('wrong email 3')


    else:
        print('wrong email 2')
else:
    print('wrong email ID 1')




