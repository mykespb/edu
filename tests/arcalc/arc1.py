#! /usr/bin/env python3
# arc1.py
# python3
# myke 2019-02-23 1.1

# arithmetic expressions solver
# school example of parsing arithmetic expressions

# given 1+2*3-4/5 count result

# use integer numbers, +-*/
# any spaces are allowed
# can signal errors (bad syntax)
# zdiv is 0

# extensions: (), ^, 2+-digits_integers, real_numbers, etc
# maybe we'll 'add exceptions for zdiv etc


import logging
logging.basicConfig (level = logging.INFO)

class Task:
    text = ""       # text to process
    pos = -1        # position to start processing
    state = 0       # 0=OFF, 1=ON (working)

    oper = []       # operators stack
    vals = []       # values stack

    # ~ # eltypes:
    # ~ ET_NONE   = 0
    # ~ ET_NUMBER = 1
    # ~ ET_SIGN   = 2

    prio = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
    }

    digits = "0123456789"

    def _sum (a, b):
        return a+b

    def _sub (a, b):
        return a-b

    def _mult (a, b):
        return a*b

    def _div (a, b):
        return a//b if b else 0

    ops = {
    "+": _sum,
    "-": _sub,
    "*": _mult,
    "/": _div
    }


    def __init__ (self, text):
        """ make new task """

        self.text = text
        self.alen = len (self.text)
        self.pos = 0
        self.state = 1 if self.alen else 0
        self.oper = []
        self.vals = []


    def __str__ (self):
        """ print me """

        return self.text


    def simple_solve (self):
        """ solver for simple case
        with 1-digit numbers, integers only, +-*/,
        maybe with spaces
        """

        try:
            logging.debug (f"simple solver")

            for c in self.text:
                logging.debug (f"got char [{c}]")

                if c in Task.digits:
                    self.vals.append (int (c))
                    logging.debug (f"append int {c}")

                elif c in Task.prio:
                    newprio = Task.prio [c]
                    logging.debug (f"got oper {c, newprio}")
                    while len (self.oper) and self.oper [-1] [1] >= newprio:
                        logging.debug (f"exec stack len: vals={len(self.vals)}, oper={len(self.oper)}")
                        x2 = self.vals.pop ()
                        x1 = self.vals.pop ()
                        op = self.oper.pop() [0]
                        logging.debug (f"to do {(x1, op, x2)}")
                        fun = Task.ops [op]
                        opres = fun (x1, x2)
                        self.vals.append (opres)
                        logging.debug (f"make oper {op} result {opres}")
                    else:
                        logging.debug (f"bypass")
                    logging.debug (f"add oper start {(c, newprio)}")
                    self.oper.append ((c, newprio))
                    logging.debug (f"add oper done {(c, newprio)}")

            if len (self.oper):
                logging.debug (f"finalize start")
                while len (self.oper) and self.oper [-1] [1] >= newprio:
                    logging.debug (f"exec stack len: vals={len(self.vals)}, oper={len(self.oper)}")
                    x2 = self.vals.pop ()
                    x1 = self.vals.pop ()
                    op = self.oper.pop() [0]
                    logging.debug (f"to do {(x1, op, x2)}")
                    fun = Task.ops [op]
                    opres = fun (x1, x2)
                    self.vals.append (opres)
                    logging.debug (f"make oper {op} result {opres}")
                logging.debug (f"finalize end")

        except:
            return "bad expression"

        return self.vals[0] if len(self.vals) else "no data"


def main ():
    """ main dispatcher """

    for test in tests:
        task = Task (test)
        print ("\n--------------------------\ninput expression:", task)
        result = task.simple_solve ()
        print ("result:", result)


# test samples:

tests = (
"1",
"2 +3",
"1+2-3*4/5",
"2  3  + +",
"1/0",
"",
"   ",
)


if __name__ == "__main__":
    main()
