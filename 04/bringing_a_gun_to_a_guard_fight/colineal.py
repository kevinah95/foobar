from __future__ import division

def find_slope_and_y_intercept(a,b):
    m = calculate_slope(a,b)
    b = calculate_y_intercept(a,m)
    return (m,b)

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

me = (1,2)
other = (-5,2)

a_set = set([(1.0, 1.0)])
new_equ = find_slope_and_y_intercept(me,other)
print(new_equ)