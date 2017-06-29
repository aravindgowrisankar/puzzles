#!/usr/bin/env python3
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2267
import sys
import itertools

def cost_of_solution(dragon_knight_assignments,knight_heights):
    """ Cost owed to each knight equals the knight's height """ 
    return sum([knight_heights[i] for i in dragon_knight_assignments])
    
def valid_solution(dragon_knight_assignments,knight_heights,dragon_head_diameters):
    num_invalid=sum([ 1 if knight_heights[knight]<dragon_head_diameters[dragon] else 0 \
                          for dragon,knight in enumerate(dragon_knight_assignments)])
    return num_invalid==0

def brute_force(knight_heights,dragon_head_diameters):
    """ 
    Brute force solution. Enumerate all permutations of knight selections, compute costs, select minimum.
    """
    default=sum(knight_heights)+1
    
    num_dragons=len(dragon_head_diameters)
    num_knights=len(knight_heights)

    if num_dragons>num_knights:
        return "Loowater is doomed!"
    knights=range(num_knights)
    random_dragon_assignments=itertools.permutations(knights,len(dragon_head_diameters))

    min_cost=default
    costs=[cost_of_solution(dragon_assignment,knight_heights) 
           if valid_solution(dragon_assignment,knight_heights,dragon_head_diameters) else default
           for dragon_assignment in random_dragon_assignments]

    if len(costs)==0:
        return "Loowater is doomed!"
    min_cost=min(costs)
    
    if min_cost<default:
        return str(min_cost)
    else:
        return "Loowater is doomed!"


def greedy(knight_heights,dragon_head_diameters):
    """ Key insight: Sort both dragon head diameters and knight heights in asc order.
    Scan dragon heads from lowest to highest and find the first knight that can kill a dragon head.
    """
    num_solved=0
    
    num_dragon_heads=len(dragon_head_diameters)
    num_knights=len(knight_heights)

    if num_dragon_heads>num_knights:
        return "Loowater is doomed!"
    
    knight_heights=sorted(knight_heights)
    dragon_head_diameters=sorted(dragon_head_diameters)
    
    min_cost=0
    knight_counter=0
    dragon_counter=0

    while dragon_counter<num_dragon_heads and knight_counter<num_knights:
        while knight_counter<num_knights:
            if knight_heights[knight_counter]>=dragon_head_diameters[dragon_counter]:
                num_solved+=1
                min_cost+=knight_heights[knight_counter]
                knight_counter+=1
                break
            else:
                knight_counter+=1

        dragon_counter+=1

    if num_solved!=num_dragon_heads:
        return "Loowater is doomed!"
    else:
        return str(min_cost)

def parse_input(heads,knights):
    knight_heights=[]
    dragon_head_diameters=[]

    if heads==0 and knights==0:
        return knight_heights,dragon_head_diameters

    for line_num in range(heads):
        dragon_head_diameters.append(int(sys.stdin.readline()))

    for line_num in range(knights):
        knight_heights.append(int(sys.stdin.readline()))

    return knight_heights,dragon_head_diameters


while True:
    line=sys.stdin.readline()
    if not line or line.strip()=="0 0":
        break
    line_array=line.split(" ")
    heads,knights=int(line_array[0]),int(line_array[1])
    knight_heights,dragon_head_diameters=parse_input(heads,knights)
    output=greedy(knight_heights,dragon_head_diameters)
    print(output)
