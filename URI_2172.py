monster_qty, experience = map(int, input().split())
total_experience = monster_qty * experience
while total_experience != 0:
    print(total_experience)
    monster_qty, experience = map(int, input().split())
    total_experience = monster_qty * experience
