
for a in [1,3,4,5,2]:
    print(a)

a = [1,2,4,3,9]

for i,value in enumerate(a):
    print(f"Index,Value :{i}, {value}")

def call_me(x):
    print("I called you");
    print(f"Value of passed argument : {x}")
    if x == 3:
        return x
    return call_me(x-1)

y = call_me(4);
print(f"Value of y : {y}")
