import pickle
import pickletools
class test:
    def __init__(self):
        self.people = 'a'

a= test()

serialized = pickle.dumps(a,protocol=0)

print(serialized)
# print(pickletools.optimize(serialized))
# print(pickletools.dis(serialized,annotate=1))
# print(pickletools.genops(serialized))
b = b'ccopy_reg\n_reconstructor\np0\n(c__main__\ntest\np1\nc__builtin__\nobject\np2\nNtp3\nRp4\n(dp5\nVpeople\np6\nVa\np7\nsb.'
print(pickle.loads(b))
print(111)