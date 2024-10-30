# Personalized Study Assistant

## Project Overview
The **Personalized Study Assistant** is a Python-based application designed to help users create and manage a personalized study schedule. The program allows users to input their study topics, define daily study hours, set deadlines, and track their progress. It dynamically adjusts the study plan based on progress and generates reports to guide the user toward achieving their study goals efficiently.

## Features
- **Personalized Study Schedule**: Create a study plan based on topics, available daily study hours, and deadlines.
- **Progress Tracking**: Log study hours, track your progress, and adjust the study plan accordingly.
- **Dynamic Adjustments**: The study schedule updates automatically based on how much time is spent on each topic.
- **Progress Reports**: Generate a report that summarizes your study progress and highlights areas that need more attention.

## Prerequisites
To run this project, you'll need the following installed on your machine:
- Python 3.13.0 or above
- pytest (for testing)

## Installation
1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/Altaf-7/Personalized-Study-Assistant.git
   ```

2. Change directory of current folder.
   ```bash
   cd personalized-study-assistant
   ```

3. (Optional) Create and activate a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
   ```

4. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main program by executing the `project.py` file:
   ```bash
   python project.py
   ```

2. Follow the on-screen prompts to:
   - Input study topics.
   - Specify the time available for each day.
   - Set deadlines.
   - Track your study progress over time.

3. After completing study sessions, log the time spent on each topic, and the system will adjust your schedule.

4. Generate a report anytime to view your progress and see which topics need more focus.

### Example:
```
Welcome to the Personalized Study Assistant!
Please enter the topics you want to study (comma-separated): Math, Physics, Chemistry
How many hours can you study per day? 4
Enter the deadline (YYYY-MM-DD): 2024-10-31

Your study schedule has been created!
----------------------------------------
Math: 1.5 hours per day
Physics: 1.0 hours per day
Chemistry: 1.5 hours per day
----------------------------------------
Log your study progress by entering the topic and hours spent.
```

## Project Structure
```
/root
  ├── project.py           # Main program file
  ├── test_project.py      # Test file containing pytest test cases
  ├── requirements.txt     # List of pip-installable libraries
  ├── README.md            # Project documentation (this file)
```

### project.py
- Contains the `main()` function that runs the program.
- Additional functions:
  1. `schedule_study(topics, hours_per_day, deadline)`: Generates a personalized study schedule.
  2. `track_progress(topic, hours_spent)`: Updates the progress for a particular topic.
  3. `generate_report()`: Generates a summary of study progress.

### test_project.py
- Contains test cases for the functions in `project.py` using `pytest`.

### requirements.txt
- Lists any required external libraries:
  ```
  pytest
  ```

## Running Tests
To ensure that the application works as expected, you can run the test cases using `pytest`:
```bash
pytest test_project.py
```
This will execute the tests for the core functions of the application.

## Future Improvements
- **Progress Visualization**: Use matplotlib to generate visual charts that display study progress over time.
- **Task Prioritization**: Automatically prioritize topics based on user-defined difficulty or importance.
- **Reminders**: Send reminders or notifications when it's time to study or when the user is behind schedule.

---
