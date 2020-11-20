#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:28:06 2020

@author: andrewqin
"""
global m
m = False
import numpy as np
import random
import time
print("")

def main():
    global arr
    arr = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype = np.int32)
    print("starting board: ")
    print("")
    print(arr)
    print("")
    print("--------------------------------")
    print("")
    print("play:")
    while(m==False):
        guessCheck()
        time.sleep(0.2)
        checkGameOver()
        time.sleep(0.2)
        if m==True:
            break
        time.sleep(0.2)
        guessCheckAnti()
        time.sleep(0.2)
        checkGameOver()
        time.sleep(0.2)
    print("Game Over")
    
def guessCheck():
    x = random.randint(0,2)
    y = random.randint(0,2)
    if arr[x,y]==0:
           arr[x,y]=1
    else:
        while(arr[x,y]!=0):
            x = random.randint(0,2)
            y = random.randint(0,2)
        arr[x,y]=1
        
    print(arr)
    print("--------------------------------")

def guessCheckAnti():
    x = random.randint(0,2)
    y = random.randint(0,2)
    if arr[x,y]==0:
           arr[x,y]=-1
    else:
        while(arr[x,y]!=0):
            x = random.randint(0,2)
            y = random.randint(0,2)
        arr[x,y]=-1
        
    print(arr)
    print("--------------------------------")

def checkGameOver():
    global m
    for x in range(0,3):
        if (arr[x,0]==1 and arr[x,1]==1 and arr[x,2]==1)or(arr[x,0]==-1 and arr[x,1]==-1 and arr[x,2]==-1):
            m = True
    for y in range(0,3):
        if(arr[0,y]==1 and arr[1,y]==1 and arr[2,y]==1)or(arr[0,y]==-1 and arr[1,y]==-1 and arr[2,y]==-1):
            m = True
    if (arr[0,0]==1 and arr[1,1]==1 and arr[2,2]==1) or (arr[0,0]==-1 and arr[1,1]==-1 and arr[2,2]==-1):
        m = True
    if (arr[0,2]==1 and arr[1,1]==1 and arr[2,0]==1) or (arr[0,2]==-1 and arr[1,1]==-1 and arr[2,0]==-1):
        m = True
    if arr[0,0]!=0 and arr[0,1]!=0 and arr[0,2]!=0 and arr[1,0]!=0 and arr[1,1]!=0 and arr[1,2]!=0 and arr[2,0]!=0 and arr[2,1]!=0 and arr[2,2]!=0:
        m = True
    
        
main()