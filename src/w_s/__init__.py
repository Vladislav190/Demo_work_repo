R'''
    Trun_Funct: хранит в себе общий полином последовательной цепочки

    InLpfTf: хранит и проверяет в себе полиномы: интегратор, фильтр, передаточная функция

    simulatefilter: Интегрирование Step Space, 
    x' = A @ x + B * ui
    y = C @ xi + D * ui
    
    Data_priob: Формирование полинома из json. Возращает массив классов полиномов

    createfilter: возращает класс общего полинома

    Данный пакет работает с файлами расишрения .json и txt 

'''
from .Trun_Funct import  TF
from .InLpfTf import *
from .crl_filt import createfilter
from .data_form import Data_priob
from .integration_ss import simulatefilter

__all__ = ["TrTrun_Funct", "InLpfTf", "crl_filt", "data_form", "integration_ss"]