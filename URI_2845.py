"""
Using the identity:
sum(k)_(1 <= k <= n, gcd(k,n) = 1) = n*phi(n)/2
where phi(n) is the Euler's Totient function
"""

identifiers_qty = int(input())
identifiers = list(map(int, input().split()))
print(2 * sum(identifiers) // identifiers_qty)
