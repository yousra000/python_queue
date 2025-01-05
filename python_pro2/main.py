from  simple_Queue import simple_Queue_menu
from enhance_Queue import enhance_Queue_menu


def main():
    while True:
        print("1. simple_Queue_menu")
        print("2. enhance_Queue_menu")
        print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                simple_Queue_menu()

            elif choice == "2":
                enhance_Queue_menu()
            elif choice == "3":
                print("See you later...")
                break
            else:
                print("invalid choice")
                continue
        except ValueError as e:
            print("Error: " + str(e))



if __name__ == "__main__":
    main()