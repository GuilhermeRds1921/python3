# Remake the 035 challenge of the triangles,
# adding the ability to show what type of triangle will be formed:
# - Equilátero: all sides equal
# - Isóceles: two equal sides
# - Scalene: all different sides


a = float(input('First segment: '))
b = float(input('Second segment: '))
c = float(input('Third segment: '))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
elif c >= a and c >= b:
    maior = c

if maior > (a + b + c - maior):
    print('dont form a triangle')

else:
    print('form a trinagle')
    if a == b and a == c:
        print('Equilateral')
    elif a != b and a != c and b != c:
        print('Scalene')
    else:
        print('Isoceles')