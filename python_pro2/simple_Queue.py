from features import Queue

def simple_Queue_menu():
    q = Queue()
    while True:
        print("1. insert")
        print("2. pop")
        print("3. list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                while True:
                    try:
                        ele = input("enter the value you want to add to Queue")
                        if ele.isdigit():
                            ele = int(ele)
                            q.insert(ele)
                        elif isinstance(ele,str):
                            q.insert(ele)
                        else:
                            print("invaild input")
                            continue
                    except ValueError as e:
                        print(f"Error: {e}")
                    choice = input("Do you want to insert another number? (y/n): ")
                    if choice == 'n': 
                        break

            elif choice == "2":
                try:
                    check = q.is_empty()
                    if check is not None:
                        q.arr.pop()
                        print("pooped successfully")
                except ValueError as e:
                    print(f"Error:{e}")


            elif choice == "3":
                q.print_queue()

            elif choice == "4":
                print("See you later...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Error: " + str(e))



if __name__ == "__main__":
    simple_Queue_menu()