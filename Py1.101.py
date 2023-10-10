while True: 
  userName = input ("Hi! What is your name? ")
  print ("Hi! " + userName)
  answer = input("Would you like to study? (◍＞◡＜◍) (y/n)  ") .lower()
  if answer == 'y':
#simulating loading bar / will be added later <<never>> ᕕ( ಠ‿ಠ)ᕗ
    print ("PREPARING MATERIALS...")
    print ("Redirecting...")
    print ("...")
    print ("redirecting")
    import webbrowser
    url= "https://www.khanacademy.org/science/ms-biology"
    webbrowser.open(url)
    break
  else:
    print("You'll get bad grades ಠ╭╮ಠ ")
    answer3 = input("Do you want to proceed? ¯\_(ツ)_/¯ ? (y/n) ") .lower()
    if answer3 == 'y':
       print (" (ノಠ益ಠ)ノ彡┻━┻   ... hehehe... You will not scape") 
       line_number = 4
