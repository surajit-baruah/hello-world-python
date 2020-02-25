import random

def getAnswer(answerNumber):
   if answerNumber == 1:
      return 'Yes'
   elif answerNumber == 2:
      return 'No'

r = random.randint(1,2)
fortune = getAnswer(r)
print (fortune)
