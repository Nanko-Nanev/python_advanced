from collections import deque
players = deque(input().split())
n = int(input())
counter = 0

while not len(players) == 1:
    for i in range(1, n+1):
        if i == n:
            print(f"Removed {players[0]}")
            players.remove(players[0])
        else:
            first = players.popleft()
            players.append(first)


print(f"Last is {players[0]}")