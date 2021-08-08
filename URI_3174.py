worker_hours = {'bonecos': 0,
                'arquitetos': 0,
                'musicos': 0,
                'desenhistas': 0}

elves_qty = int(input())
for e in range(elves_qty):
    name, job, hours = input().split()
    worker_hours[job] += int(hours)

print(worker_hours['bonecos'] // 8 +
      worker_hours['arquitetos'] // 4 +
      worker_hours['musicos'] // 6 +
      worker_hours['desenhistas'] // 12)
