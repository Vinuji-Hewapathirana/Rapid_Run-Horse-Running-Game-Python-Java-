import random

# Creating a list to store horse details
file_path = 'horse_details.txt'  # Assuming this is the path to the file
GROUPS = ['A', 'B', 'C', 'D']
horse_list = []
selected_horses = []
race_times = {}
Race_has_started = False


# Adding horse details
def add_horse_details():
    global horse_list, Race_has_started
    if not Race_has_started:
        while True:
            try:
                horse_id = int(input("Enter Horse ID: "))
                break
            except ValueError:
                print("Enter a valid integer value for Horse ID")
        horse_name = input("Enter Horse Name: ")
        jockey_name = input("Enter Jockey Name: ")
        while True:
            try:
                age = int(input("Enter Age: "))
                break
            except ValueError:
                print("Enter a valid positive integer value for age greater than 0")
        breed = input("Enter Breed of the Horse: ")
        race_record = input("Enter Race Record of the Horse: ")
        while True:
            group_list = ['A', 'B', 'C', 'D']
            group = input("Enter the Group: ").upper()
            if group not in group_list:
                print("Enter a valid group out of", group_list)
            else:
                break

        '#Creating a dictionary for the newly added horse details'
        horse_details = {"Horse ID": horse_id,
                         "Horse Name": horse_name,
                         "Jockey Name": jockey_name,
                         "Age": age,
                         "Breed": breed,
                         "Race Record": race_record,
                         "Group": group}

        horse_list.append(horse_details)
        print("Your horse details are added to the list successfully!\n", horse_list)
    else:
        print("Race has already started!")


# Deleting horse details
def delete_horse_details():
    global horse_list, Race_has_started
    if not Race_has_started:
        if not horse_list:
            print("Cannot delete record as a list of horses doesn't exist")
        else:
            id_horse = int(input("Enter Horse ID needed to be deleted: "))

            for h in horse_list:
                if h["Horse ID"] == id_horse:
                    horse_list.remove(h)
                    print("Horse details of the horse ID were successfully removed!\n", horse_list)
                else:
                    print("Horse ID was not found!")
    else:
        print("Race has already started!")


# Updating horse details
def update_horse_details():
    global horse_list, Race_has_started
    if not Race_has_started:
        if not horse_list:
            print("Cannot update record as a list of horses doesn't exist")
        else:
            id_horse = int(input("Enter Horse ID needed to be updated: "))

            for h in horse_list:
                if h["Horse ID"] == id_horse:
                    print("Enter the details of the horse needed to be updated with horse ID = ", id_horse)
                    while True:
                        try:
                            h["Horse ID"] = int(input("Enter updated Horse ID: "))
                            break
                        except ValueError:
                            print("Enter a valid integer value for the updated Horse ID")
                    h["Horse Name"] = input("Enter updated Horse Name: ")
                    h["Jockey Name"] = input("Enter updated Jockey Name: ")
                    while True:
                        try:
                            h["Age"] = int(input("Enter updated Age: "))
                            break
                        except ValueError:
                            print("Enter a valid positive integer value for age greater than 0")
                    h["Breed"] = input("Enter updated Breed of the Horse: ")
                    h["Race Record"] = input("Enter updated Race Record of the Horse: ")
                    while True:
                        group_list = ['A', 'B', 'C', 'D']
                        h["Group"] = input("Enter the updated Group: ").upper()
                        if h["Group"] not in group_list:
                            print("Enter a valid group out of", group_list)
                        else:
                            break
                    print("Your new horse details are updated successfully!\n", horse_list)
                else:
                    print("Horse ID was not found!")
    else:
        print("Race has already started!")


# Viewing horse details
# Bubble sort
def bubble_sort():
    global horse_list
    if not horse_list:
        print("Cannot execute as a list of horses doesn't exist")
    else:
        for i in range(0, len(horse_list) - 1):
            for j in range(len(horse_list) - 1):
                if horse_list[j]["Horse ID"] > horse_list[j + 1]["Horse ID"]:
                    horse_list[j], horse_list[j + 1] = horse_list[j + 1], horse_list[j]


def view_sorted_list():
    global horse_list
    if not horse_list:
        print("Cannot execute as a list of horses doesn't exist")
    else:
        bubble_sort()
        print("\nRegistered horses sorted by horse ID: ")
        for h in horse_list:
            print(h)


# Saving the details into a file
# Arranging horse list according to the groups
def save_to_text_file():
    global horse_list
    group_horse = {}
    if not horse_list:
        print("Cannot execute as a list of horses doesn't exist")
    else:
        for h in horse_list:
            group = h["Group"]
            if group not in group_horse:
                group_horse[group] = []
            group_horse[group].append(h)

        # Saving into the file
        f = open(file_path, 'w')
        for group, g in group_horse.items():
            f.write(f"\nGroup{group}:\n")
            for h in g:
                f.write(str(h) + "\n")
        f.close()

        fr = open(file_path, 'r')
        print(fr.read())
        fr.close()
        print("Horse details have been saved to the file successfully!")


