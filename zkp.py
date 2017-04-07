p = int(raw_input("enter the value of p"))
print p

q = int(raw_input("enter the value of q"))
print q

print "computing N"

N = p * q
print "N: ", N

priv1 = int(raw_input("enter the value of priv1 for alice"))
print priv1

priv2 = int(raw_input("enter the value of priv2 for alice"))
print priv2

print "the private key for alice {priv1,priv2} is", (priv1, priv2)

pub1 = int(raw_input("enter the value of pub1 for alice"))
print pub1

pub2 = int(raw_input("enter the value of pub2 for alice"))
print pub2

print "the private key for alice {pub1,pub2} is", (pub1, pub2)

j = priv1 **2
k = j * pub1
r = k % N
print "r: ", r

h = priv2 **2
i = h * pub2
m = i % N
print "m: ", m

#end of part 1#

#part 2, alice computes A,B,C and sends to bob#

print "select three random numbers a, b, c"
a = int(raw_input("enter the value of a"))
print a
b = int(raw_input("enter the value of b"))
print b
c = int(raw_input("enter the value of c"))
print c

print "the values of {a,b,c} are", (a, b, c)

A = (a**2) % N
B = (b**2) % N
C = (c**2) % N

print "Alice sends bob {A,B,C}", (A, B, C)

#end of part2#

#part3, bob sends alice a matric and alice computes and sends it back to bob#

w = priv1**0
x = priv1**1
y = priv2**0
z = priv2**1
print "computing M,P,Q........."
print a, b, c
M = (a*(w*z)) % N
P = (b*(x*y)) % N
Q = (c*(x*z)) % N

print "alice sends bob {M,P,Q}", (M,P,Q)

#end of part3#

#part4, bob verifies alice's values#
s = pub1**0
t = pub1**1
u = pub2**0
v = pub2**1
e = M**2
f = P**2
g = Q**2
S = (e*(s*v)) % N
T = (f*(t*u)) % N
V = (g*(t*v)) % N

print "bob verifies {S,T,V}", (S, T, V)
