#!/usr/bin/env python3
#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=315&page=show_problem&problem=1597
import sys

def solve(input_sequence):
    """ Compute smallest number of elements which yield maximum sum.
    For non negative integers, this means get all numbers but zeros!.
    If input is all zeros, return zero
    """
    l=[x for x in input_sequence if x!=0]
    if not l:
        l=[0]#input is all zeros
    return l

def parse_input(input_size):
    input_sequence=[]
    for line_num in range(input_size):
        input_sequence.append(int(sys.stdin.readline()))
    return input_sequence

def display(output):
    num_elements=len(output)
    for element in output[:num_elements-1]:
        print(element,end=' ')
    print(output[-1])

        
while True:
    line=sys.stdin.readline()
    if not line:
        break
    input_size=int(line)
    input_sequence=parse_input(input_size)
    if input_sequence:
        output=solve(input_sequence)
        display(output)
