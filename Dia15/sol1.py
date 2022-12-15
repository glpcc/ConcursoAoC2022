import re
f = open("input.txt")

lines = [re.findall("(?:[xy]=)([\d-]*)",i) for i in f.readlines()]

lines = [[int(j) for j in i] for i in lines]

# Calculate how many cells a poss will occupy in line y = 2000000
Y_LINE = 2000000
def calculate_occupation_range(pos: list):
    dist = abs(pos[0]-pos[2]) + abs(pos[1]-pos[3])
    dist_in_y = dist - abs(pos[1]-Y_LINE)
    if dist_in_y > 0:
        rng = [pos[0]-dist_in_y,pos[0]+dist_in_y]
        return rng
    else:
        return None

# Could be a sortered list for better performance but im lazy
occupied_ranges: list[list] = []
for line in lines:
    occ_range = calculate_occupation_range(line)
    if occ_range is not None:
        # Check for intersections
        intersected_ranges = [False for i in range(len(occupied_ranges))]
        for indx,i in enumerate(occupied_ranges):
            if occ_range[0] >= i[0] and occ_range[1] <= i[1]:
                intersected_ranges[indx] = True
                occ_range = i
            elif occ_range[0] >= i[0]:
                occ_range[0] = i[0]
                intersected_ranges[indx] = True
            elif occ_range[1] <= i[1]:
                occ_range[1] = i[1]
                intersected_ranges[indx] = True
            elif occ_range[0] < i[0] and occ_range[1] > i[1]:
                intersected_ranges[indx] = True
        occupied_ranges = [occupied_ranges[i] for i in range(len(occupied_ranges)) if not intersected_ranges[i]]
        occupied_ranges.append(occ_range)

print(occupied_ranges)
print(abs(occupied_ranges[0][0]-occupied_ranges[0][1]))