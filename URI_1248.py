tests_qty = int(input())

for t in range(tests_qty):
    diet_plan = ''.join(sorted([letter for letter in input()]))
    menu_breakfast = input()
    menu_lunch = input()

    if all([food_b in diet_plan for food_b in menu_breakfast]):
        for food_b in menu_breakfast:
            diet_plan = diet_plan.replace(food_b, '', 1)
        if all([food_l in diet_plan for food_l in menu_lunch]):
            for food_l in menu_lunch:
                diet_plan = diet_plan.replace(food_l, '', 1)
            print(diet_plan)
        else:
            print('CHEATER')
    else:
        print('CHEATER')
