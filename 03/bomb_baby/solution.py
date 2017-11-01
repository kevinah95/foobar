
''' REF: https://math.stackexchange.com/a/2070057 '''
def minimise(a, b):
    level = -1
    while b:
        cont, a = divmod(a, b)
        level += cont  # cont is the next item in the continued fraction
        a, b = b, a  # Swapping is the same as the reciprocal
    # This also acts as the Euclidean algorithm, where if a != 1,
    # a / b is not in their simplest form (As a is their GCD)
    if a != 1:
        return "impossible"
    return str(level)

def answer(M,F):
  return minimise(int(M),int(F))

print minimise(10**48,7**45)
print minimise(10**48,8**45)
print(minimise(2,4))
print(minimise(2,1))
print(minimise(4,7))
