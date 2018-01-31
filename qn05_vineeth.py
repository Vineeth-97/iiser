def poly(x, roots):
    pdt = 1
    for r in roots:
        pdt *= (x-r)
    return pdt


roots = [1, 2]

print(poly(1.1, roots))
