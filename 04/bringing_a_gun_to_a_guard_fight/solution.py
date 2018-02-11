import math



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
                if math.hypot(SOURCE[0]-t[0], SOURCE[1]-t[1]) <= distance)
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
    if(has_same_x):
        for t in all_targets:
            if(t[0] == SOURCE[0]):
                if(t != start_point):
                    temp_all.discard(t)
                
    return temp_all


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

dimensions = [300, 275]
your_position = [150, 150]
guard_position = [185, 100]
distance = 500

''' dimensions = [3, 2]
your_position = [1, 1]
guard_position = [2, 1]
distance = 4 '''

print (answer(dimensions, your_position, guard_position, distance))