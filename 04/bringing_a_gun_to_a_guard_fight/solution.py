import math


def find_slope_and_y_intercept(a,b):
    m = calculate_slope(a,b)
    slope = calculate_y_intercept(b,m)
    cuadrant = calculate_quadrant(b)
    return (m,slope,cuadrant)

def calculate_y_intercept(a,slope):
    # y_intercept = y - m*x
    return a[1] - slope * a[0]

def calculate_slope(a,b):
    if(b[0]==a[0]): return 0
    # slope = ((y2-y1)/(x2-x1))
    return ((b[1]-a[1])/(b[0]-a[0]))

def calculate_quadrant(t):
    x = t[0]
    y = t[1]
    if (x > 0 and y > 0):
        return 1

    elif (x < 0 and y > 0):
        return 2
        
    elif (x < 0 and y < 0):
        return 3
    
    elif (x > 0 and y < 0):
        return 4

def get_mirrored(point,DIMENSIONS, source_point, target_point):
    ret = []

    # mirror at top wall
    # x1 , y1 - 2 * ( y1 - b ) 
    ret.append((point[0], point[1] - 2*(point[1] - DIMENSIONS[1])))
    # mirror at bottom wall
    ret.append((point[0], point[1] - 2*(point[1])))
    # mirror at left wall
    left_point = (point[0] - 2*(point[0]), point[1])
    ret.append(left_point)
    # mirror at right wall
    ret.append((point[0] - 2*(point[0] - DIMENSIONS[0]), point[1]))
    return ret

#print(get_mirrored(TARGET))

def get_targets(start_point, distance, DIMENSIONS, SOURCE):

    all_targets = set((start_point, ))  # will also be the return value ...(2,1)
    last_targets = all_targets          # need to memorize the new points
    has_same_y = validate_same_y(SOURCE,start_point)
    has_same_x = validate_same_x(SOURCE,start_point)
    while True:
        new_level_targets = set()  # if this is empty: break the loop
        for tgt in last_targets:   # loop over what the last iteration found
            new_targets = get_mirrored(tgt, DIMENSIONS,SOURCE,start_point)
            
            # only keep the ones within range
            new_targets = set(
                t for t in new_targets
                if math.hypot(SOURCE[0]-t[0], SOURCE[1]-t[1]) <= distance and not (t[0]==t[1]==0)) 
                # if math.hypot((SOURCE[0]-t[0])-SOURCE[0], (SOURCE[1]-t[1])-SOURCE[1] ) <= DISTANCE)
            # subtract the ones we already have
            new_targets -= all_targets
            new_level_targets |= new_targets
        if not new_level_targets:
            break
        # add the new targets
        all_targets |= new_level_targets
        last_targets = new_level_targets  # need these for the next iteration
    temp_all = set()
    temp_all |= all_targets
    if(has_same_y):
        for t in all_targets:
            if(t[1] == SOURCE[1]):
                if(t != start_point):
                    temp_all.discard(t)
                    if( validate_slope(SOURCE,start_point,t) ):
                        temp_all.discard(t)
    if(has_same_x):
        for t in all_targets:
            if(t[0] == SOURCE[0]):
                if(t != start_point):
                    temp_all.discard(t)
                    if( validate_slope(SOURCE,start_point,t) ):
                        temp_all.discard(t)
    ''' for t in all_targets:
        if(t != start_point):
            if( validate_slope(SOURCE,start_point,t) ):
                temp_all.discard(t) '''
    temp_all_2 = set()
    #temp_all_2 |= temp_all
    all_equations = set()
    for t in temp_all:
        new_equ = find_slope_and_y_intercept(SOURCE,t)
        #print (new_equ)
        #print(t)
        if(t == start_point):
            temp_all_2.add(t)
        elif(new_equ not in all_equations):
            temp_all_2.add(t)
            all_equations.add(new_equ)
                
    return (temp_all_2)


def answer(dimensions, your_position, guard_position, distance):
    dimensions_aux = (dimensions[0], dimensions[1])
    your_position_aux = (your_position[0], your_position[1])
    guard_position_aux = (guard_position[0], guard_position[1])

    all_targets = get_targets(start_point=guard_position_aux, distance=distance, DIMENSIONS=dimensions,SOURCE=your_position)
    return (all_targets)

def validate_same_y(your_position, guard_position):
    return your_position[1] == guard_position[1]

def validate_same_x(your_position, guard_position):
    return your_position[0] == guard_position[0]

def validate_slope(your_position, guard_position, other_point):
    m1 = 0
    m2 = 0
    if(other_point[0] != guard_position[0]):
        m1 = ((other_point[1]-guard_position[1])/(other_point[0]-guard_position[0]))
    b1 = other_point[1] - m1* other_point[0]
    if(other_point[0] != your_position[0]):
        m2 = ((other_point[1]-your_position[1])/(other_point[0]-your_position[0]))
    b2 = other_point[1] - m2 * other_point[0]
    return (m1==m2) and (b1==b2)

def round_two_decimals(t):
    return (round(t[0]),round(t[1]))

''' dimensions = [300, 275]
your_position = [150, 150]
guard_position = [185, 100]
distance = 500 '''

''' dimensions = [3, 2]
your_position = [1, 1]
guard_position = [2, 1]
distance = 4 '''

dimensions = [2,5]
your_position = [1, 2]
guard_position = [1,4]
distance = 11

answer_result = answer(dimensions, your_position, guard_position, distance)
print (answer_result)

import numpy as np
import matplotlib.pyplot as plt


zip(*answer_result)
plt.scatter(*zip(*answer_result))
plt.show()