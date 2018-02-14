import math

def common_factor(x,y):
    if x == 0:
        return 'inf'
    if y == 0:
        return 0
    big = max(x,y)
    small = min(x,y)
    while(small!=0):
        r = small
        small = big % r
        big = r
    return abs(big)

def calc_positions(dimensions, captain_position, badguy_position,origin_dict):
    captain_array = []
    badguy_array = []
    width = dimensions[0]
    height = dimensions[1]
    cx = captain_position[0]
    cy = captain_position[1]
    gx = badguy_position[0]
    gy = badguy_position[1]
    for x,y in origin_dict[(0,0)]:
        captain_array.append((x,y))
        badguy_array.append((x+gx-cx,y+gy-cy))
    for x,y in origin_dict[(1,0)]:
        captain_array.append((x+width-2*cx,y))
        badguy_array.append((x+width-gx-cx,y+gy-cy))
    for x,y in origin_dict[(0,1)]:
        captain_array.append((x,y+height-2*cy))
        badguy_array.append((x+gx-cx,y+height-gy-cy))
    for x,y in origin_dict[(1,1)]:
        captain_array.append((x+width-2*cx,y + height-2*cy))
        badguy_array.append((x+width-gx-cx,y + height-gy-cy))
    return captain_array,badguy_array

def calc_origins(dimensions, distance):
    origin_dict = {}
    origin_dict[(0,0)]=[]
    origin_dict[(1,0)]=[]
    origin_dict[(0,1)]=[]
    origin_dict[(1,1)]=[]
    width = dimensions[0]
    height = dimensions[1]
    w = (distance/width) + 1
    h = (distance/height) + 1
    for x in range(-w,w+1):
        for y in range(-h,h+1):
            if x % 2 == y % 2:
                if x % 2 == 0:
                    origin_dict[(0,0)].append((x*width,y*height))
                else:
                    origin_dict[(1,1)].append((x*width,y*height))
            else:
                if x % 2 == 0:
                    origin_dict[(0,1)].append((x*width,y*height))
                else:
                    origin_dict[(1,0)].append((x*width,y*height))
    return origin_dict

def filter_distance(listy,distance):
        return [x for x in listy if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    
def count_slopes(captain_list,badguy_list):
    global slopes_dict
    slopes_dict = {}
    for x,y in badguy_list:
        common = common_factor(x,y)
        if common == 0:
            if (0 not in slopes_dict or slopes_dict[0]>abs(x)):
                slopes_dict[0]= abs(x)
        elif common == 'inf':
            if ('inf' not in slopes_dict or slopes_dict['inf']>abs(y)):
                slopes_dict['inf']= abs(y)
        elif (x/common,y/common) not in slopes_dict or slopes_dict[(x/common,y/common)]>math.sqrt(x**2+y**2):
            slopes_dict[(x/common,y/common)]= math.sqrt(x**2+y**2)
    for x,y in captain_list:
        common = common_factor(x,y)
        if common == 0:
            if 0 in slopes_dict and slopes_dict[0]>abs(x):
                del slopes_dict[0]
        elif common == 'inf':
            if 'inf' in slopes_dict and slopes_dict['inf']>abs(y):
                del slopes_dict['inf']
        elif (x/common,y/common) in slopes_dict and slopes_dict[(x/common,y/common)]>math.sqrt(x**2+y**2):
            del slopes_dict[(x/common,y/common)]
    return slopes_dict

dimensions = [2,5]
your_position = [1, 2]
guard_position = [1,4]
distance = 11

def answer(dimensions, captain_position, badguy_position, distance):
    origins = calc_origins(dimensions, distance)
    captains,badguys = calc_positions(dimensions, captain_position, badguy_position,origins)
    captains = filter_distance(captains,distance)
    badguys = filter_distance(badguys,distance)
    slopes = count_slopes(captains,badguys)
    return len(slopes)

print answer(dimensions, your_position, guard_position, distance)