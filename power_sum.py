#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/the-power-sum/problem
import sys

def listify(item):
    if not item:
        return item
    if not isinstance(item,list):
        new_list= [item]
    else:
        new_list=item
    return new_list

def recursive_solve(target,powers):
    if min(powers)>target:
        return []#no solution
    if len(powers)==1:
        if target in powers:
            return [target]
        else:
            return []#no solution
    else:
        #Compute solutions that contain the first  element
        element=powers.pop()

        new_solution_1=[]
        reduced_target=target-element
        if reduced_target==0:#element is the solution
            new_solution_1=[element]
        else:
            partial_1=recursive_solve(reduced_target,powers)
            for item in partial_1:
                new_solution_1.append([element]+listify(item))

       #Pick solutions that do not contain first element
        new_solution_2=recursive_solve(target,powers)
        answer=new_solution_1+new_solution_2
        powers.append(element)
        #print("In solve: target",target,"powers",powers,"answer",answer)
        return answer
        
def n_th_power_of_naturals_less_than_k(k,n):
    ans=[]
    for i in range(1,k+1):
        ans.append(pow(i,n))
    return ans

line=sys.stdin.readline()
x=int(line)
line=sys.stdin.readline()
n=int(line)

max_candidate=int(pow(x,1.0/n))
powers=n_th_power_of_naturals_less_than_k(max_candidate,n)


answer=recursive_solve(x,powers)
print(len(answer))
