import numpy as np

class TF:
   def __init__(self, b, a):
      self.b = b
      self.a = a
   def __mul__(self, other):
      a_now = self.a
      a_bck = other.a
      b_now = self.b
      b_bck = other.b
      return TF((np.convolve(b_now,b_bck)),(np.convolve(a_now,a_bck)))
      
   def to_ss(self):
      a = np.trim_zeros(np.array(self.a, float), 'f')   
      b = np.array(self.b, float)
      n = len(a) - 1                                     
      b = b / a[0]
      a = a / a[0]                                       
      b = np.concatenate([np.zeros(n + 1 - len(b)), b])  
      D = np.array([[b[0]]])
      r = b[1:] - b[0] * a[1:]                          
      A = np.zeros((n, n))
      if n > 1:
         A[:-1, 1:] = np.eye(n - 1)
      if n > 0:
         A[-1, :] = -a[1:][::-1]                         
      B = np.zeros((n, 1))
      if n > 0:
         B[-1, 0] = 1
      C = r[::-1].reshape(1, n)                          
      return A, B, C, D

def matric(mat:TF):
   A, B, C, D, = mat.to_ss()
   return A, B, C, D,