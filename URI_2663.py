competitors_total = int(input())
competitors_min = int(input())
score_histogram = dict()
for competitors in range(competitors_total):
    score = int(input())
    if score in score_histogram:
        score_histogram[score] += 1
    else:
        score_histogram[score] = 1
scores_sorted = sorted(score_histogram)
competitors_passed = score_histogram[scores_sorted[-1]]
index = -2
while competitors_passed < competitors_min:
    competitors_passed += score_histogram[scores_sorted[index]]
    index -= 1
print(competitors_passed)
