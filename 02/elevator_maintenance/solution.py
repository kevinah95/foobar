'''
Ref: https://stackoverflow.com/a/2574090/4752488
'''
def answer(l):
    l.sort(key=lambda s: list(map(int, s.split('.'))))
    return l

# l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# print(answer(l))

# l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# print(answer(l))