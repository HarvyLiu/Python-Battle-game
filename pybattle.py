print("👾Two player Gambling Glitch Battle game👾")
import random
import time
import os
import math
def rollDice(side):
  result = random.randint(1,side)
  return result
def health():
  healthStat = ((rollDice(50)*rollDice(25))/2)+69
  return healthStat
def strength():
  strengthStat = ((rollDice(75)*rollDice(50))/3)+41
  return strengthStat
  
c1Health = round(health())
c1Strength = round(strength())
c2Health = round(health())
c2Strength = round(strength())

def pickSkill(skillNum):
  
  if skillNum == 1:
    print("You used Glitch Step!!!")
    
  elif skillNum == 2:
    print("You used Numeric Blast!!!")
    
  elif skillNum == 3:
    print("You used Null hole!!!")
    
  elif skillNum == 4:
    print("You used Exploitation!!!")
    
  else:
    print("You used your fists because you didnt choose a valid skill!!!")

print("Character Creation:")
print()
c1Name = input("Name your Legend: ")
c1Type = input("Character Type: ")
print()
print(f"{c1Name} the {c1Type}")
c1Title = c1Name + " the " + c1Type


print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()
c2Name = input("Name your Legend: ")
c2Type = input("Character Type: ")
print()
print(f"{c2Name} the {c2Type}")
c2Title = c2Name + " the " + c2Type

print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()
round = 1
winner = None
print("⚔️Battle Time!!!⚔️")
while True:
  time.sleep(5)
  os.system("clear")
  print("⚔️Battle Time!!!⚔️")
  print()
  print(f"{c1Title} current strenth: {c1Strength}\n{c2Title} current strenth: {c2Strength}\n")
  print("The battle begins!\n")
  print(f"{c1Name}'s turn to choose skill ")
  c1skill = int(input("Pick your skill:\n1. Glitch Step (may cause glitches which heals you, and damages enemy)\n2. Numeric Blast (Big blast that causes great damage)\n3. Null hole(Since this hole is extremely unstable, we don't know the effects)\n4. Exploitation (Causes an unpredictable damage number)\n"))
  pickSkill(c1skill)
  print(f"{c2Name}'s turn to choose skill ")
  c2skill = int(input("Pick your skill:\n1. Glitch Step (may cause glitches which heals you, and damages enemy)\n2. Numeric Blast (Big blast that causes great damage)\n3. Null hole(Since this hole is extremely unstable, we don't know the effects)\n4. Exploitation (Causes an unpredictable damage number)\n"))
  pickSkill(c2skill)
  print()
  c1Dmg = c1Strength/100
  c2Dmg = c2Strength/100
  if c1skill == 1:
    c1Dmg += rollDice(15)
    c2Dmg -= rollDice(20)
  elif c1skill == 2:
    c1Dmg += rollDice(30)
  elif c1skill == 3:
    c2Dmg -= rollDice(45)
  elif c1skill == 4:
    c1Dmg = rollDice(100)
  if c2skill == 1:
    c2Dmg += rollDice(15)
    c1Dmg -= rollDice(20)
  elif c2skill == 2:
    c2Dmg += rollDice(30)
  elif c2skill == 3:
    c1Dmg -= rollDice(45)
  elif c2skill == 4:
    c2Dmg = rollDice(100)
  c2Dmg = math.ceil(c2Dmg)
  c1Dmg = math.ceil(c1Dmg)
  c1Health -= c2Dmg
  c2Health -= c1Dmg
  round += 1
  print(f"{c1Title} damage delt: {c1Dmg}\n{c2Title} damage delt: {c2Dmg}\n")
  if c1Health <= 0:
    print(f"{c1Name} has no more health left!")
    print(f"{c2Name} has {c2Health} health left!")
    print(f"{c2Name} the {c2Type} wins in {round} rounds")
    winner = c2Name
    break
 
    
  elif c2Health <= 0:
    print(f"{c1Name} has {c1Health} health left!")
    print(f"{c2Name} has no more health left!")
    print(f"{c1Name} the {c1Type} wins in {round} rounds")
    winner = c1Name
    break
    
  else:
    print("And they're both standing for the next round!!!")
    print(f"{c1Name} has {c1Health} health left!")
    print(f"{c2Name} has {c2Health} health left!")
    print(f"Round {round} is over!")
    continue
    
