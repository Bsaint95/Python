import random
import string

list = []

def profile_generator():
    print('Please enter your details below')
    Firstname = input('Firstname: ')
    Lastname = input('Lastname: ')
    Email = input('Email: ')

    '''
    # This generates a random password for the user from
    :param firstname:
    :param lastname:
    :return: randomly generated password
    '''
    Password = f' {Firstname[0:2]}{Lastname[-2:]}'
    Password += ''.join(random.choice(string.ascii_letters) for i in range(5))
    print('your password is:')
    print(Password)

    feedback = input('Satisfied with password Yes/No? : ')
    if feedback.upper() == 'YES':
        print('Done, Thank you for registering!')
    else:
        """
        # This enables user to input desired password
        : return:
        """
        new = input('Enter desired password: ')

        while True:
            if len(new) < 7:
                new = input('Password must not be less than 7 characters, try agin: ')
            elif len(new) >= 7:
                Password = new
                print('Password Ok')
                print('Done, Thank you for registering!')
                break
    '''
    This generates the profile dictionary and inserts it in the list.
    : return: None
    '''
    user_details = {
    'Firstname': Firstname,
    'Lastname': Lastname,
    'Email': Email,
    'Password': Password
    }

    list.append(user_details)
    '''
    This compiles the list profiles and prints out the list.
    :return: None
    '''
    while True:
        counter = 0
        action = input('To continue to next user, press 1 otherwise press 2 \n: ')
        if int(action) == 1:
            profile_generator()
            
        elif int(action) == 2 and list == []:
            print('No records founds')
            break
        
        elif int(action) == 2 and list != []:
            print('These are the details of all registered users.\n---------------------------\n ')
            for profile in list:
                print(f'Firstname: {profile["Firstname"]} \n'
                      f'Lastname: {profile["Lastname"]} \n'
                      f'Email: {profile["Email"]} \n'
                      f'Password: {profile["Password"]}\n')
            break
        break

            
profile_generator()
