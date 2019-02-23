#! /usr/bin/env python3
# arc1.py
# python3
# myke 2019-02-23 0.3
# arithmetic expressions solver
# given 1+2*3-4/5 count result
# use integer numbers, +-*/
# any spaces are allowed
# can signal errors (bad syntax, zdiv)
# extensions: (), ^, 2+-digits_integers, real_numbers, etc

import logging
logging.basicConfig (level = logging.DEBUG)

tests = (
"1",
"2 +3",
"1+2-3*4/5",
"1/0",
"",
)

class Task:
    text = ""       # text to process
    pos = -1        # position to start processing
    state = 0       # 0=OFF, 1=ON (working)

    oper = []       # operators stack
    vals = []       # values stack

    # eltypes:
    ET_NONE   = 0
    ET_NUMBER = 1
    ET_SIGN   = 2

    prio = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
    }

    digits = "0123456789"


    def __init__ (self, text):
        self.text = text
        self.alen = len (self.text)
        self.pos = 0
        self.state = 1 if self.alen else 0
        self.oper = []
        self.vals = []
        logging.debug ("task initiated")


    def give (self):
        """ give next char """

        if not self.state:
            return ""
        if self.pos == self.alen:
            self.state = 0
            return ""
        while self.state:
            logging.debug (f"pos={self.pos}")
            if self.pos >= self.alen :
                self.state = 0
                return ""
            if self.text [self.pos] not in " \t":
                outchar = self.text [self.pos]
                logging.debug (f"outchar={outchar}")
                self.pos += 1
                return outchar


    def __str__ (self):
        """ print me """

        return self.text


    def solve (self):
        """ calculate 1 expression """

        if not self.text:
            return 0
            # TBD: maybe exceptions?

        while self.state:
            eltype, elval = self.getelem ()
            logging.debug (f"eltype={eltype}, elval={elval}")

            if eltype == Task.ET_NUMBER:
                self.vals.append (elval)
            elif eltype == Task.ET_SIGN:
                newoper = (elval, Task.prio [elval])
                self.proc_oper (newoper)
                self.oper.append (newoper)
            else:
                break

        self.fin_oper ()

        return self.vals [0] if len (self.vals) else "bad expression"


    def getelem (self):
        """ get next lexem """

        c = self.give ()
        logging.debug (f"given c = [{c}]")
        if c in Task.prio:
            return (Task.ET_SIGN, c)
        elif c in Task.digits:
            return (Task.ET_NUMBER, c)
        else:
            return (Task.ET_NONE, c)


    def proc_oper (self, newoper):
        """ comparing new operator with contents of oper stack,
        execute necessary operators from oper stack with numbers from vals stack
        """
        pass


    def fin_oper (self):
       """ finalize processing of expression
       if there are unexecuted operators in oper stack
       """
       pass



def main ():
    """ main dispatcher """

    for test in tests:
        task = Task (test)
        print ("input expression:", task)
        result = task.solve ()
        print ("result:", result)


if __name__ == "__main__":
    main()
