print('\n\t Data Structures in Python\n\t #Section 2')
# // Challenge

'''
Many systems make information available through an API (application programming interface), which use JSON files (JavaScript object notation) to make data available. A JSON file is composed of elements in key-value form, which makes this format light to transfer and easy to manipulate.
As a developer at a consulting company, you were allocated to assist a client that organizes selective processes (public tender, entrance exam, etc.). This company has a web system in which candidates for a certain selection process register and follow the information. A certain contest had to be postponed, which is why a process on the server started sending emails to all the registered candidates. However, due to the large number of accesses, the server and the API went down for a few seconds, which caused a disruption in the creation of the JSON file with the list of candidates already notified of the change.
Due to the breach of the file, two new files were generated, which is why, since then, it is not known who or how many people have already received the notice. Your job, in this case, is to create a function that, based on the information that will be provided, returns a list with the emails that still need to be sent.
For this project, you and one more developer have been allocated. While your colleague works on extracting the data from the API, you create the logic to generate the function. It was agreed, between you, that the program will receive two dictionaries referring to the two files that were generated. The dictionary will have the following structure: three keys (name, email, sent), each of which receives a list of information; that is, the keys name and email will be, respectively, associated with a list of names and an email. in turn, the key sent will be associated with a list of Boolean values ​​(True-False) that will indicate whether or not the email has already been sent.

See an example.
'''

dict1 = {
  'name': ['name1'],
  'email': ['email1'],
  'sent': [False]
}

# Resolution

data1 = {
    'name': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'sent': [False, False, False, False, False, False, False, True, False, False]
}

data2 = {
    'name': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'sent': [False, False, False, True, True, True, False, True, True, False]
}

def extractEmailList(dict1, dict2):
    list1 = list(zip(dict1['name'], dict1['email'], dict1['sent']))
    print(f'\n ——————————\n List sample 1: {list1[0]}')

    list2 = list(zip(dict2['name'], dict2['email'], dict2['sent']))
    data = list1 + list2

    print(f' Data sample: {data[:2]}')
    
    # We want a list with the email of those who have not yet received the notice
    emails = [item[1] for item in data if not item[2]]
    return emails

emails = extractEmailList(dict1 = data1, dict2 = data2)
print(f' Emails to be sent: {emails}\n ——————————')

# // Internet Challenge

'''
On page 116 of Chapter 4 of the following work, you can find exercise 6 (Use of lists). In it, the author proposes the construction of an arithmetic progression using lists in Python.
BANIN, S. L. Python 3 - concepts and applications: a didactic approach.
'''

'''
Write a program that reads a list of N integers, where N is an integer previously entered by the user.
The program must not accept a typed number that is already inserted in the list, and when this situation occurs, a message must be given to the user.
Finally, display the resulting list on the screen.
'''

# Resolution

List = []
def veri(Inp):
    global List

    try:
        Inp = int(Inp)
        assert Inp not in List
        List.append(Inp)
    except AssertionError: print(' Number already entered.')
    except ValueError: pass
    finally:
        if Inp == '': return False
        else: return True

while veri(input(' Enter a number: ')): pass
else: print(f'\n Resulting list: {List}')
