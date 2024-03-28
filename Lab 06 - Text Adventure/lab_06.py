class Room:
    def __init__(self, description='', north=0, east=0, south=0, west=0):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []

    # Creating rooms
    room0 = Room("Bedroom. You are now here. There are passages to the north and east.", 1, 5, None, None)
    room_list.append(room0)

    room = Room("West Hall. There are passages in all directions.", 2, 4, 0, 6)
    room_list.append(room)

    room = Room("Kitchen. There are passages to the south and east.", None, 3, 1, None)
    room_list.append(room)

    room = Room("Dining room. There is a passage to the west and south.", None, None, 4, 2)
    room_list.append(room)

    room = Room("East Hall. There are passages in all directions.", 3, 7, 5, 1)
    room_list.append(room)

    room = Room("Kids room. There is a passage to the west and north.", 4, None, None, 0)
    room_list.append(room)

    room = Room("West balcony. There is a passage to the east.", None, 1, None, None)
    room_list.append(room)

    room = Room("East balcony. There is a passage to the west.", None, None, None, 4)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()
        print(room_list[current_room].description)

        user_input = input("What do you want to do? (N, E, S, W, or Q to quit): ").strip().upper()

        if user_input == 'N':
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input == 'E':
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input == 'S':
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input == 'W':
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input == 'Q':
            print("Goodbye!")
            done = True
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()
