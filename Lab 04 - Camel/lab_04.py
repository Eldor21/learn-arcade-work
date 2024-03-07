import random


def main():
  done = False
  miles_traveled = 0
  hunger = 0
  horse_tiredness = 0
  distance_zombies = -20
  foods_in_bag = 3

  while not done:
    random_num = random.randint(7, 14)
    random_move = random.randint(10, 20)
    random_go_ahead = random.randint(5, 12)
    random_horse_tiredness = random.randint(1, 3)
    random_oasis = random.randint(1, 20)

    print(
        "\nA. Eat from your bag.\nB. Ahead half of speed.\nC. Ahead full speed.\nD. Stop for rest in safe place.\nE. Status check.\nQ. Quit."
    )
    choice = input("What is your choice? ").upper()

    if choice == "Q":
      done = True
      print("\nGame Over\n")

    elif choice == "E":
      print(
          f"\nMiles traveled: {miles_traveled}\nFoods in bag: {foods_in_bag}\nHunger level: {hunger}\nHorse Tiredness: {horse_tiredness}\nThe zombies are {abs(miles_traveled - distance_zombies)} miles behind you.\n"
      )

    elif choice == "D":
      horse_tiredness = 0
      print("\nHorse is happy!\n")
      distance_zombies += random_num

    elif choice == "C":
      miles_traveled += random_move
      print(f"\nYou traveled {random_move} miles\n")
      hunger += 1
      horse_tiredness += random_horse_tiredness
      distance_zombies += random_num

    elif choice == "B":
      miles_traveled += random_go_ahead
      print(f"\nYou traveled {random_go_ahead} miles\n")
      hunger += 1
      horse_tiredness += 1
      distance_zombies += random_num

    elif choice == "A":
      if foods_in_bag > 0:
        foods_in_bag -= 1
        hunger = 0
        print("\nYou ate food from your bag.\n")
      else:
        print("\nYou have no food left!\n")

    if hunger > 4:
      print("\nYou are hungry!\n")
      done = True
      print("You starved to death")
    if horse_tiredness > 5:
      print("\nYour horse is getting tired!\n")
      done = True
      print("Your horse died of exhaustion")
    if miles_traveled >= 200:
      done = True
      print("\nCongratulations! You survived\n")

    if random_oasis == 17:
      print(
          "\nYou found an oasis! Your bag is refilled, and your horse is rested.\n"
      )
      foods_in_bag = 3
      horse_tiredness = 0

    if distance_zombies >= miles_traveled:
      print("\nThe zombies caught up to you!\n")
      done = True
    elif distance_zombies + 14 > miles_traveled:
      print("\nHurry up, The zombies are getting closer!\n")

  print("\nGame Over\n")


main()