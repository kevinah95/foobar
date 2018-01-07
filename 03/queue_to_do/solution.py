def result():
    from functools import reduce
    product = reduce((lambda x, y: x ^ y), [0, 1, 2, 3, 4])
    # product = 2
    #print product ^ 6

def answer2(start,length):
    first_column_array = [start]
    for i in range(length - 1):
        previous = first_column_array[-1]
        current = previous + length
        first_column_array.append(current)
    #print first_column_array
    diagonal = []
    for i in range(1, length):
        column_value = first_column_array[i]
        value = column_value - (i)
        diagonal.append(value)
    #for i in range(length):
    
    result = 0
    for x, y in map(None, first_column_array[:-1], diagonal):
        result = result^reduce((lambda x, y: x ^ y), range(x,y+1))
    result = result^first_column_array[-1]

    return result

def contador(start,max):
    n=start
    while n < max:
          yield n 
          n=n+1

def answer(start, length):
    acum = 0
    first_column_value = start
    for i in range(length):
        next_column_value = first_column_value + length
        last_column_value = next_column_value - (i+1)
        #print (i,first_column_value, last_column_value)
        contad = contador(first_column_value,last_column_value+1)
        for i in contad:
            acum = acum ^ i
        #acum = acum ^ reduce((lambda x, y: x ^ y), xrange(first_column_value,last_column_value+1))
        first_column_value = next_column_value
    return acum
    


def f(a):
     res = [a, 1, a+1, 0]
     print res[a%4]
     return res[a%4]

def getXor(a, b):
     return f(b) ^ f(a-1)
    
def gen_nums(start, length):
    l = length
    ans = 0
    while l > 0:
        ans^= getXor(start,start+l-1)
        start = start + length
        l = l - 1
    return ans
        

print gen_nums(17,4)