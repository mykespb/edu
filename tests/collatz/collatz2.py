#!/usr/bin/env python3.9
# Mikhail Kolodin 2021-08-04 2021-08-10 4.2

# solving Collatz problem... well, showing it :)
# non-recursive version

# limit of calculations
LIM = 500

# output file for .dot data
of = "collatz2.gv"

todo = []    # list of todo numbers
done = []    # list of done numbers
para = []    # pairs of numbers done: "from -> to;""

def test(n):
    """ process number n and plan next number """
    global todo, done, para
    print(n)
    if n in done:
        return
    itodo = n*3+1 if n%2 else n//2
    done.append(n)
    para.append((n, itodo))
    if itodo not in todo:
        todo.append(itodo)

def main(args):
    """ organize work """
    global todo, done, para
    print("filling start")
    todo = [i for i in range(1, LIM+1)]
    print("todo:", todo, "\ndoing all the rest...")
    while todo:
        test(todo.pop(0))
    print("done:", done)
    print("pre-para:", para)
    para = [ (x[0], x[1]) for x in para if x[0] <= LIM and x[1] <= LIM]
    print("post-para:", para)
    draw()

def draw():
    """ prepare data for .dot file """
    with open(of, 'w') as f:
        f.write("digraph G {\n")
        for k, v in para:
            f.write(f"{k} -> {v};\n")
        f.write("}\n")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
