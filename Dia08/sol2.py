f = open('input.txt')

trees = [[int(j) for j in i.strip()] for i in f.readlines()]
top_scenic_value = 0
# I will ignore border trees as they have a sceniic value of 0
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[i])-1):
        
        tree_val = trees[i][j]
        left_dist = 0
        right_dist = 0
        top_dist = 0
        bottom_dist = 0
        k = 1
        while left_dist == 0 or right_dist == 0 or top_dist == 0 or bottom_dist == 0:
            if left_dist == 0:
                if j-k < 0:
                    left_dist = k-1
                elif trees[i][j-k] >= tree_val:
                    left_dist = k
            if right_dist == 0:
                if j+k >= len(trees[0]):
                    right_dist = k-1
                elif trees[i][j+k] >= tree_val:
                    right_dist = k
            if top_dist == 0:
                if i-k < 0:
                    top_dist = k-1
                elif trees[i-k][j] >= tree_val:
                    top_dist = k
            if bottom_dist == 0:
                if i+k >= len(trees):
                    bottom_dist = k-1
                elif trees[i+k][j] >= tree_val:
                    bottom_dist = k
            k += 1
        if left_dist*right_dist*bottom_dist*top_dist > top_scenic_value:
            top_scenic_value = left_dist*right_dist*bottom_dist*top_dist
        # print(i,j,left_dist,right_dist,top_dist,bottom_dist)
print(top_scenic_value)