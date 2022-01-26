# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import numpy

def soln_eqn(ar1,b1):
    d1=numpy.linalg.det(ar1)
    ar2=[]
    for i in range(len(ar1)):
        ar2.append([])
        for j in range(len(ar1[i])):
            if j==0:
                ar2[-1].append(b1[i])
            else:
                ar2[-1].append(ar1[i][j])
    ar2=numpy.array(ar2)
    d2=numpy.linalg.det(ar2)
    ar3=[]
    for i in range(len(ar1)):
        ar3.append([])
        for j in range(len(ar1[i])):
            if j==1:
                ar3[-1].append(b1[i])
            else:
                ar3[-1].append(ar1[i][j])
    ar3=numpy.array(ar3)
    d3=numpy.linalg.det(ar3)
    return [d2/d1 , d3/d1]

def linear_sparse(ar,b):
    sln=[]
    for i in range(len(ar[0])):
        sln.append([0]* len(ar[0]))
        if i!=(len(ar[0])-1):
            ar1=[]
            for j in range(len(ar)):
                ar1.append(ar[j][i:i+2])
            ar1=numpy.array(ar1)
            s=soln_eqn(ar1, b)
            sln[-1][i:i+2]=s

        else:
            ar1=[]
            for j in range(len(ar)):
                ar1.append([ar[j][-1],ar[j][0]])
            ar1=numpy.array(ar1)
            s=soln_eqn(ar1, b)
            sln[-1][-1]=s[0]
            sln[-1][0]=s[-1]
                
    return sln

def sparsity_set_0(ar,b):
    for i in range(len(ar)):
        if sum([j*0 for j in ar[i]])== b[i]:
                return True
    else:
        return False
    
def sparsity_set_1(ar,b):
    soln=[]
    t=b[0]/b[1]
    for i in range(len(ar[0])):
        if ar[0][i]/ar[1][i]==t:
            s=[0]*len(ar[0])
            s[i]=t
            soln.append(s)
    return soln

def sparsity_set_2(ar,b):
    soln=linear_sparse(ar, b)
    min_r=None; set_r=[]
    for i in soln:
        if min_r==None:
            min_r=sum([abs(j) for j in i])
            set_r.append(i)
        elif sum([abs(j) for j in i])==min_r:
            set_r.append(i)
        elif sum([abs(j) for j in i])<min_r:
            set_r=[]
            set_r.append(i)
    return set_r

a= [[0.5, 0.4, 0.8],[-0.7,0.2, 0.7]]
a=numpy.array(a)
b=[0.9,-0.5]
b=numpy.array(b)
if sparsity_set_0(a, b):
    print([0,0,0], "is the sparsest soln: ")

elif sparsity_set_1(a, b):
    print("Sparest solution(s) is(/are): ")
    for i in sparsity_set_1(a, b):
        print(i)

else:
    print("Sparest solution(s) is(/are): ")
    for i in sparsity_set_2(a, b):
        print(i)