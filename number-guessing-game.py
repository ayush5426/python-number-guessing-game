import random
print("---WELCOME TO GUESS THE NUMBER GAME---")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}
while True:
     a = int(input("GUESS THE NUMBER CHOOSEN BY THE BOT. HINT: NUMBER IS FROM 1 TO 50 :"))
     b = int(random.choice(list(numbers)))

     if(a > 50 or a < 1):
          print("DONT YOU KNOW WHAT COMES IN FROM 1 TO 50. ARE YOU DUMB?")
          continue
     you = print("THE NUMBER YOU CHOSE IS:", a)
     bot = print("THE NUMBER CHOOSEN BY BOT IS:", b)
     if(a == b):
          print("CONGRATULATIONS!! YOU GUESSED IT RIGHT.")
          break
     else:
          print("BAD LUCK.YOU CHOSE A DIFFERENT NUMBER.")
     
     choice = input("\nPress Enter to try again or 'Q' then Enter to Leave...")
     if (choice == 'Q'):
          exit()
     elif(choice == 'q'):
          exit()
input("\nPress Enter to exit...")