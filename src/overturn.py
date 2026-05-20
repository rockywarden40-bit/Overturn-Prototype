# --- imports ---
import time
import random
import tkinter as tk
from endings import save_ending


# --- classes ---
class Character:
    def __init__(self, name, health, max_hp, level, damage):
        self.name = name
        self.health = health
        self.max_hp = max_hp
        self.level = level
        self.damage = damage
        self.inventory = (
            []
        )  # This system is currently unused in this game but does exist for future


# --- special name functions ---
def sus_name():
    print("What... You aren't worthy of entering")
    print("Ending Unlocked: Sus Ending")
    save_ending("Sus Ending")


def waterloo_name():
    return pName()


special_names = {"sus": sus_name, "waterloo": waterloo_name}


# --- start-up ---
def pName():
    name = input("Enter your name: ")
    name_lower = name.lower()

    if name == "":
        print("Please enter a valid name.")
        return pName()

    elif name_lower in special_names:
        return special_names[name_lower]()

    else:
        confirm = input(f"Are you sure you want to be called {name}? (y/n) ").lower()

        if confirm == "y":
            print(f"Your journey begins now, {name}...")
            return name
        else:
            return pName()


# --- defualt player set-up ---
name = pName()
player = Character(name, 20, 20, 1, 5)

# --- ending deciding variables ---
killed = 0
spared = 0
Emru_killed = False

# --- first room ---
# The first room will always be the same that is why it is categorized as "--- first room ---" , all other rooms will have random enemies (except room 6)
print("Room 1... Just a normal room...")
time.sleep(2)


