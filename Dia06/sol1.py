f = open('input.txt')

text = f.readline()

for i in range(len(text)):
    if len(set(text[i:i+14])) == 14:
        print(set(text[i:i+14]))
        print(text[i:i+14])
        print(i+14)
        break
f.close()