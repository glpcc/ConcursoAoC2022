import re
import math
# import cProfile
f = open("input.txt")
numbers = [[int(j) for j in re.findall("\d+",i)] for i in f.readlines()]

blueprints = [{
    "id": i[0],
    "ore_robot": i[1],
    "clay_robot": i[2],
    "ore_obsidian_robot":i[3],
    "clay_obsidian_robot":i[4],
    "ore_geode_robot":i[5],
    "obsidian_geode_robot":i[6],
}
 for i in numbers] 

# 0 = ore robot, 1= clay_robot, 2=obsidian_robot, 3=geode_robot
def calculate_num_geodes(robot: int,blueprint: dict, info: tuple = (32,1,0,0,0,0,0,0,0)):
    # print(list_robots)
    mins = info[0]
    ore_robots = info[1]
    clay_robots = info[2]
    obsidian_robots = info[3]
    geode_robots = info[4]
    ore = info[5]
    clay = info[6]
    obsidian = info[7]
    geodes = info[8]
    passed_mins = 0
    if mins == 1:
        return -1
    if robot == 0:
        if ore >= blueprint["ore_robot"]:
            passed_mins = 1
            ore -= blueprint["ore_robot"]
        else:
            passed_mins = math.ceil((blueprint["ore_robot"]-ore)/ore_robots) + 1
            if passed_mins < mins:
                ore -= blueprint["ore_robot"]
    elif robot == 1:
        if ore >= blueprint["clay_robot"]:
            passed_mins = 1
            ore -= blueprint["clay_robot"]
        else:
            passed_mins = math.ceil((blueprint["clay_robot"]-ore)/ore_robots) + 1
            if passed_mins < mins:
                ore -= blueprint["clay_robot"]
    elif robot == 2:
        if ore >= blueprint["ore_obsidian_robot"] and clay >= blueprint["clay_obsidian_robot"]:
            passed_mins = 1
            ore -= blueprint["ore_obsidian_robot"]
            clay -= blueprint["clay_obsidian_robot"]
        else:
            if clay_robots > 0:
                passed_mins = max(math.ceil((blueprint["ore_obsidian_robot"]-ore)/ore_robots) + 1,math.ceil((blueprint["clay_obsidian_robot"]-clay)/clay_robots) + 1)
                if passed_mins < mins:
                    ore -= blueprint["ore_obsidian_robot"]
                    clay -= blueprint["clay_obsidian_robot"]
            else:
                # Would never have clay
                return -1
    elif robot == 3:
        if ore >= blueprint["ore_geode_robot"] and obsidian >= blueprint["obsidian_geode_robot"]:
            passed_mins = 1
            ore -= blueprint["ore_geode_robot"]
            obsidian -= blueprint["obsidian_geode_robot"]
        else:
            if obsidian_robots > 0:
                passed_mins = max(math.ceil((blueprint["ore_geode_robot"]-ore)/ore_robots) + 1,math.ceil((blueprint["obsidian_geode_robot"]-obsidian)/obsidian_robots) +1)
                if passed_mins < mins:
                    ore -= blueprint["ore_geode_robot"]
                    obsidian -= blueprint["obsidian_geode_robot"]
            else:
                # Would never have obsidian
                return -1
    # Calculate the generated resources
    # Check if all robots are generated in time
    if passed_mins >= mins:
        return -1
    else:
        ore += ore_robots*passed_mins
        clay += clay_robots*passed_mins
        obsidian += obsidian_robots*passed_mins
        geodes += geode_robots*passed_mins
        if robot == 0:
            ore_robots += 1
        elif robot == 1:
            clay_robots += 1
        elif robot == 2:
            obsidian_robots += 1
        elif robot == 3:
            geode_robots += 1
        mins -= passed_mins
    return geode_robots*mins+geodes, (mins,ore_robots,clay_robots,obsidian_robots,geode_robots,ore,clay,obsidian,geodes)    

def is_helpful(robot,blueprint,info,max_geodes):
    mins = info[0]
    ore_robots = info[1]
    clay_robots = info[2]
    obsidian_robots = info[3]
    geode_robots = info[4]
    ore = info[5]
    clay = info[6]
    obsidian = info[7]
    geodes = info[8]
    time_to_robot = 0
    # Check if could even produce more geodes
    posible_geodes = geode_robots*mins + ((mins-1)*(mins-2))/2 + geodes
    if posible_geodes < max_geodes:
        return False
    if robot == 0:
        if ore_robots >= 4:
            return False
        if ore >= blueprint["ore_robot"]:
            time_to_robot = 1
        else:
            time_to_robot = math.ceil((blueprint["ore_robot"]-ore)/ore_robots) + 1
    elif robot == 1:
        if clay_robots >= blueprint["clay_obsidian_robot"]:
            return False
        if ore >= blueprint["clay_robot"]:
            time_to_robot = 1
        else:
            time_to_robot = math.ceil((blueprint["clay_robot"]-ore)/ore_robots) + 1
    elif robot == 2:
        if obsidian_robots >= blueprint["obsidian_geode_robot"]:
            return False
        if ore >= blueprint["ore_obsidian_robot"] and clay >= blueprint["clay_obsidian_robot"]:
            time_to_robot = 1
        else:
            if clay_robots > 0:
                time_to_robot = max(math.ceil((blueprint["ore_obsidian_robot"]-ore)/ore_robots) + 1,math.ceil((blueprint["clay_obsidian_robot"]-clay)/clay_robots) + 1)
            else:
                return False
    elif robot == 3:
        if ore >= blueprint["ore_geode_robot"] and obsidian >= blueprint["obsidian_geode_robot"]:
            time_to_robot = 1
        else:
            if obsidian_robots > 0:
                time_to_robot = max(math.ceil((blueprint["ore_geode_robot"]-ore)/ore_robots) + 1,math.ceil((blueprint["obsidian_geode_robot"]-obsidian)/obsidian_robots) +1)
            else:
                return False
    
    if time_to_robot >= mins:
        return False
    else:
        return True

test_cache = {}
def calculate_max(next_item,blueprint,list_length,info = (32,1,0,0,0,0,0,0,0)):
    # func_hash = (next_item,info)
    # if func_hash in test_cache:
    #     return test_cache[func_hash]
    # print(current_list)
    if list_length < 3:
        print(list_length)
    m = calculate_num_geodes(next_item,blueprint,info)
    if m == -1:
        return -1

    m,info = m
    for i in range(3,-1,-1):
        if is_helpful(i,blueprint,info,m):
            m = max(m,calculate_max(i,blueprint,list_length+1,info))
    # test_cache[func_hash] = m
    return m

    

print(blueprints[0])
# print(calculate_num_geodes(0,blueprints[0]))
# with cProfile.Profile() as profile:
#     print(calculate_max(0,blueprints[1],0))
# profile.print_stats(sort="tottime")
tot_sum = 1
for i in blueprints[0:3]:
    temp = calculate_max(0,i,1)
    print("TEMP1")
    temp = max(temp,calculate_max(1,i,1))
    print("TEMP2")
    test_cache.clear()
    print('AVISO!!!!!!!!!!!!!!!!!!!!',temp)
    tot_sum *= temp

print(tot_sum)

