# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Removed security backend vulnerability - hard-coded secret password

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  b_hp -= 10    # Added code to actually deal damage to boss HP
  print("You deal 10 damage!")    # Removed extra indent

def heal():
  global p_hp
  if p_hp < 50:
    p_hp += 20
    if p_hp > 50:   # Added code to ensure no over-healing
      p_hp = 50
    print(f"Healed! HP is now {p_hp}")
  elif p_hp <= 0:   # Added code to ensure no healing after defeat
    print:(f"Already defeated!")
  else:
    print(f"Already healthy!")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

  choice = ''   # Resets 'choice' variable before selection loop
  while choice != 'a' and choice != 'h':    # Added logic to ensure only appropriate options are selected
    choice = input("Action [a]ttack, [h]eal: ").lower()   # Removed cheat code logic

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  # Removed cheat code logic
  
  if b_hp > 0:
    p_hp -= 10

  if b_hp <= 0:   # Added victory condition
    print("You won!")
  
  if p_hp <= 0:   # Added loss condition
    print("You were defeated!")



print("Game Over!")   # Additional ending text is optional and can be removed at developer's discretion; kept to improve clarity that the game is completed
