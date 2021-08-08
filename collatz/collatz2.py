#!/usr/bin/env python3.9
# Mikhail Kolodin 2021-08-04 2021-08-06 4.1

# solving Collatz problem... showing it :)
# non-recursive version

LIM = 500

of = "collatz2.gv"

todo = []
done = []
para = []

def test(n):
    """ process n """
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
    """ organize """
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
    """ make dot task """
    with open(of, 'w') as f:
        f.write("digraph G {\n")
        for k, v in para:
            f.write(f"{k} -> {v};\n")
        f.write("}\n")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
