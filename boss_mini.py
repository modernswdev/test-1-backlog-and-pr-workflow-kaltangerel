# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Store the secret somewhere else. Do not push the key to Git as this will
# raise security vulnerability 
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# This attack function needs to subtract from b_hp in order to progress the game.
# Currently, it does not take away HP
def attack():
  global b_hp
    print("You deal 10 damage!") # Indentation is wrong infront of this statement

# This function needs validation logic to make sure the player do not overheal past 50.
def heal():
  global p_hp
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0: 
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
    # This variable needs to be global. Otherwise, the variable will not be updated.
      b_hp = 0
# Needs else statement to inform the user that their input is wrong.
  
# The boss shouldn't attack if the input is wrong
  if b_hp > 0:
    p_hp -= 10

# Needs extra if/else statements to determine the game results.
print("Game Over!")