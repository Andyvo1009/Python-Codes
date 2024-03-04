import random
import vocabulary
import art
word=random.choice(vocabulary.words)
word_count= len(word)
print(art.logo)
arts=art.stages
n=10
lives=5
print("GAME START!")
print("--------------------------------------")
blanks=[]
for i in range(word_count):
  blanks.append("_")
print(blanks)
print("\n"+"\n")
win=True
while(win==True):
  n-=1
  guess= input(str("Enter a letter: "))
  print("--------------------------------------")
  if guess in word:
    temp=0
    for i in range(word_count):
      if word[i]==guess:
        temp+=1
        blanks[i]=guess
    print(f"There are {temp} {guess} in this word")
    
    print(blanks)
    print(f"\n{lives} lives left")
  else:
    lives-=1
    print(arts[lives])
    print("Your guess is wrong")
    print(f"{lives} lives left")
  print("----------------------------------------------")
  if(lives==0): 
    win=False
  if '_' not in blanks:
    break
  
print(f"The answer is {word}")
if(win==False):
  print("YOU LOST")
else:
  print("YOU WON")
print("GAME OVERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
