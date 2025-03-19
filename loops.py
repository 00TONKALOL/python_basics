for number in range(100):
    if number % 2 != 0:
         print(number)


counter =100
while counter > 0:
   if counter == 99 or counter == 65 or counter == 28:
         counter-=1
         pass #skip
   print(counter)
   counter -= 1
   if counter==35: #increment by 1
        break # terminate