from collections import defaultdict
import sys

# debug
verbose = 0

# operations
ADD   = 1
MUL   = 2
INP   = 3
OUT   = 4
JMPT  = 5
JMPF  = 6
LE    = 7
EQ    = 8
RPTR  = 9
HALT  = 99

# steps
BIG_STEP = 4
JMP_STEP = 3
SML_STEP = 2

# modes
POS = 0
INTR= 1
REL = 2

class IntCode():

    def __init__(self, file_name):
        # init machine
        self.mem  = defaultdict(lambda:0)
        self.pc   = 0
        self.r    = 0
        self.halt = False

        # load code
        f = open(file_name, 'r')
        string = f.readline().split(',')
        codes = list(map(int, string))
        for i in range(len(codes)):
            self.mem[i] = codes[i]

    def getState(self):
        return self.pc, self.r, self.mem.copy()

    def setState(self, state):
        self.pc  = state[0]
        self.r   = state[1]
        self.mem = state[2]

    def run(self, sig_in=None):
        # int code iteration

        while True:

            # get op code
            OP = self.getOpcode()
            if verbose:
                print('Current OP: ', OP, 'full: ', self.mem[self.pc])

            if OP == ADD:
                p1, p2, p3 = self.getMode(self.mem[self.pc])
                if verbose:
                    print('ADD', p1, p2)

                self.mem[p3] = self.mem[p1] + self.mem[p2]
                self.pc += BIG_STEP

            elif OP == MUL:
                p1, p2, p3 = self.getMode(self.mem[self.pc])
                if verbose:
                    print('MUL', p1, p2)

                self.mem[p3] = self.mem[p1] * self.mem[p2]
                self.pc += BIG_STEP

            elif OP == INP:
                p1, _, _ = self.getMode(self.mem[self.pc])

                self.mem[p1] = sig_in
                if verbose:
                    print('INP', sig_in)

                self.pc += SML_STEP

            elif OP == OUT:
                p1, _, _ = self.getMode(self.mem[self.pc])
                if verbose:
                    print('OUT', p1)

                self.pc += SML_STEP
                return self.mem[p1]

            elif OP == JMPT:
                p1, p2, _ = self.getMode(self.mem[self.pc])
                if verbose:
                    print('JMPT', p1, p2)

                if self.mem[p1] != 0:
                    self.pc = self.mem[p2]
                else:
                    self.pc += JMP_STEP

            elif OP == JMPF:
                p1, p2, _ = self.getMode(self.mem[self.pc])
                if verbose:
                    print('JMPF', p1, p2)

                if self.mem[p1] == 0:
                    self.pc = self.mem[p2]
                else:
                    self.pc += JMP_STEP

            elif OP == LE:
                p1, p2, p3 = self.getMode(self.mem[self.pc])
                if verbose:
                    print('LE', p1, p2)

                if self.mem[p1] < self.mem[p2]:
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                self.pc += BIG_STEP

            elif OP == EQ:
                p1, p2, p3 = self.getMode(self.mem[self.pc])
                if verbose:
                    print('EQ', p1, p2)

                if self.mem[p1] == self.mem[p2]:
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                self.pc += BIG_STEP

            elif OP == RPTR:
                p1, _, _ = self.getMode(self.mem[self.pc])
                if verbose:
                    print('RPTP', p1)

                self.r += self.mem[p1]
                self.pc += SML_STEP

            elif OP == HALT:
                self.halt = True
                break
            else:
                print('Op-code error,',self.mem[self.pc])
                sys.exit()

    def getMode(self, op):
        # Parse from opcode
        v1, v2, v3 = 0, 0, 0
        op_string = ('0'*5)+str(op)
        f1 = int(op_string[-3])
        f2 = int(op_string[-4])
        f3 = int(op_string[-5])
        if verbose:
            print('modes:', f1, f2, f3, op_string)

        # First parameter
        if f1 == POS:
            v1 = self.mem[self.pc + 1]
        elif f1 == INTR:
            v1 = self.pc + 1
        else:
            v1 = self.r + self.mem[self.pc + 1]

        # Second parameter
        if f2 == POS:
            v2 = self.mem[self.pc + 2]
        elif f2 == INTR:
            v2 = self.pc + 2
        else:
            v2 = self.r + self.mem[self.pc + 2]

        # Third parameter
        if f3 == REL:
            v3 = self.r + self.mem[self.pc + 3]
        else:
            v3 = self.mem[self.pc + 3]

        if verbose:
            print('Parameter values:', v1, v2, v3)

        return v1, v2, v3

    def getOpcode(self):
        return self.mem[self.pc] % 100












