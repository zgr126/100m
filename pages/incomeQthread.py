
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
import threading

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
            self.wide_img_sck =  CBackEndSocket(ip, port, True, True, False, False )
            self.cmd_sck_send =  CBackEndSocket( ip, port+2, False, False, False, True )
            self.cmd_sck_recv =  CBackEndSocket( ip, port+1, False, False, True, False )
            self.telefocus_img_sck =  CBackEndSocket(ip, port+3, True, False, False, False )
            
            while(True):
                rev_wide_img  = self.wide_img_sck.receiveWideImage()
                pos, rev_telefocus_img = self.telefocus_img_sck.receivePosAndTelefocusImg()
                cmd = self.cmd_sck_recv.receiveCMD( "mc_status" )
                if cmd is not None:
                    print(cmd)
                # if rev_telefocus_img is not None:
                #     self.getPicSignal.emit(rev_telefocus_img)
                if rev_wide_img is not None:
                    self.getPicSignal.emit(rev_wide_img)
                time.sleep(1/50)
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

# def write_video( img_buffer, video_part ):
#     #global mc_id, mc_fps, save_path
#     save_path = "./"
#     save_video_file = None;
#     mc_id_temp = "none";
#     mc_fps_temp = 0
#     write_over_flag = False;
#     import copy
#     while True:
#         mc_id_read = copy.deepcopy(mc_id)
#         mc_fps_read = copy.deepcopy(mc_fps)

#         if mc_id_read != mc_id_temp:
#             if mc_id_read != "none":
#                 if save_video_file is not None:
#                     save_video_file.release()
#                 write_over_flag = False
#                 save_video_file = cv2.VideoWriter(save_path+mc_id_read+"_s"+str(video_part)+".avi", cv2.VideoWriter_fourcc(*'XVID'), mc_fps_read, (1440, 1080))
#                 print("start recording file part[{}] id [{}] at fps [{}]".format(video_part, save_path+mc_id_read, mc_fps_read))
#             else:
#                 if save_video_file is not None:
#                     write_over_flag = True
#                 print("wating for recording file part[{}] id [{}] at fps [{}]".format(video_part, save_path+mc_id_temp, mc_fps_temp))
#             mc_id_temp = mc_id_read; mc_fps_temp = mc_fps_read;

#         if save_video_file is not None:
#             img_temp = None;
#             if len(img_buffer) > 0:
#                 img_temp = copy.deepcopy(img_buffer[0])
#                 img_buffer.pop(0)
#                 if len(img_buffer) > 3:
#                     print("write_video buffer over flow:", len(img_buffer))
#             elif write_over_flag:
#                 save_video_file.release()
#                 save_video_file = None
#                 write_over_flag = False
#                 print("finished recording")
                
#             if img_temp is not None and save_video_file is not None:
#                 save_video_file.write( img_temp )
#             else:
#                 time.sleep( 0.001 )
#         else:
#             time.sleep( 0.001 )

# #create writing video thread
# write_video_thread_lst = []
# write_video_img_buffer_lst =[]
# for galvo_index in range( 1 ):
#     write_video_img_buffer_lst.append([])
#     write_video_thread_lst.append( threading.Thread(target=write_video, args=(write_video_img_buffer_lst[-1], galvo_index)) );
#     write_video_thread_lst[-1].start()
#     write_video_thread_lst[-1].setName('writeVideo_'+str(galvo_index))
#     print("started new thread [{}]".format(write_video_thread_lst[-1].getName()))