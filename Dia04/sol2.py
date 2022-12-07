f = open('input.txt')

lines = [[[int(k) for k in j.split('-')] for j in i.strip().split(',')] for i in f.readlines()]

num = 0
for pair1,pair2 in lines:
    if not ((pair1[1] < pair2[0]) or (pair1[0] > pair2[1])):
        num += 1
        print(pair1,pair2)

print(num)