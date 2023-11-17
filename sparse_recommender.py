class SparseMatrix:   

    def __init__(self):
        self.dic = {}
    def __init__(self,r,c):
        self.rows = r
        self.coloumns = c
        self.dic = {}

    def set(self,r,c,a):
        if r < 0 or r >= self.rows or c < 0 or c >= self.coloumns:
            print("Invalid/Mismatch Dimensions")
            raise ValueError("Invalid/Mismatch Dimensions")
        self.dic[(r, c)] = a
    def get(self,r,c):
        if r<0 or r>= self.rows or c<0 or c>= self.coloumns:
            print("Invalid/Mismatch Dimensions")
            raise ValueError("Invalid/Mismatch Dimensions")
        return self.dic.get((r,c),0)

    def recommend(self,vec):
        if len(vec)!=self.coloumns:
            print("Invalid/Mismatch Dimensions")
            raise ValueError("Invalid/Mismatch Dimensions")
        s = [0]*self.rows
        for (r,c),a in self.dic.items():
            s[r]+= vec[c]*a
        return s

    def add_movie(self,mat):
        if mat.rows!= self.rows or mat.coloumns!= self.coloumns:
            print("Invalid/Mismatch Dimensions")
            raise ValueError("Invalid/Mismatch Dimensions")
        resMat = SparseMatrix(self.rows, self.coloumns)
        for (r,c),a in self.dic.items():
            resMat.set(r,c,a)
        for (r,c),a in mat.dic.items():
            resMat.set(r,c,a)
        return resMat

    def toDense(self):
        dense = [[0]*self.coloumns for j in range(self.rows)]
        for (i,j),a in self.dic.items():
            dense[i][j] = a
        return dense
