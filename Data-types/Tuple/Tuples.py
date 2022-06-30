#like the list, it is a collection of ordered objects but it is immutable.
tp = ()
print(tp)

#creating a tuple of strings:
tp = ("Lenny", "Weda")
print(tp)
print("-------------------------intializing with a list--------------------")
#initializing with a list:
tp = ()
tp = (tuple(["lenny", "Weda", "Orengo"]))
print(tp)

#nested tuple:
print("-------------------------nested tuple-------------------------")
tp2 = ("year", "of ", "birth")
tp3 = (tp, tp2)
print(tp3)

print("---------------------------------element access:------------------------")
#element access:
print(tp[0])