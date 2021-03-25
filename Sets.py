

# sets le list ko jastai kaam garxa, syntax in similar hunxa tara just like real sets in maths, elements repeat
#    hunna ani "[]" ko satta "{}" use hunxa ani yesari ni lekhna milxa: {sadasdasd ["asdasdas", "dasdasd"]}

a = set()
a.add(1)
a.union({1, 2 })
a1 = a.union({1, 2, 3})

print(max(a))
a.remove(1)
print(a)
print(a.isdisjoint(a1))
