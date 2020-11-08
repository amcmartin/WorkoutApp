import sqlite3
from datetime import date
import time
import calendar


class Workout:
    def __init__(self, category):
        self.today = int(time.time())
        self.DOTW = calendar.day_name[date.today().weekday()]
        self.category = category
        self.exercises = []

    def get_date(self):
        return self.today

    def get_category(self):
        return self.category

    def add_exercise(self,exercise):
        self.exercises.append(exercise)

    def log_exercises(self):
        """Logs all information about the exercise into the data base"""
        conn = sqlite3.connect("workout.db")
        cursor = conn.cursor()
        for exercise in self.exercises:
            cursor.execute("INSERT INTO workout VALUES (?, ?, ?, ?, ?, ?)",
                           (self.today, self.DOTW, self.category,exercise.name,exercise.sets,exercise.reps))
        conn.commit()
        conn.close()


def print_exercises(self):
    for i in (self.exercises):
        print(i.name)


class Exercise:
    def __init__(self,name,sets,reps):
        self.name = name
        self.sets = sets
        self.reps = reps

    def get_name(self):
        return self.name
    def get_sets(self):
        return self.sets
    def get_reps(self):
        return self.reps









if __name__ == "__main__":
    workout = Workout("Back")
    exercise1 = Exercise("Dead Lift",5,5)
    exercise2 = Exercise("bent over rows", 4,10)
    workout.add_exercise(exercise1)
    workout.add_exercise(exercise2)
    # workout.log_exercises()
    # conn = sqlite3.connect("workout.db")
    # cursor = conn.cursor()
    # cursor.execute("""CREATE TABLE workout (
    #     Date integer,
    #     DayOfTheWeek text,
    #     Category text,
    #     exercise text,
    #     Sets integer,
    #     Reps integer
    #     )""")
    conn = sqlite3.connect("workout.db")
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO workout VALUES (1576280665, 'Saturday', 'Back', 'Deadlift', 5, 5)")
    cursor.execute("SELECT * FROM workout WHERE DayOfTheWeek='Saturday'")
    print(cursor.fetchall())
    # conn.commit()
    conn.close()
