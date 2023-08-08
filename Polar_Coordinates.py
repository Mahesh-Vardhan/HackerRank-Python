import math

inp = input()
inp_complex = complex(inp)  
r = abs(inp_complex) 
theta = math.atan2(inp_complex.imag, inp_complex.real)

print(f"{r}")
print(f"{theta}")
