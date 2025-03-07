def part1():
    with open('input.txt', 'r') as file:
        area = 0
        for l in file:
            ls = list(map(int,l.strip().split('x')))
            ls.sort()
            area += 3*ls[0]*ls[1] + 2*ls[0]*ls[2] + 2*ls[1]*ls[2]

        print(area)

def part2():
    with open('input.txt', 'r') as file:
        ribbon = 0
        for l in file:
            ls = list(map(int,l.strip().split('x')))
            ls.sort()
            ribbon += 2*ls[0] + 2*ls[1]
            ribbon += ls[0] * ls[1] * ls[2]

        print(ribbon)

part1()
part2()
