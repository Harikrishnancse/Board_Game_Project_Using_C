from Board import *

n = int(input('Enter the size : '))
b = Board(n)
while(True):
    inp = int(input('1. Insert 2.Display 3.Exit \n  Enter the choice :'))
    if inp==1:
        b_no = int(input('Enter the block number : '))
        pos = input('enter the position').split()
        x , y =  int(pos[0]) , int(pos[1])
        b.insert(x,y, b_no)
    elif inp==2:
        b.print()
    elif inp==3:
        break

    

