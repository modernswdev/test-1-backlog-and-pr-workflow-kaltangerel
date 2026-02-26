# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

#Fix

SECRET_CODE = "replace_code"

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  if (b_hp <= 0):
      print("The Boss is already defeated!")
      return
  else:
      b_hp -= 10
      print("You deal 10 damage!")
  

def heal():
  global p_hp
  if (p_hp < 50 and p_hp > 0):
      p_hp += 20
      print(f"Healed! HP is now {p_hp}")
  elif (p_hp >= 50):
      print(f"HP is full!")
  

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()
  
  while True:
    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    elif choice == 'c':
        if input("Code: ") == SECRET_CODE:
            b_hp = 0
        break
    else:
        print(f"Invalid Input. Try again.")

  if b_hp > 0:
    p_hp -= 10

if p_hp <= 0:
    print("victory!")
elif b_hp <= 0:
    print("Defeat!")