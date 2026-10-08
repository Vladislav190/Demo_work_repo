#num — числитель
#den — знаменатель
import sys
from w_s.text_opn import txt_open, js_open
from w_s.Trun_Funct import TF
from w_s.InLpfTf import *
from w_s.data_form import Data_priob
from w_s.crl_filt import createfilter
from w_s.integration_ss import simulatefilter

files_json = sys.argv[1]
param = js_open(files_json)

files_txt = sys.argv[2] # нужен массив? или норм разложение
u_t = txt_open(files_txt)

qqq = createfilter(Data_priob(param))

yi = [o for o in (simulatefilter(qqq, u_t))]
for i in range(len(yi)):
    print(f'{u_t[i][0]} {yi[i]}')