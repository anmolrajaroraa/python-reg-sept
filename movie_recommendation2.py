dataset={
    "romance" : ['Shuddh Desi Romance' , 'Aashiqui' ,'Lootera' , 'Raanjhanaa' ,'Yeh Jawaani Hai Deewani' ,'Jab Tak Hai Jaan' ,'Jannat 2' ,'Kal Ho Naa Ho' , 'Dilwale Dulhania Le Jayenge' ,'Fanaa' , 'Rab Ne Bana Di Jodi' ,'Ghulam' ,'Chalte Chalte','Hum Tum','Dil Chahta Hai' ,'Love Aaj Kal','Saajan','Jab We Met','Vivah','Devdas'],
    "comedy" : ['Made In China','Housefull 4','Life Mein Time Nahi Hai Kisi Ko','Jo Hal Dil Ka','Judgemental Hai Kya','Jabariya Jodi','Khandaani shafakhana','Gun Pe Done','De De Pyaar de','Mere Pyare Prime Minister','Luka Chupi','Hera Pheri','Munna Bhai M.B.B.S','3 Idiots','Coolie No 1','Heyy Baby','Bheja Fry','Chachi 420','Welcome'],
    "action" : ['War','Kesari','Uri The Surgical Strike','Junglee','Kabir Singh','Sonchiriya','Manikarna The Queen','Sahoo','','Article 15','Marjaava','Laal Kaptaan','Jabariyan jodi','Bagghi','Wanted','Ghajini','Badlapur','Don','Krish','Dishoom'],
    "horror" : ['Amavas','Midsommar','Pari2','Ghost','Bhoot part one','Khamoshi','Arjun patiala','Escape room','Itsy Bitsy','Conjuring 2','Khamoshi','Pari','Raginni MMS','Alone','Darna Mana Hai','Raaz','Kaal','Aatma','Naagin','Stree'],
    "biopic" : ['Bhaag milkha Bhaag','War','Neerja','Mary kom','The dirty picture','Dangal','Paan Singh tomar','Bandit Queen','Haseena Parkar','shahid'] 
    }

user1_action = ['Aashiqui', 'War' ,'Kesari' ,'Kabir Singh','Pari2','Article 15','Kal Ho Naa Ho','Escape room','Pari','Mary kom','Dangal','Sonchiriya','Conjuring 2','Ghost','shahid','Bandit Queen','Laal Kaptaan','Kaal','Aatma','Luka Chupi','Krish','Dishoom']
user2_romance =['Aashiqui','Kabir Singh','Raanjhanaa','Article 15','Jannat 2','Escape Room','Dilwale Dulhania Le Jayenge','Fanaa','Chalte Chalte','shahid','Gun Pe Done','Sahoo','Kal Ho Naa Ho','Raginni MMS','Ms Dhoni the untold Story','Paan Singh tomar','The dirty picture']
user3_biopic=['Ghost','Manikarna The Queen','Khamoshi','Bypass road','Kal Ho Naa Ho','War','Pari','Dangal','Article 15','Conjuring 2','Pari2','Ghost','Paan Singh tomar','The dirty picture','Neerja','Bandit Queen','Laal Kaptaan','Kaal','Aatma','Luka Chupi','Krish','Dishoom','Sahoo']

intersection1 = len(set(user1_action).intersection(set(user2_romance)))
intersection2 = len(set(user1_action).intersection(set(user3_biopic)))
union1 =len(set(user1_action).union(set(user2_romance)))
union2 = len(set(user1_action).union(set(user3_biopic)))

similarity1= intersection1/union1 * 100
similarity2 = intersection2/union2*100

similarity = user2_romance if similarity1>= similarity2 else user3_biopic
#print(similarity)
dict_user1_most_watched_genre=dict.fromkeys(dataset.keys(),0)
for key in dataset:
    for movie in user1_action:
        if movie in dataset[key]:
            dict_user1_most_watched_genre[key] += 1

list_user1_most_watched_genre_keys = list(dict_user1_most_watched_genre.keys())
list_user1_most_watched_genre_values = list(dict_user1_most_watched_genre.values())

index = list_user1_most_watched_genre_values.index(   max(   list_user1_most_watched_genre_values   )   )

most_watched_category = list_user1_most_watched_genre_keys[index]

print("Most watched category is",most_watched_category)

unseen_movies_user1 = set(dataset[most_watched_category]) - set(user1_action)

recommended_movies_based_on_similarity = unseen_movies_user1.intersection(set(similarity))

print(recommended_movies_based_on_similarity)

# if list_user1.count('romance')>(list_user1.count('comedy') and list_user1.count('action') and list_user1.count('horror') and list_user1.count('biopic')):
#     print("most watched genre by user1 is Romance")
#     #list(listromance)=set(dataset['romance'])-set(user1_action)
#     print("Recomendation for user 1 is",listromance[0],listromance[1])
# elif  list_user1.count('action')>(list_user1.count('comedy') and list_user1.count('horror') and list_user1.count('biopic')and list_user1.count('romance')):
#     #print('most watched genre by user1 is action')
#     action=set(dataset['action'])-set(user1_action)
#     listaction=[]
#     for i in action:
#         listaction.append(i)
#     print(listaction[0])
#
#     print("Recomendation for user 1 is",listaction[2],'and',listaction[1])
#
# elif list_user1.count('comedy') > (list_user1.count('action') and list_user1.count('horror') and list_user1.count('biopic') and list_user1.count('romance')):
#     print('most watched genre by user1 is comedy')
# elif list_user1.count('horror') > (list_user1.count('comedy') and list_user1.count('action') and list_user1.count('biopic')and list_user1.count('romance')):
#     print('most watched genre by user1 is horror')
# elif list_user1.count('biopic')> (list_user1.count('comedy') and list_user1.count('action') and list_user1.count('horror') and list_user1.count('romance')):
#     print('most watched genre by user1 is biopic')

                                  
'''
count1=0
count2=0
count3=0  count4=0
count5=0
for genre in list_user1:
    if genre=="romance":
        count1+=1
    elif genre=="comedy":
        count2+=1
    elif genre=="action":
        count3+=1
    elif genre=="horror":
        count4+=1
    elif genre=="biopic":
        count5+=1
    
m=max(count1,count2,count3,count4,count5)
print(m)
'''
