# CyberScope

CyberScope is a Python program designed to automate the execution of scripts or programs at specific times on Windows. It continuously checks the current time against a predefined schedule and runs the associated command when the scheduled time is reached.

## Features

- **Automated Task Execution**: Specify tasks to run at particular times.
- **Multi-threaded Execution**: Commands are executed in separate threads to ensure the main program remains responsive.

## Requirements

- Windows operating system.
- Python 3.x installed on the system.
- Ensure the scripts or programs to be run are accessible to the Python environment.

## Installation

1. Clone the repository or download the `cyberscope.py` file.
2. Ensure Python is installed and added to the system PATH.

## Usage

1. Modify the `schedule` list in `cyberscope.py` to include the times and commands you wish to execute. Each task should be a dictionary with keys `time` (in `HH:MM` format) and `command` (the command or script to execute).

    ```python
    schedule = [
        {'time': '14:00', 'command': 'notepad.exe'},
        {'time': '14:30', 'command': 'calc.exe'}
    ]
    ```

2. Run the script using Python:

    ```sh
    python cyberscope.py
    ```

3. The program will check the schedule every minute and execute the specified commands at the appropriate times.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features or improvements you make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.