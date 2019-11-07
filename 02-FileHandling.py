import csv

users = [
    {
        'username' : 'ram',
        'email' : 'ram@gmail.com',
        'password' : 'ram123'
    },
    {
        'username' : 'shyam' ,
        'email' : 'shyam@gmail.com' ,
        'password' : 'shyam123'
    }
]

'''with open('users.csv', 'w') as file:
    writer = csv.writer(file)
    for user in users:
        writer.writerow(user.values())'''

users = []
keys = []
isHeader = True
with open('users.csv') as file:
    data = csv.reader(file)
    for row in data:
        if isHeader:
            keys = row
            isHeader = False
            print(keys)
            continue
        user = {i:j for i,j in zip(keys,row)}
        print(user)
        users.append(user)
        #print(row[0], row[1], row[2])
    print(users)

'''with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = users[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user)'''