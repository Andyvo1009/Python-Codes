import random
words = "ape cat dog baboon elephant giraffe apple coconut monkey rubik mice mouse pineapple android apple house fence python grail zerg protoss terran llama fire policeman mamerto smad zebra lion luffy nigga universidad".split()
word=words[random.randint(0,len(words)-1)]
word_count= len(word)
n=10
lives=5
print("GAME START!")
print("--------------------------------------")
blanks=[]
for i in range(word_count):
  blanks.append("_")
for i in range(word_count):
  print(blanks[i],end= " ")
win=True
while(win==True):
  n-=1
  guess= input(str("\nEnter a letter: "))
  print("--------------------------------------")
  if guess in word:
    temp=0
    for i in range(word_count):
      if word[i]==guess:
        temp+=1
        blanks[i]=guess
    print(f"There are {temp} {guess} in this word")
    for i in range(word_count):
      print(blanks[i],end= " ")
    print(f"\n{lives} lives left")
  else:
    lives-=1
    print("Your guess is wrong")
    print(f"{lives} lives left")
  print("----------------------------------------------")
  if(lives==0): 
    win=False
  if '_' not in blanks:
    break
  
  
if(win==False):
  print("LOST")
else:
  print("WIN")
print("GAME OVERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
