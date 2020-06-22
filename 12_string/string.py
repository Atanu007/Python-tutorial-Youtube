#Strings Array

a = "Hello world"

# 0  1  2  3  4  5
#[h][e][l][l][] [w]
#010101010   0101010     0101010    01010    01010

print(a[1])

#Slicing

print(a[6:11])

#Negative indexing

print(a[-11:-5])

#String Length

print(len(a))

#String methods
print(a.upper())
print(a.strip())

# Check if it String are a string variable
txt = "qweqweqweqw eqwe qwe john qw eqwe qefiowjdfjqdjpidg"
x = "john" in txt
print(x)

# String Concatenation

firstname = "加賀屋"
lastname = 'ジャン'
fullname = firstname + lastname

print(fullname)