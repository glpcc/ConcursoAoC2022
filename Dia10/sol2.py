f = open('input.txt')

lines = [i.strip() for i in f.readlines()]

cycle = 0
register = 1
signal_strength_sum = 0
crt: str = ""
def draw_pixel(sprite_pos,cycle,crt):
    if abs((cycle-1)%40 - sprite_pos) <= 1:
        crt += '#'
    else:
        crt += '.'
    return crt


for line in lines:
    if line == 'noop':
        cycle += 1
        crt = draw_pixel(register,cycle,crt)
    else:
        _, value = line.split(' ')
        value = int(value)
        print(register,cycle)
        crt = draw_pixel(register,cycle+1,crt)
        crt = draw_pixel(register,cycle+2,crt)
        cycle += 2
        register += value
    

for i in range(len(crt)):
    if i%40 == 0:
        print()
    print(crt[i],end='')
