from fractions import Fraction
import random as r

class Matrix:
    def __init__(self, m:int, n:int = 0, identity = False):
        is_unidimarray = False
        self.m = 0
        self.n = 0
        if isinstance(m, list):
            self.m = len(m)
            try:
                self.n = len(m[0])
            except:
                self.n = len(m)
                self.m = 1
                is_unidimarray = True
            if is_unidimarray == 1:
                self.M = list()
                self.M.append([Fraction(e) for e in m])
            else:
                self.M = [[Fraction(e) for e in row] for row in m]
        elif isinstance(m, int) and isinstance(n, int):
            if m > 0 and n > 0:
                self.m = m
                self.n = n
                self.M = [[Fraction(0) for _ in range(m)] for _ in range(n)]
                if identity == True:
                    for i in range(min(self.m, self.n)):
                        self.M[i][i] = 1                    
            else:
                self.M = [[Fraction(0) for _ in range(m)] for _ in range(n)]
                self.m = 1
                self.n = 1
        else:
            self.M = [[Fraction(0) for _ in range(m)] for _ in range(n)]
            self.m = 1
            self.n = 1

    def __add__(self, B):
        if self.m == B.m and self.n == B.n:
            return Matrix([[self.M[i][j] + B.M[i][j] for j in range(self.n)] for i in range(self.m)])
        else:
            return Matrix(1, 1)
    def __mul__(self, B):
        if isinstance(B, Matrix):
            if self.n == B.m:
                return Matrix([[sum([self.M[i][k] * B.M[k][j] for k in range(self.n)]) for j in range(B.n)] for i in range(self.m)])
            else:
                return Matrix(1, 1)
        else:
            try:
                return Matrix([[e * B for e in row] for row in self.M])
            except:
                return Matrix(1, 1)
    def __eq__(self, __value) -> bool:
        if self.m==__value.m and self.n==__value.n:
            for i in range(self.m):
                for j in range(self.n):
                    if self.M[i][j]!=__value.M[i][j]:
                        return False
        else :
            return False
        return True
    
    def setRandSimetry(self, value = 1):
        for i in range(self.m):
            for j in range(i, self.n):
                if i == j:
                    self.M[i][j] = r.randint(0, value)
                else:
                    self.M[i][j] = self.M[j][i] = r.randint(0, value)
    def setDiagonal(self):
        for i in range(self.m):
            for j in range(self.n):
                if i == j:
                    self.M[i][j] = 1
                else:
                    self.M[i][j] = 0
    def swap_row(self, R1:int, R2:int):
        self.M[R1], self.M[R2] = self.M[R2], self.M[R1]
    def add_row(self, R1:int, R2:int, coef = 1):
        if R1 > -1 and R1 < self.m and R2 > -1 and R2 < self.m:
            for j in range(self.n):
                self.M[R1][j] += self.M[R2][j] * coef
    def copy(self):
        return Matrix([row.copy() for row in self.M])
    def reducir(self):
        U = self.copy()
        Pt = Matrix(U.m, U.n, identity = True)
        L = Matrix(U.m, U.n, identity=True)
        EPt = Matrix(U.m, U.n, identity=True)
        es_resolvible = True
        for i in range(U.m - 1):
            if U.M[i][i] == 0:
                es_resolvible = False
                for j in range(i + 1, self.m):
                    if U.M[j][i] != 0:
                        EPt.setDiagonal()
                        es_resolvible = True
                        EPt.swap_row(i,j)
                        Pt = Pt * EPt
                        U.swap_row(i, j)
                        break
            if es_resolvible == False:
                print("SIN SOLUCION")
                return Pt, L, U
            for j in range(i + 1, U.m):
                if U.M[j][i] != 0:
                    coef = Fraction(U.M[j][i] / U.M[i][i]).limit_denominator()
                    U.add_row(j, i, Fraction(-1 * coef))
                    tmp = Matrix(U.m, U.n, identity=True)
                    tmp.add_row(j, i, Fraction(coef))
                    L = L * tmp
        print("---------------\n ORIGINAL\n---------------")
        self.print()
        print("---------------\n Pt\n---------------")
        Pt.print()
        print("---------------\n L\n---------------")
        L.print()
        print("---------------\n U\n---------------")
        U.print()
        print("---------------\n RESULTADO PRODUCTO (Pt * L * U)\n---------------")
        (Pt*L*U).print()
        return Pt, L, U
    def print(self):
        for row in self.M:
            for e in row:
                print(e, end = "  ")
            print()