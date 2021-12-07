answer = input("Would you like to play the game? (yes/no) ")

if answer.lower().strip() == "yes":
    
    print("I am going to be watching you through your impending adventure, and you are going to have to make choices that could be either advantageous or could end up leading to your demise. No pressure though.")
    print("You wake up in the morning to your alarm going off repeatedly. It is time for school")
    answer = input("You're very tired this morning would you like to shower? Yes or no").lower().strip()

    
    if answer == "yes":
        print("Good you passed the first test, at least you're sanitary.")
        answer = input("You walk down the stairs to get some cereal for breakfast. You can either choose between Frosted Flakes or Raisin Bran?").lower().strip()

        if answer == "frosted flakes":
            print("Excellent choice. You were very hungry and you eat 2 whole bowls.")
            print("After your second bowl of Frosted Flakes you begin to feel a little off. Not so much that you're sick but something just isn't right.")
            answer = input("You contemplate telling your mom how you're feeling. Should you tell her? Yes or no").lower().strip()

            if answer == "no":
                print("Instead of telling your mom you grab your backpack and rush out to school.")
                print("On your walk to school you begin to hear these very loud noises like a buzzing or something, but you seem to be the only one hearing it.")
                print("As you walk past angry old Mr. Johnson's house you notice and interesting looking 'thing' in the backyard.")
                print("It looks like a portal but you dismiss it because you don't believe in that kind of stuff.")
                answer = input("Would you like to go investigate? Yes or no").lower().strip()

                if answer == "yes":
                    print("You walk over to the portal to inspect it. As you are looking at in Mr. Johnson yells at you for being on his lawn and are so startled you fall into the portal.")
                    print("As you fall in you are met by some sort of wizard looking person. He tells you his name is Doctor Strange.")
                    print("Yes I am doing a Marvel crossover because I love Marvel. More importanly I technically don't have permission from Disney or Marvel so can we just keep this between us. Thanks")
                    print("Doctor Strange explains to you that you have been chosen to help out the Avengers in one of their battles in alternate universes.")
                    print("You can either go to help in New York 2012 in a universe where Tony doesn't carry the missle into the portal to explode the mother ship,")
                    print("or you can go to Scotland during the events of Infinity War in a universe where Captain America doesn't show up to help Vision and Wanda, and then you could just go back home and go to school")
                    answer = input("So what will it be? New York, Scotland, or home?").lower().strip()

                    if answer == "new york":
                        print("Strange brings you to Stark Tower where you can grab an Iron Man suit if you want.")
                        answer = input("would you like to get into an Iron Man suit to help? Yes or no").lower().strip()

                        if answer == "yes":
                            print("You run and get into one of Starks suits. You are immediately met by Jarvis asking what you're doing.")
                            answer = input("Do you tell him the truth or lie?").lower().strip()

                            if answer == "truth":
                                print("You explain everything as best you can to Jarvis and he actually believes you. He then explains that Tony is going to run out of suit power before carrying the missle fully through the Tesseract portal.")
                                print("You fly in the suit to try and find Tony. Jarvis has already explained to Tony what is happening.")
                                answer = input("At this point you can either 1) try to swap suits with Tony or 2) take the missle yourself leaving Tony.")

                                if answer == "1": #NY successful ending
                                    print("Jarvis directs you to Tony and as he is carrying the missle, your suit flys open dropping you. Tony lets go of the missle and falls out of his suit into yours.")
                                    print("Tonys suit then forms around your body and flys you to a landing spot.")
                                    print("Tony then grabs the missle and flys it up into the portal letting it reach the Chitauri mother ship. He then falls back through the portal and lands on the ground")
                                    print("You and Tony are both congratulated, and afterwards you are returned to your own universe by Doctor Strange. Success! You Win! I totally had faith that you could do it")

                                elif answer == "2": #NY unsuccessful ending
                                    print("You decide you want to take the missle from Tony and blow up the mother ship yourself.")
                                    print("You fly over and grab the missle from Tony just as his suit runs out of power and he falls into the water. Jarvis has given you the trajectory.")
                                    print("However as you go to angle the missle up you missplace your footing and the missle is now on the wrong course. As you're flying up you miss the portal by an inch and then let go.")
                                    print("You fall far down as the missle flys up. You hit the ground as the missle explodes in the air and not a minute later you are cature by Chitauri. Game over.")
                            
                                
                            elif answer == "lie": #2nd losing choice in NY
                                print("You make up a lie to Jarvis and since he is a very complex AI he does not believe you and locks down the other suits which impedes you from helping Tony. The Chitauri go on to take over NY and eventually the entire Earth. Game over")
                                

                        elif answer == "no": #1st losing choice in NY
                            print("Why would you not want to get in a real Iron Man suit? Anyways you instead run through to the Stark Tower window where a wild Chitauri flys through the window hitting you. Game Over.")
                            


                    elif answer == "scotland":
                        print("Doctor Strange takes you to the streets of Scotland where Vision and Wanda are ambushed by the Children of Thanos. How offers you some interesting Wakandan tech to assist you.")
                        answer = input("Would you like to take a ranged or melee weapon?").lower().strip()

                        if answer == "melee":
                            print("With a Wakandan melee weapon you are able to atleast distract the Children of Thanos allowing Wanda to try and heal Vision.")
                            answer = input("After healing Vision, him and Wanda split up and you can choose to follow and assist one of them. Will you follow Wanda or Vision?").lower().strip()

                            if answer == "vision": #Scotland Successful ending
                                print("You run over to help Vision and find that one of the Children of Thanos is trying to take the Mind Stone from him. You strike him and he backs off.")
                                print("Wanda has injured the Child she is fighting and is now regrouped with you and Vision. The Children of Thanos now flee.")
                                print("Vision and Wanda thank you greatly and Doctor Strange returns to send you through a portal back to your own universe.")
                                print("Success! You have won the game!")
                            
                            elif answer == "wanda": #Scotland unsuccessful ending
                                print("You follow Wanda and choose to help her. However Wanda is already very powerful and she is able to fight for herself.")
                                print("You hear that Vision is in trouble and when you go back to help him you find that the Mind Stone has been taken from his head and he is dead. Thanos will now have all 6 infinity stones. Game over.")
                                

                        elif answer == "ranged": #1st losing choice in Scotland
                            print("You show up and begin trying to shoot at the Children of Thanos however you cannot hit them. They evade your attacks and close in and kill you then steal the mind stone from Vision. Game over")
                            

                    elif answer == "home": #5th losing choice
                        print("You tell Strange you want to just go home. He looks at you with disappointment but conjures a new portal back to Mr. Johnson's backyard.")
                        print("You enter the portal and walk back out of the backyard and head to school. It is a boring day of school and you walk home and live your life as normal.")
                    
                elif answer == "no": #4th losing choice
                    print("I really thought you were going to learn from the last times. I'm not even going to make up an idea of what happens next. You lose. I guess you try to play again.")

            elif answer == "yes": #3rd losing choice
                print("She tells you to stay home and you go up to your room and get in bed.")
                print("Like I said earlier you're tired so you end up sleeping the whole day.")
                print("When you wake up you feel fine, but you missed the entire adventure I hinted at in the beginning. So thats lame.")
                print("Game over!")

        elif answer == "raisin bran": #2nd losing choice
            print("How could anyone in their right mind pick raisin bran. You're adventure ends here!")

    elif answer == "no": #1st losing choice
        print("That's gross, you lose. Sorry maybe you should be more sanitary.")

else:
    print("Thats too bad :(")
