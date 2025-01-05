from features import Queue 
from features import Enhanced_queue

class QueueOutOfRangeException(Exception):
    pass

def enhance_Queue_menu():
    q = Queue()
    while True:
        print("1. create queue")
        print("2. insert")
        print("3. pop")
        print("4. print")
        print("5. save")
        print("6. load")
        print("7. Exit")

        choice = input("Enter your choice: ")
        arr_queue={}
        try:
            if choice == "1":
                try:
                    name = input("Enter the name of the queue: ")
                    if name == "":
                        raise ValueError("empty string")
                    if not isinstance(name, str):
                        raise ValueError("Invalid")
                    if name in Enhanced_queue.Queues:
                        print("already exists.")
                        return
                    max_size = int(input("Enter the maximum size of the queue: "))
                    if not isinstance(max_size,int):
                        raise ValueError ("Input must be an integer.")
                    arr_queue[name] = Enhanced_queue(name, max_size)
                    print(f"'{name}' created with size {max_size}.")
                except ValueError:
                    print("Invalid")

            elif choice == "2":
                try:
                    name = input("Enter the name of the queue : ")
                    if name not in Enhanced_queue.Queues:
                        print(f"No queue found with the name '{name}'.")
                        return
                    value = input("Enter the value: ")
                    value=int(value)
                    if not isinstance(max_size,int):
                        raise ValueError ("Invalid")
                    Enhanced_queue.Queues[name].insert(value)
                    print(f"'{value}' inserted.")
                except ValueError as e:
                    print(f"Error: {e}")
                except QueueOutOfRangeException as e:
                    print(f"Error: {e}")


            elif choice == "3":
                try:
                    name = input("Enter the name of the queue : ")
                    if name not in Enhanced_queue.Queues:
                        print(f"No queue found with the name '{name}'.")
                        return
                    value =Enhanced_queue.Queues[name].pop()
                    if value is not None:
                        print(f"Popped item: {value}")
                except ValueError as e:
                    print(f"Error: {e}")
                except QueueOutOfRangeException as e:
                    print(f"Error: {e}")


            elif choice == "4":
                try:
                    name = input("Enter the name of the queue to print: ")
                    if name == "":
                        raise ValueError("empty string")
                    if not isinstance(name, str):
                        raise ValueError("Invalid")
                    if name not in Enhanced_queue.Queues:
                        print(f"No queue found with the name '{name}'.")
                        return
                    print(f"Contents of queue '{name}':")
                    Enhanced_queue.Queues[name].print_queue()
                except Exception as e:
                    print(f"Error: {e}")
            
            elif choice == "5":
                try:
                    filename = input("Enter the filename to save queues: ")
                    Enhanced_queue.save(filename)  
                    print(f"All queues have been saved to '{filename}'.")
                except Exception as e:
                    print(f"Error saving queues: {e}")
            elif choice == "6":
                    try:
                        filename = input("Enter the filename to load queues: ")
                        Enhanced_queue.load(filename)  
                    except Exception as e:
                        print(f"Error loading queues: {e}")
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Error: " + str(e))
            




if __name__ == "__main__":
    enhance_Queue_menu()