import os
import anaconda
def trend():
    os.system('cls')
    mangas= ["01. One Piece",
             "02. Chainsaw man",
             "03. One Punch Man",
             "04. Black Clover",
             "05. Spy x Family",
             "06. Kakkou no Iinazuke",
             "07. Yofukashi no Uta",
             "08. Jujutsu Kaisen",
             "09. Demon Slayer",
             "10. Yakusoku no Neverland"]
    print('\nTOP 10 Manga on the week')
    #masukan : list iteration
    # for i in mangas:
    for i in range(10):
        print(mangas[i])
    print("="*25)    
    detail = input("\ninfo detail nomor : ")
    if detail == '1':
        os.system('cls')
        print("One Piece\n")
        print("Genre\t\t: Adventure, Fantasy, Shounen.\n"+
              "Tahun\t\t: 1997\n"+
              "Pengarang\t: Eiichiro Oda\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 1055\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100140\n")
        print("Luffy and the Straw Hat Pirates take on the wealthy and ambitious Gild Tesoro,\n"+ 
              "captain of a massive ship labelled the moving country of dreams.")
    elif detail == '2':
        os.system('cls')
        print("Chainsaw man\n")
        print("Genre\t\t: Action, Horror comedy, Dark Fantasy.\n"+
              "Tahun\t\t: 2018\n"+
              "Pengarang\t: Tatsuki Fujimoto\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 107\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100037\n")
        print("Chainsaw Man follows the story of Denji,\n"+ 
              "an impoverished young man who makes a contract that fuses his body with that of a dog-like devil named Pochita,\n"+
              "granting him the ability to transform parts of his body into chainsaws.")
    elif detail == '3':
        os.system('cls')
        print("One Punch Man\n")
        print("Genre\t\t: Action, Comedy, Superhero, Fiction.\n"+
              "Tahun\t\t: 2009\n"+
              "Pengarang\t: Yusuke Murata\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 221\n"+
              "Link\t\t: https://mangadex.org/title/d8a959f7-648e-4c8d-8f23-f1f3f8e129f3/one-punch-man\n")
        print("Saitama, the protagonist,\n" + 
              "is an exceptionally powerful hero who easily defeats the monsters or other villains with a single punch.\n" + 
              "However, due to his overwhelming strength..\n" + 
              "Saitama has become bored with his powers and is constantly trying to find stronger opponents who can fight him.")
    elif detail == '4':
        os.system('cls')
        print("Black Clover\n")
        print("Genre\t\t: Action, Adventure, Comedy, Fantasy, Shounen.\n"+
              "Tahun\t\t: 2015\n"+
              "Pengarang\t: Yuki Tabata\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 341\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100141\n")
        print("The story follows Asta, a young boy born without any magic power.\n" +  
              "This is unknown to the world he lives in because seemingly everyone has some sort of magic power.\n" +
              "With his fellow mages from the Black Bulls, Asta plans to become the next Wizard King.")
    elif detail == '5':
        os.system('cls')
        print("Spy x Family\n")
        print("Genre\t\t: Action, Comedy, Fiction, Spy.\n"+
              "Tahun\t\t: 2019\n"+
              "Pengarang\t: Tatsuya Endou\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 68\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100143\n")
        print("The story follows a spy who has to build a family to execute a mission,\n" +
              "not realizing that the girl he adopts as his daughter is a telepath,\n" + 
              "and the woman he agrees to be in a marriage with is a skilled assassin.")
    elif detail == '6':
        os.system('cls')
        print("Kakkou no Iinazuke\n")
        print("Genre\t\t: Harem, Romance, Comedy.\n"+
              "Tahun\t\t: 2020\n"+
              "Pengarang\t: Miki Yoshikawa\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 130\n"+
              "Link\t\t: https://mangadex.org/title/4e7a4a0f-8391-4069-839b-de2352297dab/a-couple-of-cuckoos\n")
        print("The members of the Umino household are all rather similar: they are energetic and incredibly dynamic" + 
              "—except for Nagi, a serious and introverted young man whose sole focus is on academics.\n" + 
              "He is the complete opposite of someone like his younger sister Sachi, " + 
              "who is a reflection of her extroverted parents.\n" + 
              "Thus, it should come as no surprise that Nagi was swapped with another baby at birth." +
              "On the way to meet his true parents, Nagi encounters Erika Amano, a young social media star.\n" + 
              "While spending the day with her, he learns that Erika's parents forced a marriage onto her.\n" + 
              "Later that day, Nagi comes to learn that Erika's fiancé is actually none other than himself," + 
              "in order to officially be part of  each other's family." + 
              " With the goal to build the pair's relationship,\n" +  
              "Nagi's biological father arranges for the fiancés to start living together!\n" +
              "However, no matter what tricks their parents pull, Nagi refuses to marry Erika.\n" + 
              "That is because he already has sights set on someone else: the beautiful and intelligent Hiro Segawa.")
    elif detail == '7':
        os.system('cls')
        print("Yofukashi no Uta\n")
        print("Genre\t\t: Romance, Comedy, Supernatural, Fiction.\n"+
              "Tahun\t\t: 2019\n"+
              "Pengarang\t: Kotoyama\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 145\n"+
              "Link\t\t: https://mangadex.org/title/259dfd8a-f06a-4825-8fa6-a2dcd7274230/yofukashi-no-uta\n")
        print("On one such walk, Kou meets a weird girl, Nazuna Nanakusa," + 
              "who diagnoses the cause of his sleeplessness: despite making changes in his life,\n" + 
              "he is still holding himself back from experiencing true freedom.\n" + 
              "She says that he won't be able to sleep unless he is satisfied with how he spends his waking hours.\n" +
              "When it appears that she has resolved his current worries, Nazuna invites him back to her apartment to share her futon.\n" + 
              "After a while, unaware that he is only feigning unconsciousness, she leans over him—and bites his neck!")
    elif detail == '8':
        os.system('cls')
        print("Jujutsu Kaisen\n")
        print("Genre\t\t: Adventure, Fiction, Dark Fantasy, Supranatural.\n"+
              "Tahun\t\t: 2018\n"+
              "Pengarang\t: Gege Akutami\n"+
              "Status\t\t: on-going\n"+
              "Chapter\t\t: 201\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100034\n")
        print("Yuta Okkotsu gains control of an extremely powerful, " + 
              "cursed spirit and gets enrolled in the Tokyo Prefectural Jujutsu High\n" +
              "School by sorcerers to help him control his power and keep an eye on him.")
    elif detail == '9':
        os.system('cls')
        print("Demon Slayer\n")
        print("Genre\t\t: Adventure, Fiction, Dark Fiction, Martial arts.\n"+
              "Tahun\t\t: 2016\n"+
              "Pengarang\t: Koyoharu Gatouge\n"+
              "Status\t\t: Completed\n"+
              "Chapter\t\t: 205\n"+
              "Link\t\t: https://mangaplus.shueisha.co.jp/titles/100009\n")
        print("A boy raised by boars, who wears a boar's head," + 
              " boards the Infinity Train on a new mission with the Flame Pillar\n" + 
              "along with another boy who reveals his true power when he sleeps.\nTheir mission is to defeat " + 
              "a demon who has tormenting people and killing the demon slayers who oppose it.")
    elif detail == '10':
        os.system('cls')
        print("Yakusoku no Neverland\n")
        print("Genre\t\t: Horror, Mystery, Psychological, Shounen, Supernatural.\n"+
              "Tahun\t\t: 2016\n"+
              "Pengarang\t: Kaiu Shirai\n"+
              "Status\t\t: Completed\n"+
              "Chapter\t\t: 183\n"+
              "Link\t\t: https://mangadex.org/title/46e9cae5-4407-4576-9b9e-4c517ae9298e/yakusoku-no-neverland?tab=chapters&page=3\n")
        print("The escapees find life outside Grace Field House is filled with dangers," + 
              " but under the leadership of Emma and Ray,\n" + 
              "they become determined to return to free their remaining siblings," + 
              "along with children from the other Farms.\n" + 
              "They encounter demons of all descriptions, including Mujika and Sonju who aid them in their quest.\n" + 
              "Emma and Ray later meet up again with Norman and together with their allies,\nthey fight " + 
              "a battle for freedom against the demon queen Legravalima and the human Peter Ratri who manages the Farms." + 
              "Eventually, through her own determination, \nEmma secures the freedom of all the children and re-forges The Promise,\n" +
              "bringing all of them to the human world, but at the cost of her own memory.")
    else:
        os.system('cls')
        trend()
    
    balik = input("\nBack to menu? ")
    if balik == 'y' or 'Y':
        os.system('cls')
        anaconda.main_menu()