def ribbit():
    Ribbit = Character("Ribbit", 15, 15, 1, 1)

    print("Ribbit attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Ribbit HP: {Ribbit.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Ribbit.health -= player.damage
            print(
                f"You attack Ribbit! He loses {player.damage} HP and now has {Ribbit.health} HP left."
            )
            time.sleep(1)

            # Check if Ribbit dies
            if Ribbit.health <= 0:
                killed += 1
                print("You have killed Ribbit!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Ribbit attacks back
            player.health -= Ribbit.damage
            print(
                f"Ribbit attacks back! You lose {Ribbit.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Ribbit!")
            break

        else:
            print("Invalid input, try again.")


ribbit()


# --- enemy list and system ---
def catsy():
    Catsy = Character("Catsy", 20, 20, 2, 1)

    print("Catsy attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Catsy HP: {Catsy.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Catsy.health -= player.damage
            print(
                f"You attack Catsy! He loses {player.damage} HP and now has {Catsy.health} HP left."
            )
            time.sleep(1)

            # Check if Catsy dies
            if Catsy.health <= 0:
                Catsy.health = 0
                killed += 1
                print("You have killed Catsy!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Catsy attacks back
            player.health -= Catsy.damage
            print(
                f"Catsy attacks back! You lose {Catsy.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Catsy!")
            break

        else:
            print("Invalid input, try again.")


def mew():
    Mew = Character("Mew", 25, 25, 3, 2)

    print("Mew attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Mew HP: {Mew.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Mew.health -= player.damage
            print(
                f"You attack Mew! He loses {player.damage} HP and now has {Mew.health} HP left."
            )
            time.sleep(1)

            # Check if Mew dies
            if Mew.health <= 0:
                Mew.health = 0
                killed += 1
                print("You have killed Mew!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Mew attacks back
            player.health -= Mew.damage
            print(
                f"Mew attacks back! You lose {Mew.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Mew!")
            break

        else:
            print("Invalid input, try again.")


def eggy():
    Eggy = Character("Eggy", 20, 20, 2, 1)

    print("Eggy attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Eggy HP: {Eggy.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Eggy.health -= player.damage
            print(
                f"You attack Eggy! He loses {player.damage} HP and now has {Eggy.health} HP left."
            )
            time.sleep(1)

            # Check if Eggy dies
            if Eggy.health <= 0:
                Eggy.health = 0
                killed += 1
                print("You have killed Eggy!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Eggy attacks back
            player.health -= Eggy.damage
            print(
                f"Eggy attacks back! You lose {Eggy.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Eggy!")
            break

        else:
            print("Invalid input, try again.")


def blade():

    Blade = Character("Blade", 30, 30, 4, 3)

    print("Blade attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Blade HP: {Blade.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Blade.health -= player.damage
            print(
                f"You attack Blade! He loses {player.damage} HP and now has {Blade.health} HP left."
            )
            time.sleep(1)

            # Check if Blade dies
            if Blade.health <= 0:
                Blade.health = 0
                killed += 1
                print("You have killed Blade!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Blade attacks back
            player.health -= Blade.damage
            print(
                f"Blade attacks back! You lose {Blade.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Blade!")
            break

        else:
            print("Invalid input, try again.")


def jeper():
    Jeper = Character("Jeper", 35, 35, 5, 4)

    print("Jeper attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Jeper HP: {Jeper.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Jeper.health -= player.damage
            print(
                f"You attack Jeper! He loses {player.damage} HP and now has {Jeper.health} HP left."
            )
            time.sleep(1)

            # Check if Jeper dies
            if Jeper.health <= 0:
                Jeper.health = 0
                killed += 1
                print("You have killed Jeper!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Jeper attacks back
            player.health -= Jeper.damage
            print(
                f"Jeper attacks back! You lose {Jeper.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Jeper!")
            break

        else:
            print("Invalid input, try again.")


def Wraith():

    Wraith = Character("Wraith", 40, 40, 6, 5)

    print("Wraith attacks you!")
    time.sleep(2)

    global killed
    global spared

    while True:
        print(f"Your HP: {player.health}")
        time.sleep(1)
        print(f"Wraith HP: {Wraith.health}")
        time.sleep(1)

        choice = input("Do you Attack or Spare? ").lower()

        if choice == "attack":
            # Player attacks
            Wraith.health -= player.damage
            print(
                f"You attack Wraith! He loses {player.damage} HP and now has {Wraith.health} HP left."
            )
            time.sleep(1)

            # Check if Wraith dies
            if Wraith.health <= 0:
                Wraith.health = 0
                killed += 1
                print("You have killed Wraith!")
                player.level += 1
                player.max_hp += 5
                player.health = player.max_hp
                player.damage += 1

                print(f"You're level increased to {player.level}.")
                time.sleep(1)
                print(
                    f"Your stats have increased \nHP: {player.health} \nDamage: {player.damage}"
                )
                time.sleep(2)

                break

            # Wraith attacks back
            player.health -= Wraith.damage
            print(
                f"Wraith attacks back! You lose {Wraith.damage} HP and now have {player.health} HP."
            )
            time.sleep(1)

            # Check if player dies
            if player.health <= 0:
                print("You died...")
                break

        elif choice == "spare":
            spared += 1
            print("You spared Wraith!")
            break

        else:
            print("Invalid input, try again.")


enemy_list = [catsy, mew, eggy, blade, jeper, Wraith]
enemy = random.choice(enemy_list)

print("Room 2... A new enemy approaches...")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 3... Catsy and Mew are twins btw...")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 4... You are still alive...")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 5... Something is wrong... Its coming from room 6...")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()


def emru():

    global Emru_killed, spared, killed

    print("Emru appears.")
    time.sleep(1)

    choice = input("Fight or Spare? ").lower()

    if choice == "spare":
        print("Emru: You spare Emru... He suddenly disappears")
        spared += 1
        return

    # --- Forced fight ---
    print("Emru: Look at your health")
    player.health = 1
    print(player.health)

    time.sleep(2)
    print("Try attacking me or spare, doesn't matter")
    time.sleep(1)

    # --- First phase ---
    choice = input("Attack or Spare? ").lower()

    if choice == "attack":
        print("0 damage dealt")
        time.sleep(2)

        print("Emru: Don't you know me?")
        print("Emru: Time for my final attack")
        time.sleep(2)

        print("Attack failed")
        time.sleep(2)

        print("Emru: What")
        time.sleep(2)
        print("Emru: How did you do that?")
        time.sleep(2)

        # --- Final phase ---
        choice = input("Attack or Attack? ").lower()

        print("Damage dealt: 10000000")
        print("Emru: How did...")
        time.sleep(2)

        print("Emru: This wasn't your attack right...")
        time.sleep(2)

        print("Emru: There is no way it was...")
        time.sleep(2)

        print("Emru: His attack...")
        print("Emru Deleted from file")

        Emru_killed = True
        killed += 1

        print("You killed Emru!")
        print("Your level...")
        time.sleep(2)
        player.health = player.max_hp
        print("didn't increase?")

    elif choice == "spare":
        print("Emru: Spare me? What an IDIOT")
        time.sleep(2)

        player.health = 0
        print("You died... Ha Ha Ha... Only if this happened with him as well")
        time.sleep(2)
        print("An unknown presence prevents your death")
def secret_room_event():
    chance = random.random()

    if chance > 0.1:
        return  # 90% → nothing happens

    print("\n...")
    time.sleep(1)
    print("A strange door appears.")
    time.sleep(1)

    choice = input("Do you want to open it? (yes/no): ").lower()

    if choice != "yes":
        print("You ignore it.")
        return

    print("You open the door...")
    time.sleep(2)

    # --- TKINTER WINDOW ---
    root = tk.Tk()
    root.title("???")
    root.geometry("600x400")

    label = tk.Label(root, text="", font=("Consolas", 24))
    label.pack(expand=True)

    states = [
        ("What is happening", "red", "black"),
        ("7h15 c4n7 b3 17", "black", "red"),
        ("☟ ✌💣 🕈✌❄☜☼☹⚐⚐", "red", "black")  # Wingdings
    ]

    index = 0

    def glitch():
        nonlocal index

        text, bg, fg = states[index]
        root.configure(bg=bg)
        label.configure(text=text, bg=bg, fg=fg)

        index += 1

        if index < len(states):
            root.after(1500, glitch)
        else:
            root.after(2000, root.destroy)

    glitch()
    root.mainloop()

    # --- ENDING ---
    print("...")
    time.sleep(1)
    print("You witness something strange, you weren't supposed to see this.")

    save_ending("Secret Ending")

print("Room 6... You feel an overwhelming presence coming from here...")
time.sleep(2)
emru()

print(
    "Room 7... You have made it this far... But you feel like something is missing..."
)
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 8... You feel like Your journey is almsot over")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 9... You feel the presence of an exit")
time.sleep(2)
enemy = random.choice(enemy_list)
enemy()

print("Room 10... The exit")
time.sleep(2)
print("You aren't attacked this time")
print("You are judged")

# --- SPECIAL ENDINGS FIRST ---

# Massacre Ending (killed everyone)
if spared == 0 and killed > 0:
    print("You killed everyone... I don't blame you... You made the right choice...")
    print("Ending Unlocked: Massacre Ending")
    save_ending("Massacre Ending")

#True Ending (killed only Emru)
elif killed == 1 and Emru_killed == True:
    print("You only killed Emru... You are a true hero...")
    print("Ending Unlocked: True Ending")
    save_ending("True Ending")

# Pacifist Ending (spared everyone)
elif killed == 0 and spared > 0:
    print("You spared everyone... Why?")
    print("Ending Unlocked: Pacifist Ending")
    save_ending("Pacifist Ending")

# Puppet Ending (killed all except Emru)
elif spared == 1 and Emru_killed == False:
    print("You killed everyone but Emru... Are you working for him?")
    print("Ending Unlocked: Puppet Ending")
    save_ending("Puppet Ending")

# --- GENERAL ENDINGS ---

# Killer Ending
elif killed > spared:
    print("You killed more than you spared...")
    print("Ending Unlocked: Killer Ending")
    save_ending("Killer Ending")

# Dark Heart Ending 
else:
    print("You spared some... yet you still killed some...")
    print("Ending Unlocked: Dark Heart Ending")
    save_ending("Dark Heart Ending")