from __future__ import division
source= (1,1)
target = (2,1)
dimensions = (3,2)

def first_equ(source, target):
    
    plus_plus_a = target[0]/2 + source[0]/2
    plus_plus_b = target[1]/2 + source[1]/2
    r0 = (plus_plus_a,plus_plus_b)
    minus_minus_a = target[0]/2 - source[0]/2
    minus_minus_b = target[1]/2 - source[1]/2
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a,plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def second_equ(source, target, b):
    
    plus_plus_a = target[0]/2 + source[0]/2
    plus_plus_b = b - (target[1]/2 + source[1]/2)
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = target[0]/2 - source[0]/2
    minus_minus_b = b - (target[1]/2 - source[1]/2)
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def third_equ(source, target, a):
    
    plus_plus_a = a - (target[0]/2 + source[0]/2)
    plus_plus_b = target[1]/2 + source[1]/2
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = a - (target[0]/2 - source[0]/2)
    minus_minus_b = target[1]/2 - source[1]/2
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def fourth_equ(source, target, a, b):
    
    plus_plus_a = a - (target[0]/2 + source[0]/2)
    plus_plus_b =  b - (target[1]/2 + source[1]/2)
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = a - (target[0]/2 - source[0]/2)
    minus_minus_b = b - (target[1]/2 - source[1]/2)
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def validate_same_y(your_position, guard_position):
    return your_position[1] == guard_position[1]


def validate_same_x(your_position, guard_position):
    return your_position[0] == guard_position[0]





def answer(dimensions, your_position, guard_position, distance):
    
    source= (1,1)
    target = (2,1)
    dimensions = (dimensions[0], dimensions[1])
    source = (your_position[0], your_position[1])
    target = (guard_position[0], guard_position[1])
    
    has_same_y = validate_same_y(source,target)
    has_same_x = validate_same_x(source,target)

    all_targets = set( ( first_equ(source, target) + second_equ(source, target, dimensions[1]) + third_equ(source, target, dimensions[0]) + fourth_equ(source, target, dimensions[0], dimensions[1]) ) )
    temp_all = set()
    temp_all |= all_targets

    middle_x = (source[0] + target[0])/2
    middle_y = (source[1] + target[1])/2
    middle = (middle_x,middle_y)

    if(has_same_y):
        for t in all_targets:
            if(t[1] == source[1]):
                if(t != middle):
                    temp_all.discard(t)
    if(has_same_x):
        for t in all_targets:
            if(t[0] == source[0]):
                if(t != middle):
                    temp_all.discard(t)
    return len(temp_all)


dimensions = [300, 275]
your_position = [150, 150]
guard_position = [185, 100]
distance = 500

print (answer(dimensions, your_position, guard_position, distance))

# (target[0], source[0], target[1], source[1])
# ( first_equ(source[0], target[0], source[1], target[1]) + second_equ(source[0], target[0], source[1], target[1], b) + third_equ(source[0], target[0], source[1], target[1], a) + fourth_equ(source[0], target[0], source[1], target[1], a, b) )