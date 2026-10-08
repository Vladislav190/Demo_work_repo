from w_s.InLpfTf import *

def Data_priob(chain):
   key = []
   datac = []
   for i in chain:
      key = list(i.keys())
      match key[0]:
         case "lpf"        : datac.append(lpfunction(i["lpf"]["deg"], i["lpf"]["T"]))
         case "tf"         : datac.append(TranceFunction(i["tf"]["num"], i["tf"]["denom"]))
         case "integrator" : datac.append(Integration(**i["integrator"]))
   return datac