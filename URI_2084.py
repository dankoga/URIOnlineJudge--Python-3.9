if __name__ == '__main__':
    candidates_qty = int(input())
    votes = list(map(int, input().split()))
    votes.sort(reverse=True)
    total_votes = sum(votes)

    if (20 * votes[0] >= 9 * total_votes) or \
       ((5 * votes[0] >= 2 * total_votes) and 10 * (votes[0] - votes[1]) >= total_votes):
        print(1)
    else:
        print(2)
