items = []
def show(lst):
    if not lst:
        print("Current list is empty. ")
    else:
        print("Current list:")
        for index, value in enumerate(lst):
            print(f"{index}. {value}")

def insert_element(lst):
    value = input("Enter value to insert: ")
    lst.append(value)
    show(lst)

def delete_by_value(lst):
    value = input("Enter value to delete: ")
    if value in lst:
        lst.remove(value)
    else:
        print("value not found.")
    show(lst)

def delete_by_index(lst):
    try:
        idx = int(input("Enter index to delete: "))
        lst.pop(idx)
    except (ValueError, IndexError):
        print("Invalid index.")
    show(lst)

def update_element(lst):
    try:
        idx = int(input("Enter index to update: "))
        new_val = input("Enter new value: ")
        lst[idx] = new_val
    except (ValueError, IndexError):
        print("Invalid index.")
    show(lst)

while True:
    print("\nMENU")
    print("1. Insert Element")
    print("2. Delete by Value")
    print("3. Delete by Index")
    print("4. Update Element at Index")
    print("5. Show list")
    print("6. Exit")
    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        insert_element(items)
    elif choice == "2":
        delete_by_value(items)
    elif choice == "3":
        delete_by_index(items)
    elif choice == "4":
        update_element(items)
    elif choice == "5":
        show(items)
    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")