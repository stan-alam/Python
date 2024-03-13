

import os
from multiprocessing import Process
 
 
def run_child_process() -> None:
    print("Child: child process")
    print(f"Child: PID: {os.getpid()}")
    print(f"Child: Parent’s PID: {os.getppid()}")
 
 
def start_parent(num_children: int) -> None:
    print("Parent : parent process")
    print(f"Parent : Parent’s PID: {os.getpid()}")
    for i in range(num_children):
        print(f"Starting Process {i}")
        Process(target=run_child_process).start()
 
if __name__ == "__main__":
    num_children = 3
    start_parent(num_children)