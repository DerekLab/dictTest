from ctypes import *


class InitMdInfoField(Structure):
    _fields_ = [('FlowPaht', c_char_p)
                ]


class RegisterInfoField(Structure):
    _fields_ = [('BrokerID', c_char_p),
                ('UserID', c_char_p),
                ('LoginMode', c_int),
                ('pszFrontAddress', c_char_p),
                ('pszNsAddress', c_char_p)
                ]


class addnum(Structure):
    _fields_ = [('a', c_int),
                ('b', c_int)
                ]


class addnum2(Structure):
    _fields_ = [('c', c_int)
                ]
