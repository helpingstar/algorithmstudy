import sys

input = sys.stdin.readline


def solution():
    n_player, m = map(int, input().split())
    rooms = []
    for i in range(n_player):
        level, nick = input().split()
        level = int(level)
        checked = False
        for bot, top, mem_list in rooms:
            if len(mem_list) < m and (bot <= level <= top):
                mem_list.append((nick, level))
                checked = True
                break
        if not checked:
            rooms.append([level - 10, level + 10, [(nick, level)]])
    for bot, top, mem_list in rooms:
        if len(mem_list) == m:
            print("Started!")
        else:
            print("Waiting!")
        for nick, level in sorted(mem_list, key=lambda x: x[0]):
            print(level, nick)


solution()
