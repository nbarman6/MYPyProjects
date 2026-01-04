import os

def create_folders(count, main_folder):
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)

    for i in range(1, count + 1):
        folder_path = os.path.join(main_folder, str(i))
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    print(f"{count} folders created successfully.\n")

# -------- MAIN PROGRAM --------
while True:
    print("===== Folder Creator =====")
    print("1. Create folders")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        try:
            num = int(input("How many folders do you want to create? : "))
            if num <= 0:
                print("Enter a positive number only.\n")
                continue

            folder_name = input("Enter main folder name: ")
            create_folders(num, folder_name)

        except ValueError:
            print("Invalid input. Enter numbers only.\n")

    elif choice == "2":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.\n")
