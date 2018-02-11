import math

BOTTOM_LEFT = (0, 0)
TOP_RIGHT = (3, 2)

SOURCE = (1, 1)
TARGET = (2, 1)

def get_mirrored(point):
    ret = []

    # mirror at top wall
    # x1 , y1 - 2 * ( y1 - b ) 
    ret.append((point[0], point[1] - 2*(point[1] - TOP_RIGHT[1])))
    # mirror at bottom wall
    ret.append((point[0], point[1] - 2*(point[1] - BOTTOM_LEFT[1])))
    # mirror at left wall
    ret.append((point[0] - 2*(point[0] - BOTTOM_LEFT[0]), point[1]))
    # mirror at right wall
    ret.append((point[0] - 2*(point[0] - TOP_RIGHT[0]), point[1]))
    return ret

#print(get_mirrored(TARGET))

def get_targets(start_point, distance):

    all_targets = set((start_point, ))  # will also be the return value ...(2,1)
    last_targets = all_targets          # need to memorize the new points

    while True:
        new_level_targets = set()  # if this is empty: break the loop
        for tgt in last_targets:   # loop over what the last iteration found
            new_targets = get_mirrored(tgt)
            
            ''' for i in range(len(new_targets)):
                new_targets[i] = (new_targets[i][0] - SOURCE[0],new_targets[i][1] - SOURCE[1])
            print(new_targets) '''
            # only keep the ones within range
            new_targets = set(
                t for t in new_targets
                if math.hypot(SOURCE[0]-t[0], SOURCE[1]-t[1]) <= DISTANCE)
                # if math.hypot((SOURCE[0]-t[0])-SOURCE[0], (SOURCE[1]-t[1])-SOURCE[1] ) <= DISTANCE)
            # subtract the ones we already have
            new_targets -= all_targets
            new_level_targets |= new_targets
        if not new_level_targets:
            break
        # add the new targets
        all_targets |= new_level_targets
        last_targets = new_level_targets  # need these for the next iteration

    return all_targets

DISTANCE = 4    

all_targets = get_targets(start_point=TARGET, distance=DISTANCE)
print( (all_targets))