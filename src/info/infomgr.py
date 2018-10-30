#! /usr/bin/env python
import wx
import sys
import os
import array
sys.path.append(os.path.abspath(".."))
from ui import uicore

class secBootInfo(uicore.secBootUi):

    def __init__(self, parent):
        uicore.secBootUi.__init__(self, parent)

    def printLog( self ,logoStr ):
        self.m_textCtrl_log.write(logoStr + "\n")

    def clearLog( self ):
        self.m_textCtrl_log.Clear()

    def printDeviceStatus( self ,statusStr ):
        self.m_textCtrl_deviceStatus.write(statusStr + "\n")

    def clearDeviceStatus( self ):
        self.m_textCtrl_deviceStatus.Clear()

    def getReg32FromBinFile( self, filename, offset=0):
        reg32Vaule = 0
        if os.path.isfile(filename):
            reg32Array = array.array('c', [chr(0xff)]) * 4
            with open(filename, 'rb') as fileObj:
                fileObj.seek(offset)
                reg32Array = fileObj.read(4)
                fileObj.close()
            reg32Vaule = (ord(reg32Array[3])<<24) + (ord(reg32Array[2])<<16) + (ord(reg32Array[1])<<8) + ord(reg32Array[0])
        return hex(reg32Vaule)

    def getVal32FromByteArray( self, binarray, offset=0):
        val32Vaule = ((binarray[3+offset]<<24) + (binarray[2+offset]<<16) + (binarray[1+offset]<<8) + binarray[0+offset])
        return val32Vaule