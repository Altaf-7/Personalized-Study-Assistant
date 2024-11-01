# Personalized Study Assistant
## Video Demo
```bash
https://youtu.be/t6VhF3_x6Eo
```

## Project Overview
The **Personalized Study Assistant** is a Python-based application designed to help users create and manage a personalized study schedule. The program allows users to input their study topics,define priority of topics, define daily study hours, set deadlines, and track their progress. It dynamically adjusts the study plan based on progress and generates reports to guide the user toward achieving their study goals efficiently.

## Features
- **Personalized Study Schedule**: Create a study plan based on topics, available daily study hours, deadlines and priority.
- **Progress Tracking**: Log study hours, track your progress, and adjust the study plan accordingly.
- **Dynamic Adjustments**: The study schedule updates automatically based on how much time is spent on each topic.
- **Progress Reports**: Generate a report that summarizes your study progress and highlights topics that need more attention.

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
   - Specify the priority between 1 to 5 for each topic.
   - Specify the time available for each day.
   - Set deadlines.
   - Track your study progress over time.

3. After completing study sessions, log the time spent on each topic, and the system will adjust your schedule.

4. Generate a report anytime to view your progress and see which topics are completed and the topics which need more focus.

### Example:
```
Welcome to the Personalized Study Assistant!
Please enter the topics you want to study (comma-separated): Maths, Physics, Biology
How important is "Maths" on a scale of 1 to 5? 4
How important is "Physics" on a scale of 1 to 5? 3
How important is "Biology" on a scale of 1 to 5? 1
How many hours can you study per day? 4
Enter the deadline (YYYY-MM-DD): 2024-11-10
----------------------------------------------------------------------------------------------
Your Study Schedule has been Created!
For Next 10 Days:- 
Maths     : 2 hours per day
Physics   : 1 hours 30 minutes per day
Biology   : 30 minutes per day
----------------------------------------------------------------------------------------------

Log your study progress or type 'exit' to quit:
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
  1. `schedule_study(topics, hours_per_day, total_days)`: Generates a personalized study schedule.
  2. `track_progress(study_plan, topic, time_studied)`: Updates the progress for a particular topic.
  3. `generate_report(study_plan, deadline)`: Generates a summary of study progress.

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
- **Reminders**: Send reminders or notifications when it's time to study or when the user is behind schedule.

---
