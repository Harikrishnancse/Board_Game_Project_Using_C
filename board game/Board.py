class Board:
    def __init__(self,n):
        self.size = n
        self.board = [['-' for i in range(n)] for i in range(n)]

    def print(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()
        print()

    def insert(self , i , j , block):
        if self.board[i-1][j-1] == '-' :
            self._insert(i,j,block)
        else:
            print('Another block already presnt in position\n ')

    def _insert(self , i , j , block):
        flag,x_pos,y_pos = self.adjacency(i-1,j-1,block)
        if flag:
            self.board[i-1][j-1] = block
            print('Block inserted....')
        else:
            #print('block ',block,' already present in adjacent position ',x_pos,' ',y_pos)
            self.board[x_pos][y_pos] = '-'
            self._insert(i,j,block+1)
            

    def adjacency(self ,x,y,block):
        i_s , i_e = x-1 , x+1
        j_s , j_e = y-1 , y+1
        if (i_s<0):
            i_s=0
        if (j_s<0):
            j_s=0
        if (i_e>self.size-1):
            i_e=self.size-1
        if (j_e>self.size-1):
            j_e=self.size-1
        #print(i_s,' ',i_e,'',j_s,' ',j_e,'\n')
        for i in range(i_s,i_e+1):
            for j in range(j_s,j_e+1):
                if self.board[i][j] == block:
                    return False,i,j
        return True,'null','null'
        
        
