#while else loop:
a = [1, 2, 3, 4, 5, 6, 7]
while a:
    print(a.pop())
else:
    print("the list is now empty")
    print(a)

print("--------------------------for else loop---------------------------")
#for-else loop, note that a break statement will mean that the else is skipped
a = [10,9,8,7,6,5,4,3,3,2]
for i in a:
    print(i)
else:
    print("the list is over")

print("---------------------------The range function:---------------------")
# The arguments are start, stop, step:
for i in range(0, 10, 2):
    print(i)