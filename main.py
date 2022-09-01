# ------------------------------------------
#everything that the program needs is imported from here
import test
import startup
import loadinganimation
import replit
#-------------------------------------------
startup.startsequence() #displays the startup sequence on the terminal to the user

question = input('Start the new code test? y/n: ') #when their is new code needing to be test
if question == "y":
    loadinganimation.loadinganim() #shows user the beutiful loading animation while giving the code time to load
    test.testfunction()
    

else:
  print('New code test skipped, started program normally')
  for i in range(3):
  
    loadinganimation.loadinganim()
  replit.clear()
  print('haha their is nothing here yet')
























