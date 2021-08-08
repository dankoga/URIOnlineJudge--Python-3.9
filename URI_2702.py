from operator import sub

meals_available = list(map(int, input().split()))
meals_ordered = list(map(int, input().split()))
meals_deficit = 0
for index in range(3):
    meal_short = meals_ordered[index] - meals_available[index]
    if meal_short > 0:
        meals_deficit += meal_short
print(meals_deficit)
