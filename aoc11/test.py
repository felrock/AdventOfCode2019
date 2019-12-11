import sys
import collections

# usage: python3 11.1.py program-file initial-square-color

# intCode computer (generator interface, yields outputs, gets inputs from list)
def run(inp):
    initmem = list(map(int, open(sys.argv[1]).read().split(',')))
    mem = collections.defaultdict(lambda: 0, enumerate(initmem))
    pc,base = 0, 0
    while mem[pc] != 99:
        opcode = mem[pc] % 100
        print(pc)
        modes = ("%05d" % mem[pc])[0:3]
        o1 = base if modes[2] == '2' else 0
        o2 = base if modes[1] == '2' else 0
        o3 = base if modes[0] == '2' else 0
        if opcode in (1,2,3,4,5,6,7,8,9):
            op1 = mem[pc+1] if modes[2] == '1' else mem[o1+mem[pc+1]]
        if opcode in (1,2,5,6,7,8):
            op2 = mem[pc+2] if modes[1] == '1' else mem[o2+mem[pc+2]]
        if opcode in (1,2): # add and mul
            f = {1: int.__add__, 2: int.__mul__}[opcode]
            mem[o3+mem[pc+3]] = f(op1,op2)
            pc += 4
        elif opcode == 3: # input
            mem[o1+mem[pc+1]] = inp.pop(0)
            pc += 2
        elif opcode  == 4: # output
            pc += 2
            yield op1
        elif opcode == 5: # jump if true
            pc = op2 if op1 != 0 else pc+3
        elif opcode == 6: # jump if false
            pc = op2 if op1 == 0 else pc+3
        elif opcode == 7: # less than
            mem[o3+mem[pc+3]] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8: # equals
            mem[o3+mem[pc+3]] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 9: # set relative base
            base += op1
            pc += 2
        else: raise Exception("invalid opcode %d" % opcode)

# painting robot, supports infinite grid as a dict for (x,y):color
pipe = list()
robot = run(pipe)
hull = collections.defaultdict(lambda: 0)
hull[(0,0)] = int(sys.argv[2])
d, x, y = 0, 0, 0
dirs = ((0,-1), (1,0), (0,1), (-1,0))
minx,maxx,miny,maxy = 0, 0, 0, 0
try:
    while True:
        pipe.append(hull[(x,y)])
        color = next(robot)
        turn = next(robot)
        hull[(x,y)] = color
        d = (d+1)%4 if turn == 1 else (d-1)%4
        dx, dy = dirs[d]
        x, y = x+dx, y+dy
        minx,maxx,miny,maxy = min(x,minx),max(x,maxx),min(y,miny),max(y,maxy)
except StopIteration:
    pass

# answer part 1
print(len(hull.keys()))
