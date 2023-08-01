 #a context manager is object that defines a context of a block of code


# def open_file(filename):
#     file = open(filename, "r")

#     def __enter__(self):
#         return file

#     def __exit__(self, exc_typ, exc_value, exc_tb):
#         file.close()

#     return __enter__, __exit__


# with open_file("my_file.txt") as f:
#     contents = f.read()




#Example2 uisng a time series
#import time


# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()

#     def __exit__(self, exc_type, exc_values, traceback):  
#         end_time = time.time()
#         execution_time = end_time - self.start_time
#         print({execution_time})


# with Timer():
#     time.sleep(2)        



      
# # Multithreading and multiprocessing
# import threading

# def task(name):
#     print({name})



    
# # create multiple threads    
# threads = []
# for i in range(5):
#     t = threading.Thread(target=task, args=({i}))


#     threads.append(t)
#     t.start()


# # create multiple threads    

# for t in threads:
#     t.join()


#Example on multiprocessing

# import multiprocessing

# def process_task(name):
#       print({name})
      
# #create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# #submit multiple tasks to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=({i}))

# #close the pool and wait for all processes to finish
# pool.close()
# pool.join()


#Demonstrate the use of multiprocessing and multithreading

#import threading
#import multiprocessing

#def task(name):
   #print(f"{name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

#create multiple threads
# threads = []

# for i in range(5):
#     t = threading.Thread(target=task, args=({i}))
#     threads.append(t)
#     t.start()

# # wait for all threads to finish

# for t in threads:
#     t.join()

import sqlite3
import time
import threading
import multiprocessing

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT)")
        self.connection.commit()

    def insert_task(self, task_name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (name) VALUES (?)", (task_name,))
        self.connection.commit()

    def print_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)


class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def read_contents(self):
        return self.file.read()    


# Example usage for DatabaseManager:
with DatabaseManager("example.db") as db_manager:
    db_manager.insert_task("Task 1")
    db_manager.print_tasks()


# Example usage for FileManager:
# Example usage for FileManager:
file_path = "/home/kuberwa/Desktop/Desktop/Desktop/Desktop/A7/example.txt"
with FileManager(file_path, "r") as  file_manager:
    contents = file_manager.read()
    print(contents)

# import time
# import threading
# import multiprocessing

def sleep_for(seconds):
    time.sleep(seconds)
    print(f"Thread sleeping for {seconds} seconds has finished.")

def main():
    # Create a thread that sleeps for 1 second.
    thread1 = threading.Thread(target=sleep_for, args=(1,))
    thread1.start()

    # Create a thread that sleeps for 2 seconds.
    thread2 = threading.Thread(target=sleep_for, args=(2,))
    thread2.start()

    # Create a process that sleeps for 3 seconds.
    process1 = multiprocessing.Process(target=sleep_for, args=(3,))
    process1.start()

    # Wait for all threads and processes to finish.
    thread1.join()
    thread2.join()
    process1.join()

if __name__ == "__main__":
    main()
