class Room:
    def __init__(self, description='', north=0, east=0, south=0, west=0, up=0, down=0):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down

class Item:
    def __init__(self, name, description, room):
        self.name = name
        self.description = description
        self.room = room

def main():
    room_list = []
    item_list = []

    # Creating rooms
    room_list.append(Room("Bedroom. You are now here. There are passages to the north, east and downward.", 1, 5, None, None, None, 8 ))
    room_list.append(Room("West Hall. There are passages to north, east, south and west.", 2, 4, 0, 6))
    room_list.append(Room("Kitchen. There are passages to the south, east and downward.", None, 3, 1, None, None, 10))
    room_list.append(Room("Dining room. There is a passage to the west, south and downward.", None, None, 4, 2))
    room_list.append(Room("East Hall. There are passages in all directions, except upward.", 3, 7, 5, 1, None, 9))
    room_list.append(Room("Kids room. There is a passage to the west, north and downward.", 4, None, None, 0))
    room_list.append(Room("West balcony. There is a passage to the east.", None, 1))
    room_list.append(Room("East balcony. There is a passage to the west.", None, None, None, 4))

    # Creating basement rooms
    room_list.append(Room("Swimming Pool. There are passages to north and upward.", 9, None, None, None,  5))
    room_list.append(Room("Game Zone.There are passages to north, south and upward .", 10, None, 8, None, 1, ))
    room_list.append(Room("Fitness Hall. There are passages to south and upward.", None, None, 9, None, 3 ))

    # Creating items
    item_list.append(Item("key", "A small rusty key lies here.", 6))
    item_list.append(Item("sword", "A gleaming sword is mounted on the wall.", 3))
    item_list.append(Item("lantern", "There's a lantern here that might be useful.", 8))

    current_room = 0

    done = False
    while not done:
        print("\n" + room_list[current_room].description)

        # Display items in the room
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        command = input("What do you want to do? (N, E, S, W, U, D, get [item], inventory, or Q to quit): ").strip().lower().split()

        if len(command) == 1:
            if command[0] == 'n':
                next_room = room_list[current_room].north
            elif command[0] == 'e':
                next_room = room_list[current_room].east
            elif command[0] == 's':
                next_room = room_list[current_room].south
            elif command[0] == 'w':
                next_room = room_list[current_room].west
            elif command[0] == 'u':
                next_room = room_list[current_room].up
            elif command[0] == 'd':
                next_room = room_list[current_room].down
            elif command[0] == 'q':
                print("Goodbye!")
                done = True
                continue
            else:
                print("I don't understand that command.")
                continue

            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif len(command) > 1:
            cmd, item_name = command[0], " ".join(command[1:])
            if cmd == "get":
                found = False
                for item in item_list:
                    if item.name == item_name and item.room == current_room:
                        item.room = -1
                        print(f"You picked up the {item.name}.")
                        found = True
                        break
                if not found:
                    print("You can't find that here.")
            elif cmd[0] == "inventory":
                has_items = False
                for item in item_list:
                    if item.room == -1:
                        print(f"You have a {item.name}.")
                        has_items = True
                if not has_items:
                    print("You are carrying nothing.")
            else:
                print("I don't understand that command")
        if all(item.room == -1 for item in item_list):  # Check if all items are collected
            print("Congratulations! You have found all the items. Game Over!")
            break
if __name__ == "__main__":
    main()
