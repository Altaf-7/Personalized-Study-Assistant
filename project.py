from datetime import date
import sys
import re

# Main function to run the program
def main():
    print("Welcome to the Personalized Study Assistant!")
    # topics_raw = input("Please enter the topics you want to study (comma-separated): ").split(",")
    topics_raw = sys.argv[1].split(",")
    topics = {}
    for topic in topics_raw:
        while True:
            try: #update README.md for this
                weightage_raw = int(input(f'How important is "{topic.strip()}" on a scale of 1 to 5? ').strip())
                if weightage_raw not in range(1,6):
                    raise ValueError
                topics[topic.strip()] = weightage_raw
                break
            except ValueError:
                pass

    while True:
        # hours_per_day = float(input("How many hours can you study per day? "))
        hours_per_day = float(sys.argv[2])
        if 0 < hours_per_day < 24:
            if hours_per_day > 12:
                print(
                    "Warning: Studying more than 12 hours a day may cause some health issues in the long run."
                )
                # add this as a feature in README.md
                while True:
                    confirmation = input("wish to continue? (yes/no): ")
                    if confirmation == "yes":
                        break
                    elif confirmation == "no":
                        sys.exit()
            break
        else:
            print("Enter proper hours you can study")

    while True:
        try:  # update README.md for this
            # deadline_str = input("Enter the deadline (YYYY-MM-DD): ")
            deadline_str = sys.argv[3]
            if not re.search(r"202[4-9]-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|1[0-9]|2[0-9]|3[0-1])", deadline_str):
                raise ValueError
            year, mon, da = deadline_str.split("-")
            year, mon, da = int(year), int(mon), int(da)
            deadline = date(year, mon, da)
            today = date.today()
            total_days = (deadline - today).days
            if total_days <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid date. Please enter a valid Future date in the format YYYY-MM-DD.")


    # Generate the Study Schedule
    study_plan = schedule_study(topics, hours_per_day, total_days)
    for topic, hours in study_plan.items():
        hours_int = int(hours)
        minutes = int(round((hours - hours_int) * 60))
        if minutes == 0:
            print(f"{topic}\t: {hours_int} hours per day")
        elif hours_int == 0:
            print(f"{topic}\t: {minutes} minutes per day")
        else:
            print(f"{topic}\t: {hours_int} hours {minutes} minutes per day")
    print("-"*108)


    # Track progress
    while True:
        print("Log your study progress or type 'exit' to quit:")
        topic = input("Which topic did you study? (or 'exit'): ").strip()
        if topic == 'exit':
            break
        if topic not in study_plan.keys():
            print("Topic not found! Please try again.")
            continue
        hours_spent = float(input(f'How many hours did you study for "{topic}" (in float) ? '))
        track_progress(study_plan, topic, hours_spent)


# Function to generate a study schedule
def schedule_study(topics, hours_per_day, total_days):
    total_hours = total_days * hours_per_day
    study_plan = {}
    total_weight = sum(topics.values())
    for topic in topics.keys():
        study_plan[topic] = round(total_hours * topics[topic] / total_weight / total_days, 2)
    print("-"*108)
    print("Your Study Schedule has been Created!")
    print(f"For Next {total_days} Days:- ")
    return study_plan


# Function to track progress
def track_progress(study_plan, topic, hours_spent):
    # Reduce the remaining time for the topic
    if topic in study_plan.keys():
        ...
        
    else:
        print(f'Topic "{topic}" not found in the study plan.')


# Function to generate a progress report
def generate_report(study_plan, deadline): ...


if __name__ == "__main__":
    main()
