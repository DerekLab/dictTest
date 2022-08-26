from ctpmdType import *
from ctypes import *
import os
import time

def main():
    pathnow = os.path.abspath('gfctpmd.dll')
    pathnow = pathnow.replace('\\', '/')

    lib_add = cdll.LoadLibrary(pathnow)

    Initmd_ = InitMdInfoField()
    Initmd_.FlowPaht = b'E:\\Workstation Files\\PycharmProjects\\MypythonProject\\TempMD\\'

    Register_ = RegisterInfoField()
    Register_.BrokerID = b'9999'
    Register_.UserID = b'03245'
    Register_.LoginMode = 3
    Register_.pszFrontAddress = b'tcp://180.168.146.187:10211|tcp://58.33.41.185:42213|tcp://58.33.41.185:42213'
    Register_.pszNsAddress = b'tcp://127.0.0.1:1234'

    openTCP = lib_add.InitMdApi
    openTCP.restype = c_int
    openTCP(Initmd_, Register_)
    time.sleep(10)

    # print(Initmd_.FlowPaht)

    '''
    py_struct_1 = addnum()
    py_struct_1.a = 55
    py_struct_1.b = 10
    py_struct_1_pointer = py_struct_1

    py_struct_2 = addnum2()
    py_struct_2.c = 15
    py_struct_2_pointer = py_struct_2

    print(lib_add.add2(py_struct_1_pointer, py_struct_2_pointer))
    '''


if __name__ == '__main__':
    main()
