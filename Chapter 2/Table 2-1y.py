# Table 2-1.

xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

print("{:<10} Time (s)".format("N"))
print("-"*20)
for i in range(3):
    print("{:<10} {}".format(xs[i], ys[i]))