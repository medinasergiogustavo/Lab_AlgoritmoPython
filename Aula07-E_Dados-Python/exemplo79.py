"""
Conjuntos (set)
"""

biomeleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print("Listagem da tupla biomoleculas = ", biomeleculas)
print("Listagem da tupla biomoleculas (sem repetição) = ",set(biomeleculas))


c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)  # elementos em comum
c4 = c1.difference(c2)    # c4 = {1,2}
c5 = c2.difference(c1)    # c5 = { 6,7}
c6 = c2.union(c1)         # c6 = {1,2,3,4,5,6,7}

print("Elementos em comum = ", c1.intersection(c2))

print("Elementos que estão no conjunto C1 e não no C2 = ", c1.difference(c2))
print("Elementos que estão no conjunto C2 e não no C1 = ",c2.difference(c1))
print("Soma dos Elementos que estão no conjunto C2 e no C1 = ",c2.union(c1))