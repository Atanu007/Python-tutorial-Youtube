


# Build in Data type on python


#text Type:    str x = "john"
#Numeric Type: int float complex    x = 1 , x = 10.23 m x = ij
#Sequence Type:  list, tuples , range
#Mapping Type:  dict 
#Set Type: set , frozenset
#Boolean Type: bool
#Binary Types: bytes, bytearray, memory view  


#Example Setting the Data Type
x = "Hello World"    #str
x = 220                 # int
x = 230.5                #float
x = 1j                  #complex
x = ["tuna", "banana", "cherry"]  #list
x = ("tuna", "banana", "cherry")  #tuple
x = range(6)                        #range
x = {"name" : "John", "age" : 26}   #dict
x = {"tuna", "banana", "cherry"}   #set
x = frozenset({"tuna", "banana", "cherry"}) #frozenset
x = True     #bool
x = b"Hello"  #bytes
x = bytearray(4)   #bytearray
x = memoryview(bytes(23))  # memoryview


#Setting the Specific Data Type

x = str("Hello World")    #str
x = int(220)                 # int
x = float(230.5)                #float
x = complex(1j)                  #complex
x = list(("tuna", "bacon", "cherry")) #list
x = tuple(("tuna", "bacon", "cherry")) #tuple
x = range(6)                        #range
x = dict(name="John", age=36)   #dict
x = set(("tuna", "bacon", "cherry"))   #set
x = frozenset(("tuna", "bacon", "cherry")) #frozenset
x = bool(5)     #bool
x = bytes(15)  #bytes
x = bytearray(25)   #bytearray
x = memoryview(bytes(25))  # memoryview