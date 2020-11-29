#!/usr/bin/env python3

from solutions_45_49 import s45_table
from solutions_45_49 import s46_tablePrefix
from solutions_45_49 import s47_tableArbitrary

print("Solution 45: Truth Tables")
s45_table('and(A, or(A, B))')
print("Solution 46: Truth table for infix expressions")
s46_tablePrefix('A and (A or not B)')
s46_tablePrefix('A or not B')
s46_tablePrefix('not(A impl B)')
s46_tablePrefix('A and not (A xor not (A nand B))')
print("Solution 47: Truth table for arbitrary number of operands")
s47_tableArbitrary(['A', 'B', 'C'], 'A and (B or C) equ A and B or A and C')
s47_tableArbitrary(['A', 'B', 'C'], 'A and B and C')
s47_tableArbitrary(['A', 'B', 'C'], 'not A and not B and not C')
