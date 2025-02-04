import subprocess
import time
from datetime import datetime
import os
import threading

class CyberScope:
    def __init__(self, schedule):
        """
        Initialize the CyberScope with a schedule.
        
        :param schedule: A list of dictionaries with keys 'time' and 'command'. 
                         'time' is a string in HH:MM format, 'command' is the script or program to run.
        """
        self.schedule = schedule

    def run_scheduled_tasks(self):
        """Check the schedule and run tasks at the specified times."""
        while True:
            now = datetime.now().strftime("%H:%M")
            for task in self.schedule:
                if task['time'] == now:
                    print(f"Running command: {task['command']} at {now}")
                    self.run_command(task['command'])
            time.sleep(60)  # Check the schedule every minute

    @staticmethod
    def run_command(command):
        """Run a command in a separate thread."""
        def target():
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"Successfully executed: {command}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to execute: {command}. Error: {e}")

        thread = threading.Thread(target=target)
        thread.start()

if __name__ == "__main__":
    # Example schedule
    schedule = [
        {'time': '14:00', 'command': 'notepad.exe'},
        {'time': '14:30', 'command': 'calc.exe'}
    ]

    cyberscope = CyberScope(schedule)
    cyberscope.run_scheduled_tasks()