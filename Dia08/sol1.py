f = open('input.txt')

trees = [[int(j) for j in i.strip()] for i in f.readlines()]

visible_trees = [[False for j in i] for i in trees]
# Count visible from left side
for i in range(len(trees)):
    min_h = -1
    for j in range(len(trees[i])):
        if trees[i][j] > min_h:
            visible_trees[i][j] = True
            min_h = trees[i][j]

# Count visible from right side
for i in range(len(trees)):
    min_h = -1
    for j in range(1,len(trees[i])+1):
        if trees[i][-j] > min_h:
            visible_trees[i][-j] = True
            min_h = trees[i][-j]

# Count visible from top
for i in range(len(trees[0])):
    min_h = -1
    for j in range(len(trees)):
        if trees[j][i] > min_h:
            visible_trees[j][i] = True
            min_h = trees[j][i]

# Count visible from bottom
for i in range(len(trees[0])):
    min_h = -1
    for j in range(1,len(trees)+1):
        if trees[-j][i] > min_h:
            visible_trees[-j][i] = True
            min_h = trees[-j][i]

# Count total visible trees
num_trees = 0
for i in visible_trees:
    for j in i:
        if j:
            num_trees += 1

print(num_trees)