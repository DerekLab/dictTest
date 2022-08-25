from ctpmdType import *
from ctypes import *
import os
import time
import threading


def main():
    pathnow = os.path.abspath('gfctpmd.dll')

    pathnow = pathnow.replace('\\', '/')
    print(pathnow)

    lib_add = cdll.LoadLibrary(pathnow)

    InitmdF = InitMdInfoField()
    InitmdF.FlowPaht = bytes("D:\\PycharmProjects\\pythonProject\\MdTemp", "utf-8")

    py_struct_1 = addnum()
    py_struct_1.a = 55
    py_struct_1.b = 10
    py_struct_1_pointer = py_struct_1

    py_struct_2 = addnum2()
    py_struct_2.c = 15
    py_struct_2_pointer = py_struct_2

    print(lib_add.add2(py_struct_1_pointer, py_struct_2_pointer))

    '''
    openTCP = lib_add.CreateMdApi
    # openTCP.argtype = [ctypes.c_char_p, ctypes.c_char_p]
    openTCP.argtype = [ctypes.c_char_p]

    openREG = lib_add.RegisterSpi

    # openVer = lib_add.GetApiVersion
    # openVer.restype = ctypes.c_char_p

    openFront = lib_add.RegisterFront
    openFront.argtype = [ctypes.c_char_p]

    openInit = lib_add.Init

    TCPbyte = (ctypes.c_char * 100)(*bytes("D:\\PycharmProjects\\pythonProject\\MdTemp", "utf-8"))
    ctypes.cast(TCPbyte, ctypes.POINTER(ctypes.c_char))
    # TCPchar = (ctypes.c_char * 100)(*bytes("tcp://192.168.193.154:10211|tcp://58.33.41.185:42213|tcp://58.33.41.185:42213", "utf-8"))
    # TCPchar = (ctypes.c_char * 100)(*bytes("tcp://121.36.146.182:20002", "utf-8"))
    TCPchar = (ctypes.c_char * 100)(*bytes("tcp://180.168.146.187:10211", "utf-8"))
    # ctypes.cast(TCPchar, ctypes.POINTER(ctypes.c_char))

    openTCP(TCPbyte)
    openREG()
    # openVer()
    openFront(TCPchar)
    openInit()
    # lib_add.InitMD(stu_obj)

    time.sleep(10)


    thread1 = threading.Thread(name='t1', target=test, args=(1, 10))
    thread2 = threading.Thread(name='t2', target=test, args=(11, 20))
    thread1.start()  # 启动线程1
    thread2.start()  # 启动线程2

    '''


if __name__ == '__main__':
    main()
