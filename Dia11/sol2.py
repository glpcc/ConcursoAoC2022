from __future__ import annotations

f = open('input.txt')
lines = [i.strip() for i in f.readlines()]

# Calculated by multipling every number the monkeys checks for divisibility ( I havent found the proof but i tested it and works :)  )
MOD_NUM = 9699690

class Monkey():
    def __init__(self,monkey_num: int, starting_items: list[int],opp: str,opp_number: str,divisible_num: int,true_throw_monkey_num: int,false_throw_monkey_num: int) -> None:
        self.monkey_num = monkey_num
        self.items = starting_items
        self.processed_items = 0
        if opp_number == 'old':
            self.operation = lambda x: x*x
        elif opp == '+':
            self.operation = lambda x: x+int(opp_number)
        elif opp == '*':
            self.operation = lambda x: x*int(opp_number)
        else:
            raise ValueError('Operation not valid')
        
        self.divisible_num = divisible_num
        self.true_monk = true_throw_monkey_num
        self.false_monk = false_throw_monkey_num
    
    def process_items(self, monkey_dict: dict[int,Monkey]):
        for i in range(len(self.items)):
            item = self.items[i]
            worry_level = self.operation(item)
            if worry_level%self.divisible_num == 0:
                monkey_dict[self.true_monk].items.append(worry_level%MOD_NUM)
            else:
                monkey_dict[self.false_monk].items.append(worry_level%MOD_NUM)
            self.processed_items += 1
        self.items = []

monkey_dict: dict[int,Monkey] = dict()
for i in range(8):
    mokey_num = int(lines[i*7][7])
    processed_items = [int(j) for j in lines[i*7 + 1][15:].split(',')]
    opp = lines[i*7 + 2][21]
    opp_num = lines[i*7 + 2][23:]
    divisible_num = int(lines[i*7 + 3][19:])
    true_mon = int(lines[i*7 + 4][25])
    false_mon = int(lines[i*7 + 5][26])
    monkey = Monkey(mokey_num,processed_items,opp,opp_num,divisible_num,true_mon,false_mon)
    monkey_dict[mokey_num] = monkey

for j in range(10000):
    for i in monkey_dict:
        monkey_dict[i].process_items(monkey_dict)
    if j%999 == 0:
        processed_items_list = []
        for i in monkey_dict:
            processed_items_list.append(monkey_dict[i].processed_items)
        print(j,sorted(processed_items_list))


processed_items_list = []
for i in monkey_dict:
    processed_items_list.append(monkey_dict[i].processed_items)

print(sorted(processed_items_list)[-1]*sorted(processed_items_list)[-2])