def search():
    os.system('cls')
    
    komik = {"action" : "Chainsawman\n"+ 
                        "One Punch Man\n"+
                        "Black Clover\n"+
                        "Spy x Family\n"+
                        "Jujutsu Kaisen\n"+
                        "Demon Slayer\n",
            "fantasy" : "One Piece\n"+
                        "Chainsawman\n"+ 
                        "Black Clover\n"+
                        "Yakusoku no Neverland\n"+
                        "Jujutsu Kaisen\n"+
                        "Demon Slayer\n",
            "romance" : "Kakkou no Iinazuke\n"+
                        "Yofukashi no Uta\n",
            "comedy"  : "One Piece\n"+
                        "One Punch Man\n"+
                        "Black Clover\n"+
                        "Spy x Family\n"+
                        "Kakkou no Iinazuke\n"+
                        "Yofukashi no Uta\n"}
    
    print('\n-- Search manga by genre --\n')
    genre= ["1. Action",
            "2. Fantasy",
            "3. Romance",
            "4. Comedy"]
    
    for i in range(4):
        print(genre[i])
    
    choose = input("\npilih : ")
    if choose == '1':
        os.system('cls')
        print("Action--")
        print(komik["action"])
        back()
      
    elif choose == '2':
        os.system('cls')
        print("Fantasy--")
        print(komik["fantasy"])
        back()
      
    elif choose == '3':
        os.system('cls')
        print("Romance--")
        print(komik["romance"])
        back()
      
    elif choose == '4':
        os.system('cls')
        print("Comedy--")
        print(komik["comedy"])
        back()
      
    else:
        os.system('cls')
        search()

def back():
      b = input('\nback? ')
      if b == 'y' and 'Y':
            os.system('cls')
            anaconda.main_menu()