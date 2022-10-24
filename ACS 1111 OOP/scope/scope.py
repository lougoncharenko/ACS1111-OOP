# global scope

# variables created outside of a function are
# global and can be accessed by an function in the program

# what happens when a variable is defined in a block?
for i in range (1,10):
    print (f"i: {i}")

print(i)


# local variable

def test_local_var():
    local = 'hi'
    print('hi')

test_local_var()
# print local will produce a name error because its a local var
print (local) 


# parameter vatriables

def count_to(n):
    for i in range(1,n):
         print (f"i: {i}")
    print(i)

count_to(5) #works
print(n) #error
print(i) #error

