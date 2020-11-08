import csv
import datetime
from datetime import date
import calendar


class Workout:
    def __init__(self, category):
        self.today = date.today()
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
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for exercise in self.exercises:
                writer.writerow([self.today,self.DOTW,self.category,exercise.name,exercise.sets,exercise.reps])


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
    workout.log_exercises()

