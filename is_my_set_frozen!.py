s1={1,2,4,0}
s1.add(-1)
print(s1,type(s1))

#frozen sets - immutable sets
fs1 = frozenset({10,20,30})
print(fs1,type(fs1))

#fs1.add(40)
print(fs1)
fs2=frozenset({10,50,100,200})
print(fs2,type(fs2))

print(fs1 & fs2)
print(fs1 | fs2)
print(fs1-fs2)
print(fs2-fs2)
