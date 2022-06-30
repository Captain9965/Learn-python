#sometimes backward iteration can be useful, one can use reversed() for this:
print("----------------------------using reversed() method:----------------------------------")

for i in reversed(range(0, 10)):
    print(i)
print("--------------------------------using conventional range():-------------------------")

for i in range(9, -1, -1):
    print(i)

print("-------------------------using slice syntax:----------------------------------------")
k = range(10)[::-1]
print(k)

for i in k:
    print(i)