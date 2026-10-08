import numpy as np  
from scipy.integrate import ode
from w_s.Trun_Funct import TF


def f(t,x:np.ndarray,A, B:np.ndarray, u):
   return (A @ x) + (B * u) 

def simulatefilter(tf: TF, inpsig):
   A, B, C, D = tf.to_ss()
   n = A.shape[0]
   x = np.zeros(n)
   r = ode(f)
   r.set_integrator('dopri5') # Метод
   t = [o[0] for o in inpsig]
   u_u = [o[1] for o in inpsig]
   y = np.zeros(len(t))
   for i in range(len(t)-1):
      y[i] = (C @ x).item()+ D[0,0] * u_u[i]
      r.set_initial_value(x, t[i]) # Значения u разное, поэтому мы берем каждый новый промежуток
      r.set_f_params(A, B[:,0], u_u[i])
      x = r.integrate(t[i+1]) #временной промежуток интегрирования
   y[-1] = (C @ x).item() + D[0, 0] * u_u[-1]
   return y