n = int(input())
cards = list(map(int, input().split()))

Alice = 0
Bob = 0

sorted_cards = sorted(cards, reverse=True)

for i in range(n):
    if i % 2 ==0:
        Alice += sorted_cards[i]
    else:
        Bob += sorted_cards[i]
print(Alice - Bob)