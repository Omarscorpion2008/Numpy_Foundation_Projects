import numpy as np
class Calc:
    def __init__(self):
        rng = np.random.default_rng()
        self.array1 = rng.integers(low=1, high=50, size=(2, 2))
        self.array2 = rng.integers(low=1, high=50, size=(2, 2))
        
        #self.addition_subtraction()
        #self.multiplication_division()
        #self.transpose()
        #self.inverse_and_determinant()
        
    def addition_subtraction(self):
        if self.array1.shape == self.array2.shape:
            addition = self.array1 + self.array2
            subtraction = self.array1 - self.array2
            print(f"Addition:\n {addition}")
            print(f"Subtraction:\n {subtraction}")
        else:
            print("invalid matrices shapes")
    
    def multiplication_division(self):
        if self.array1.shape[1] == self.array2.shape[0]:
            multiplication = self.array1 @ self.array2
            print(f"Multiplication:\n {multiplication}")
        else:
            print("Invalid matrices shapes")
    
    def transpose(self):
        array1_trans = np.transpose(self.array1)
        array2_trans = np.transpose(self.array2)
        
        print(array1_trans)
        print(array2_trans)
    
    def inverse_and_determinant(self):
        if self.array1.shape[0] != self.array1.shape[1]:
            print("Matrix must be square")
            return
        else:
            determinant = np.linalg.det(self.array1)
            if np.isclose(determinant, 0):
                print("Inverse computing can't be proceeded")
            else:
                inverse = np.linalg.inv(self.array1)
                print(f"Inverse:\n {inverse}")
Calc()