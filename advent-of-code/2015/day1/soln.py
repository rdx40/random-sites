def part1():
    with open('input.txt', 'r') as file:
        ls = file.read().strip()
        print(ls.count('(') - ls.count(')'))

def part2():
    with open('input.txt', 'r') as f_in :
        ls = f_in.read().strip()
        floor = 0
        for idx,ch in enumerate(ls):
            if ch == '(' : floor += 1
            elif ch == ')' : floor -=1

            if floor == -1 :
                print(idx + 1)
                break
part1()
part2()
