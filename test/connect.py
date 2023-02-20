import cv2
from utils.connectServer import CBackEndSocket
import sys

class test():
    def __init__(self):
        super(test, self).__init__()
        ip = '192.168.123.146'
        port = 6000
        # self.wide_img_sck =  CBackEndSocket(ip, port, True, True, False, False )
        self.cmd_sck_send =  CBackEndSocket( ip, port+2, False, False, False, True )
        self.cmd_sck_recv =  CBackEndSocket( ip, port+1, False, False, True, False )
        self.telefocus_img_sck =  CBackEndSocket(ip, port+3, True, False, False, False )
        pos, rev_telefocus_img = self.telefocus_img_sck.receivePosAndTelefocusImg()
        if rev_telefocus_img is not None:
            cv2.imshow("cam_Wide_Send", rev_telefocus_img)
            print('getImg',str(time.time()))

if __name__ == '__main__':
    test()
    sys.exit()