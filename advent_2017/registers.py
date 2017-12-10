from collections import defaultdict
from operator import lt, gt, le, ge, eq, ne 
import inputs

def compare(registers, lhs, condition, rhs):
    ops = {'<': lt,
           '>': gt,
           '<=': le,
           '>=': ge,
           '==': eq,
           '!=': ne}
    return ops[condition](registers[lhs], int(rhs))

def execute(registers, lhs, action, rhs):
    if action == 'inc':
        registers[lhs] += int(rhs)
    elif action == 'dec':
        registers[lhs] -= int(rhs)
    return registers

registers = defaultdict(int)
alltime_max = 0
for line in inputs.registers.split('\n'):
    lhs1, action, rhs1, _, lhs2, condition, rhs2 = line.split()
    if compare(registers, lhs2, condition, rhs2):
        registers = execute(registers, lhs1, action, rhs1)
    alltime_max = max(alltime_max, max(registers.values()))

print(max(registers.values()))
print(alltime_max)
