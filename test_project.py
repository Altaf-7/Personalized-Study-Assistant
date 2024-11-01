from project import schedule_study, track_progress, generate_report
from datetime import date
from io import StringIO
import sys


# hours_per_day and total_days are getting checked for correction in main(), so no need to check here
def test_schedule_study():
    assert schedule_study({"chem": 4, "phy": 3, "maths": 2}, 6.5, 45) == {
        "chem": "2:53",
        "phy": "2:10",
        "maths": "1:26",
    }

    assert schedule_study({"a": 3, "b": 3, "c": 3, "d": 3}, 8, 100) == {
        "a": "2:00",
        "b": "2:00",
        "c": "2:00",
        "d": "2:00",
    }

    assert schedule_study({"a": 4, "b": 3, "c": 1}, 4.0, 15) == {
        "a": "2:00",
        "b": "1:30",
        "c": "0:30",
    }

    assert schedule_study(
        {"matrix": 5, "circle": 3, "vectors": 4, "probability": 5}, 2.5, 5
    ) == {"matrix": "0:44", "circle": "0:26", "vectors": "0:35", "probability": "0:44"}

    assert schedule_study(
        {"matrix": 2, "circle": 1, "vectors": 3, "probability": 4}, 0, 3
    ) == {"matrix": "0:00", "circle": "0:00", "vectors": "0:00", "probability": "0:00"}


# topic and time_studied are getting checked for correction in main(), so no need to check here
def test_track_progress():
    assert track_progress(
        {"chem": "2:53", "phy": "2:10", "maths": "1:26"}, "chem", "2:00"
    ) == {"chem": "0:53", "phy": "2:10", "maths": "1:26"}

    assert track_progress(
        {"algebra": "4:00","statitics": "3:30", "complex": "1:15", "linear equation": "2:20",}, "linear equation","1:45"
    ) == {"algebra": "4:00", "statitics": "3:30", "complex": "1:15", "linear equation": "0:35"}

    assert track_progress({"a": "2:00", "b": "1:30", "c": "0:30"}, "c", "1:15") == {
        "a": "2:00", "b": "1:30", "c": "0:00",}

    assert track_progress(
        {"matrix": "1:20", "circle": "2:15", "vectors": "3:55", "probability": "2:35"},
        "vectors","0:00") == {"matrix": "1:20", "circle": "2:15", "vectors": "3:55", "probability": "2:35"}
    
    assert track_progress(
        {"loops": "2:25", "functions": "1:55", "exception handling": "0:55", "classes & objects": "1:35"},
        "loops","2:25") == {"loops": "0:00", "functions": "1:55", "exception handling": "0:55", "classes & objects": "1:35"}


#as this function does not return but prints an sequence of string we have to use StringIO() from io library
def test_generate_report():
    captured_output = StringIO()
    sys.stdout = captured_output

    generate_report({"Math": "2:00", "Science": "1:30", "Computer": "0:00"}, date(2024, 11, 25))
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
    assert "Progress Report:" in output
    assert "Math On track" in output
    assert "2 hours remaining for today." in output
    assert "Science On track" in output
    assert "1 hours and 30 mins remaining for today." in output
    assert "Computer Completed." in output
    assert f"Days remaining until the deadline: {(date(2024, 11, 25) - date.today()).days}" in output


    captured_output = StringIO()
    sys.stdout = captured_output    

    generate_report({"loops": "0:00", "functions": "1:05", "exception handling": "0:55", "classes & objects": "1:15"}, date(2024, 12, 31))
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
    assert "Progress Report:" in output
    assert "loops Completed." in output
    assert "functions On track" in output
    assert "1 hours and 5 mins remaining for today." in output
    assert "exception handling On track" in output
    assert "55 mins remaining for today." in output
    assert "classes & objects On track" in output
    assert "1 hours and 15 mins remaining for today." in output
    assert f"Days remaining until the deadline: {(date(2024, 12, 31) - date.today()).days}" in output
    
