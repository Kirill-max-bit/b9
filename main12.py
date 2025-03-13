# a
a = "первое"
b = "второе"
c = "третье"
b, a, c = c, b, a
print(f"a: {a}, b: {b}, c: {c}")


# b
a = "первое"
b = "второе"
c = "третье"
b, c, a = a, b, c
print(f"a: {a}, b: {b}, c: {c}")
