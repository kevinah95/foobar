from __future__ import division
x1 = 2
x2 = 1
y1 = 1
y2 = 1
a = 3
b= 2

def first_equ(x1, x2, y1, y2):
    
    plus_plus_a = x2/2 + x1/2
    plus_plus_b = y2/2 + y1/2
    r0 = (plus_plus_a,plus_plus_b)
    minus_minus_a = x2/2 - x1/2
    minus_minus_b = y2/2 - y1/2
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a,plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def second_equ(x1, x2, y1, y2, b):
    
    plus_plus_a = x2/2 + x1/2
    plus_plus_b = b - (y2/2 + y1/2)
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = x2/2 - x1/2
    minus_minus_b = b - (y2/2 - y1/2)
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def third_equ(x1, x2, y1, y2, a):
    
    plus_plus_a = a - (x2/2 + x1/2)
    plus_plus_b = y2/2 + y1/2
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = a - (x2/2 - x1/2)
    minus_minus_b = y2/2 - y1/2
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

def fourth_equ(x1, x2, y1, y2, a, b):
    
    plus_plus_a = a - (x2/2 + x1/2)
    plus_plus_b =  b - (y2/2 + y1/2)
    r0 = (plus_plus_a, plus_plus_b)
    minus_minus_a = a - (x2/2 - x1/2)
    minus_minus_b = b - (y2/2 - y1/2)
    r1 = (minus_minus_a, minus_minus_b)
    r2 = (minus_minus_a, plus_plus_b)
    r3 = (plus_plus_a, minus_minus_b)

    return r0,r1,r2,r3

print(set( ( first_equ(x1, x2, y1, y2) + second_equ(x1, x2, y1, y2, b) + third_equ(x1, x2, y1, y2, a) + fourth_equ(x1, x2, y1, y2, a, b) ) ))


# (x2, x1, y2, y1)
# ( first_equ(x1, x2, y1, y2) + second_equ(x1, x2, y1, y2, b) + third_equ(x1, x2, y1, y2, a) + fourth_equ(x1, x2, y1, y2, a, b) )