from datetime import date
import sys
import re

# Main function to run the program
def main():
    print("Welcome to the Personalized Study Assistant!")
    topics_raw = input("Please enter the topics you want to study (comma-separated): ").split(",")
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


    # Valadation of Hours To Study and also to check if its under 12 for well being
    while True:
        hours_per_day = float(input("How many hours can you study per day? "))
        if 0 < hours_per_day < 24:
            if hours_per_day > 12:
                print(
                    "Warning: Studying more than 12 hours a day may cause some health issues in the long run."
                )
                print("Please Reconsider and go for less.")
                continue
            break
        else:
            print("Enter proper hours you can study")


    # Valdatition of Date in correct format, also for date in future 
    while True:
        try:
            deadline_str = input("Enter the deadline (YYYY-MM-DD): ")
            if not re.search(r"^(?:202[4-9])-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|1[0-9]|2[0-9]|3[0-1])$", deadline_str):
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
        study_plan[topic] = f"{hours_int}:{minutes:02}"
        if minutes == 0:
            print(f"{topic}\t: {hours_int} hours per day")
        elif hours_int == 0:
            print(f"{topic}\t: {minutes} minutes per day")
        else:
            print(f"{topic}\t: {hours_int} hours {minutes} minutes per day")
    print("-"*108)


    # Track progress
    while True:
        print("\nLog your study progress or type 'exit' to quit:")
        topic = input("Which topic did you study? (or 'exit'): ").strip().lower()
        if topic == 'exit':
            break
        if topic not in study_plan.keys():
            print("Topic not found! Please try again.")
            continue
        while True:
            hours_spent = input(f'How many hours did you study for "{topic}" (HH:MM) ? ').strip()
            if not re.search(r"^(0?[0-9]|1[0-2]):(0?[0-9]|[1-5][0-9])$",hours_spent):
                print("Please enter a valid time in HH:MM")
                continue
            break
        study_plan = track_progress(study_plan, topic, hours_spent)
        if all(value == "0:00" for value in study_plan.values()):
            print("Done for today, Go have fun...\n")
            break


    # Optionally generate a report after progress
    while True:
        report = input("\nWould you like to see a progress report? (y/n): ").lower()
        if report == 'y':
            generate_report(study_plan, deadline)
            break
        elif report == 'n':
            break


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
def track_progress(study_plan, topic, time_studied):
    if topic in study_plan.keys():
        study_plan_hour_int, study_plan_minutes = study_plan[topic].split(":")
        study_plan_hour_int, study_plan_minutes = int(study_plan_hour_int), int(study_plan_minutes)
        time_studied_hours, time_studied_mins = time_studied.split(":")
        time_studied_hours, time_studied_mins = int(time_studied_hours), int(time_studied_mins)
        "\n"

        if time_studied_hours > study_plan_hour_int:
            print(f'\nYou have Studied "{topic}" excess than Scheduled time.')
            study_plan_hour_int = 0
            study_plan_minutes = 0
        elif time_studied_hours == study_plan_hour_int:
            if time_studied_mins > study_plan_minutes:
                print(f'\nYou have Studied "{topic}" excess than Scheduled time.')
                study_plan_hour_int = 0
                study_plan_minutes = 0
            elif time_studied_mins == study_plan_minutes:
                print(f'''You Accomplished today's goal for topic "{topic}".''')
                study_plan_hour_int = 0
                study_plan_minutes = 0
            else:
                study_plan_hour_int = 0
                study_plan_minutes -= time_studied_mins
        else:
            if time_studied_mins > study_plan_minutes:
                study_plan_hour_int -=1
                study_plan_minutes = 60 + study_plan_minutes - time_studied_mins
            elif time_studied_mins == study_plan_minutes:
                study_plan_hour_int = study_plan_hour_int - time_studied_hours
                study_plan_minutes = 0
            else:
                study_plan_hour_int = study_plan_hour_int - time_studied_hours
                study_plan_minutes -= time_studied_mins

        #update the study hours per input
        study_plan[topic] = f"{study_plan_hour_int}:{study_plan_minutes:02}"
        if study_plan_minutes == 0:
            print(f'Progress for "{topic}" updated. {study_plan_hour_int} hours remaining for "{topic}" today.')
        elif study_plan_hour_int == 0:
            print(f'Progress for "{topic}" updated. {study_plan_minutes} mins remaining for "{topic}" today.')
        else:
            print(f'Progress for "{topic}" updated. {study_plan_hour_int} hours and {study_plan_minutes} mins remaining for "{topic}" today.')
        return study_plan
    else:
        print(f'Topic "{topic}" not found in the study plan.')


# Function to generate a progress report
def generate_report(study_plan, deadline):
    "\n"
    print("*"*108)
    print("Progress Report:")
    for topic, time in study_plan.items():
        hours, mins = time.split(":")
        hours, mins = int(hours), int(mins)
        if hours == 0 and mins == 0:
            print(f"{topic} Completed.")
        elif hours > 0 or mins > 0:
            print(f"{topic} On track")
            if hours == 0:
                print(f'{mins} mins remaining for today.')
            elif mins == 0:
                print(f'{hours} hours remaining for today.')
            else:
                print(f'{hours} hours and {mins} mins remaining for today.')
    days_remaining = (deadline - date.today()).days
    print(f"Days remaining until the deadline: {days_remaining}")
    print("*"*108)


if __name__ == "__main__":
    main()
