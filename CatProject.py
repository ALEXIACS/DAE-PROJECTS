catWetFoodList = ["Small Human-Grade Fresh Cat Food", "Tiki Cat Emma Luau Variety Pack","Wellness Complete Health Kitten Formula","Purina Pro Plan Prime Plus Adult 7+","","","","","",""]
catDryFoodList = ["Hill's Science Diet Adult Chicken Recipe", "Open Farm Homestead Turkey & Chicken", "Orijen Original Recipe High-Protein Cat Food", "Purina Beyond: Wild-Caugh Whitefish and Cage-Free Egg Recipe", "Blue Buffalo Chicken Recipe", "Made by Nacho"]
while True: 
  userName = input ("Hi! What is your name? ")
  print ("Hi! " + userName)
  answer1 = input(" Do you have a cat? (y/n)  ") .lower()
  if answer1 == 'y':
# If user has a Cat, then ask Cat's name
    answer = input ("What is your cat's name??! ")
    print ( answer + "?  What a beautiful name!!" )
    answer3 = input ("Is it your first cat? (y/n)  ")
    if answer3 == 'y':
      print ("Oh, nice, here we will teach you everything you need to know to take good care of your cat! Like what food is good depending on the cat's age, or what the cat's need to have a helthy life!!")
# If user has a Cat, Cat's age
    answer2 = input(" Is it a kitten? (y/n) ") .lower()
    if answer2 == 'y': 
      answer3 = input("How months old is your cat? (answer in #)  ")
      young = '1'
      adult = '12'
      if answer3 <= adult:
        print ("Awww, so young")
#To complete !! make a list of cat food brands for kittens and nutritional value, 
# ask if the cat has fur, if not make a list of products for skin, else list products to prevent cat vomits
      print("Hi! " + userName + " ")
      import webbrowser
      url1 = "https://www.amazon.com/Healthy-Kitten-Food/s?k=Healthy+Kitten+Food"
      webbrowser.open(url1)
      break
    else:
# To complete !! Make a list of cat food brands for adult cats and what they need
# ask if the cat has fur, if not make a list of products for skin, else list products to prevent cat vomits.
      print("We will redirect you to your preferences!!! ")
      import webbrowser
      url2 = "https://www.amazon.com/Healthy-Cat-Food/s?k=Healthy+Cat+Food"
      webbrowser.open(url2)
      break
  else:
    print ("Then why are you searching for cat food??! ")
  answer2 = input ("Are you planning on having a cat??  (y/n)  ") .lower ()
  if answer2 == 'n':
    print ("Oh! so the page will close automatically")
    print ("Closing...")
    print("...")
    break
  else:
    print("Oh! ok so...")
#redirect to line 4
