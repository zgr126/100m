
# -*-coding:utf8 -*-
__author__ = "jermeyjone"
__abc__ = "第一个PySide程序，创建一个窗口"

import numpy as np

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
import time
# import utils.backend_server_sim as backend 
from utils.connectServer import CBackEndSocket
import pages.userTable as ut
import utils.gol as gol
import cv2

# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class Worker(QObject):
    connectSignal = Signal(int)
    getPicSignal = Signal(object)
    progress = Signal(int)
    completed = Signal(int)
    
    # 需要执行的耗时任务
    def do_work(self, n):
        for i in range(1, n+1):
            time.sleep(1)
            self.progress.emit(i)

        self.completed.emit(i)
    def connectServer(self):
        try:
            ip = gol.get('config')['ip']
            port  = gol.get('config')['port']
            # self.wide_img_sck =  CBackEndSocket(ip, port, True, True, False, False )
            # self.cmd_sck_send =  CBackEndSocket( ip, port+2, False, False, False, True )
            # self.cmd_sck_recv =  CBackEndSocket( ip, port+1, False, False, True, False )
            self.telefocus_img_sck =  CBackEndSocket(ip, port+3, True, False, False, False )
            
            while(True):
                pos, rev_telefocus_img = self.telefocus_img_sck.receivePosAndTelefocusImg()
                if rev_telefocus_img is not None:
                    # rev_telefocus_img = add_projection_points( rev_telefocus_img, pos )
                    # cv2.imshow("dd", rev_telefocus_img)
                    # print('getImg',str(time.time()))
                    # a = rev_telefocus_img
                    # b = (255 << 24 | a[:,:,0] << 16 | a[:,:,1] << 8 | a[:,:,2]).flatten()
                    # print(type(b))
                    # print(rev_telefocus_img)
                    self.getPicSignal.emit(rev_telefocus_img)
                time.sleep(1/30)
        except:
            print('获取ip/port异常')

def add_projection_points( img, projection_points_dict ):
    h,w,c = img.shape
    galvo_num = w//1440
    for galvo_index in range(galvo_num):
        x_offset = galvo_index*1440
        for coord in projection_points_dict["pose_reprojection_"+str(galvo_index)]:
            cv2.circle(img, (int(coord["x"]*1440+x_offset),int(coord["y"]*1080)), 20, (0,255,0), 2)

    return img