from project import schedule_study, track_progress, generate_report
from datetime import date
import pytest


def test_schedule_study():
    assert schedule_study(["chem", "phy", "maths"], 3, date(2024, 11, 1)) == {
        "chem": 1.0,
        "phy": 1.0,
        "maths": 1.0,
    }

    assert schedule_study(["a", "b", "c", "d"], 8, date(2024, 12, 1)) == {
        "a": 2.0,
        "b": 2.0,
        "c": 2.0,
        "d": 2.0,
    }

    assert schedule_study(["a", "b", "c"], 4, date(2025, 2, 10)) == {
        "a": 1.33,
        "b": 1.33,
        "c": 1.33,
    }

    assert schedule_study(
        ["matrix", "circle", "vectors", "probability"], 2, date(2025, 6, 28)
    ) == {"matrix": 0.5, "circle": 0.5, "vectors": 0.5, "probability": 0.5}

    with pytest.raises(SystemExit):
        schedule_study(["A", "B"], 4, date(2024, 10, 1))
        schedule_study(["m", "n"], 6, date(2024, 10, 29))

    ...  # add more edge cases like hrs_can_you_study = 0 and others


# def test_track_progress():
#     ...


# def test_generate_report():
#     ...