# Function to select horses
def selection_for_major_round():
    global horse_list, selected_horses, file_path

    try:
        if not horse_list:
            print("No horses registered. Cannot select.\n")
        else:
            file = open(file_path, 'r')
            key = None  # Initialize key outside the loop
            value = None  # Initialize value outside the loop
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 2:
                        key, value = parts[0], ' '.join(parts[1:])
                        key = key.strip()
                        value = value.strip()
                    if key == 'Group':
                        horse_list.append({'Group': value})
                    else:
                        horse_list[-1][key] = value
            file.close()
    except ValueError as ve:
        print(f"Error adding horse details: {ve}\n")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}\n")
    except Exception as e:
        print(f"Error loading horse details: {e}\n")
        return

    final_round_horses = {}

    try:
        for group in GROUPS:
            group_horses = [horse for horse in horse_list if horse.get('Group') == group]
            if group_horses:
                selected_horse = random.choice(group_horses)
                final_round_horses[group] = selected_horse
    except Exception as e:
        print(f"Error selecting final round horses: {e}\n")
        return

    if len(final_round_horses) == len(GROUPS):
        selected_horses = final_round_horses
        print("\nFinal Round Horses:")
        for group, horse in final_round_horses.items():
            print(f"Group {group}: {horse.get('Horse Name')} (Horse ID: {horse.get('Horse ID')})")
        print("\nFinal round horses selected successfully!\n")
    else:
        print("Not enough horses in each group to select final round horses.\n")


# Function to display winning horse details
def display_winners():
    global selected_horses, race_times

    if selected_horses:
        race_times = {}

        for group, horse in selected_horses. items():
            race_time = random.randint(10, 90)
            race_times[horse['Horse ID']] = race_time

        print("\nRace Times for Final Round Horses:")
        for horse_id in race_times:
            print(f"Horse ID: {horse_id}, Time: {race_times[horse_id]} seconds")

        sorted_horses = list(race_times.items())
        n = len(sorted_horses)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if sorted_horses[j][1] > sorted_horses[j + 1][1]:
                    sorted_horses[j], sorted_horses[j + 1] = sorted_horses[j + 1], sorted_horses[j]

        print("\nWinners:")
        for i in range(min(3, len(sorted_horses))):
            horse_id, time = sorted_horses[i]
            horse = None
            for h in selected_horses.values():
                if h['Horse ID'] == horse_id:
                    horse = h
                    break
            if horse:
                print(f"{i + 1} Place: {horse['Horse Name']} (Horse ID: {horse['Horse ID']}), Time: {time} seconds")

    else:
        print("No final round horses selected. Please run 'SDD' to select horses for the final round.\n")


# Function to visualize winning horses
def visualizing_winner(race_times):
    global selected_horses

    if selected_horses and race_times:
        print("\nVisualization of Time Spent by Winning Horses:")

        sorted_horses = list(race_times.items())

        n = len(sorted_horses)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_horses[j][1] > sorted_horses[j+1][1]:
                    sorted_horses[j], sorted_horses[j+1] = sorted_horses[j+1], sorted_horses[j]

        i = 0
        while i < 3 and i < len(sorted_horses):
            horse_id, time = sorted_horses[i]
            horse = None
            for h in selected_horses.values():
                if h['Horse ID'] == horse_id:
                    horse = h
                    break
            if horse:
                stars = '*' * (time // 10)
                print(f"{horse['Horse Name']}:  {stars:<20} {time}s ({i + 1}st Place)")
            i += 1

    else:
        print("No final round horses selected. Please run 'SDD' to select horses for the final round.\n")


# Function to start the race
def starting_status_of_the_race():
    global Race_has_started
    if not Race_has_started:
        print("Race starting!!\n")
        Race_has_started = True
    else:
        print("Race has already started!\n")


# Instructions for the user
def rapid_run():
    while True:
        print("Rapid Run Horse Management\n"
              "Type AHD to add horse details\n"
              "Type DHD to delete horse details\n"
              "Type UHD to update horse details\n"
              "Type VHD to view registered horse details table\n"
              "Type SHD to save horse details to a text file\n"
              "Type SDD to select horses for the major round\n"
              "Type WHD to display winning horses' details\n"
              "Type VWH to visualize the time of winning horses\n"
              "Type SR to start the race\n"
              "Type ESC to exit program\n")

        command = input("Enter your command: ").upper()

        if command == "AHD":
            add_horse_details()
        elif command == "DHD":
            delete_horse_details()
        elif command == "UHD":
            update_horse_details()
        elif command == "VHD":
            view_sorted_list()
        elif command == "SHD":
            save_to_text_file()
        elif command == "SDD":
            selection_for_major_round()
        elif command == "WHD":
            display_winners()
        elif command == "VWH":
            visualizing_winner(race_times)
        elif command == "SR":
            starting_status_of_the_race()
        elif command == "ESC":
            print("Exit")
            break
        else:
            print("Please enter a valid command!")


rapid_run()
