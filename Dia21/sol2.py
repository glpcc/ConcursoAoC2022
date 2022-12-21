import time

c = time.time_ns()

f = open("input.txt")

# dict with monkey: monkey_value or tuple with left_mokey,right_mokey,op
tree: dict[str,tuple[str,str,str]|int] = dict()

for i in f.readlines():
    line = i.strip()
    mokey = line[:4]
    if line[6].isdigit():
        tree[mokey] = int(line[6:])
    else:
        left_monkey = line[6:10]
        opp = line[11]
        right_monkey = line[13:]
        tree[mokey] = (left_monkey,right_monkey,opp)

def calculate_monkey(mokey: str):
    if type(tree[mokey]) == int:
        return tree[mokey]
    else:
        temp = tree[mokey]   
        left_monkey = calculate_monkey(temp[0])
        right_monkey = calculate_monkey(temp[1])
        opp = temp[2]
        if opp == '+':
            return left_monkey + right_monkey
        elif opp == '-':
            return left_monkey - right_monkey
        elif opp == '/':
            return left_monkey / right_monkey
        else:
            return left_monkey * right_monkey

tree["humn"] = 1
# root comparisons = tlpd + jjmw
b = calculate_monkey('jjmw')
magnitud = 12
done = False
iters = 0
while not done:
    a = calculate_monkey('tlpd')
    while a-b > 0:
        tree['humn'] += 10**magnitud
        a = calculate_monkey('tlpd')
        iters += 1
    if a-b == 0:
        done = True
    else:
        tree['humn'] -= 10**magnitud
        magnitud -= 1
        print(magnitud)

print(tree['humn'])
print(iters)
print((time.time_ns()-c)/10000)