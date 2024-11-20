info = {90: 'A', 80: 'B', 70: 'C'}
thekeys = list(info.keys())
thekeys.sort()
for key in thekeys:
    print(key, info[key])

print("____")

for key in info:
    print(key, info[key])
