a = ["a", "b"]
b = ["c", "d"]

print(f"{a=} {b=}")

a = b.copy()

print(f"{a=} {b=}")

a[0] = "g"

print(f"{a=} {b=}")