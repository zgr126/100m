
import numpy as np

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
import utils.QFlowLayout as uQ
import time

import pages.userDetails as ud
import utils.db as db
import calc.main2 as cm
import pyqtgraph as pg

# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class Page(QWidget):
    data = []
    def __init__(self, data,arg=None):
        super(Page, self).__init__(arg)
        self.data = data
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        l = QLabel('百米基础属性')
        self.layout.addWidget(l)
        List9 = cm.List9(self.data)
        self.List9 = List9
        self.table = QTableWidget(2, 8)  # 3 行 5 列的表格
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        self.table.setMaximumHeight(120)
        self.table.setHorizontalHeaderLabels(['项目', '速度', '躯干俯仰角', '平均绝对步长', '平均相对步长', '步频', '重心水平位移', '重心垂直位移'])
        self.layout.addWidget(self.table)
        self.table.setItem(0,0,QTableWidgetItem('当前项目'))

        l2 = QLabel('每10米分段时间')
        self.layout.addWidget(l2)

        self.table2 = QTableWidget(2, 11)  # 3 行 5 列的表格
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        self.table2.setMaximumHeight(120)
        self.table2.setHorizontalHeaderLabels(['项目', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'])
        self.table2.setItem(0,0,QTableWidgetItem('当前项目'))
        
        self.layout.addWidget(self.table2)

        # List9 = cm.List9(self.data)
        # option1 = {'data':[List9['PerSpeed']],
        #     'title':'水平面投影角加速度',
        #     'yAxis':['加速度','rad/s²']}
        # # self.layout.addStretch()
        self.contrastData = None
        self.formWid = None
        self.setTable()
        
    def setTable(self):
        # print(List9)
        List9 = self.List9
        # table1
        self.table.setItem(0,1,QTableWidgetItem(str(round(List9['AvgSpeed'],2))))
        self.table.setItem(0,2,QTableWidgetItem(str(round(List9['AvgAngleNormal'],2))))
        self.table.setItem(0,3,QTableWidgetItem(str(round(List9['StepSize'],2))))
        self.table.setItem(0,4,QTableWidgetItem(str(round(List9['StepSize_height'],2))))
        self.table.setItem(0,5,QTableWidgetItem(str(round(List9['StepNum'],2))))
        self.table.setItem(0,6,QTableWidgetItem(str(round(List9['AvgVertCenter'],2))))
        self.table.setItem(0,7,QTableWidgetItem(str(round(List9['AvgLevelCenter'],2))))

        
        if self.contrastData is not None:
            cList = self.contrastData
            # table1
            self.table.setItem(1,0,QTableWidgetItem('对比项目'))
            self.table.setItem(1,1,QTableWidgetItem(str(round(cList['AvgSpeed'],2))))
            self.table.setItem(1,2,QTableWidgetItem(str(round(cList['AvgAngleNormal'],2))))
            self.table.setItem(1,3,QTableWidgetItem(str(round(cList['StepSize'],2))))
            self.table.setItem(1,4,QTableWidgetItem(str(round(cList['StepSize_height'],2))))
            self.table.setItem(1,5,QTableWidgetItem(str(round(cList['StepNum'],2))))
            self.table.setItem(1,6,QTableWidgetItem(str(round(cList['AvgVertCenter'],2))))
            self.table.setItem(1,7,QTableWidgetItem(str(round(cList['AvgLevelCenter'],2))))
            # table2
            self.table2.setItem(1,0,QTableWidgetItem('对比项目'))
            for index, pitem in enumerate(cList['PerTime'][:10]):
                self.table2.setItem(1,index+1,QTableWidgetItem(str(round(pitem,2))))
        # table2
        for index, pitem in enumerate(List9['PerTime'][:10]):
            self.table2.setItem(0,index+1,QTableWidgetItem(str(round(pitem,2))))
        # picList
        a = self.layout.findChild(QScrollArea, 'formArea')
        if a != None:
            a.setParent(None)
            self.layout.removeWidget(a)

        # 制造对比数据
        d1 = None
        d2 = None
        if self.contrastData is not None:
            cList = self.contrastData
            d1 = cList['PerSpeed'][1:11]
            d2 = [cList['LandLF'],cList['LandRT'],cList['RiseLF'],cList['RiseRT'],
            cList['LFTime'],cList['RTTime'],cList['BufferLF'],cList['BufferRT'],cList['KickLF'],cList['KickRT']]
        option1 = [{'data':List9['PerSpeed'][:10],'data2': d1,
            'xData': ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
            'title':'运动员在每10米分段平均速度',
            'type': 'line',
            'yAxis':['速度','m/s']},
            {'data':[List9['LandLF'],List9['LandRT'],List9['RiseLF'],List9['RiseRT'],
            List9['LFTime'],List9['RTTime'],List9['BufferLF'],List9['BufferRT'],List9['KickLF'],List9['KickRT']],'data2':d2,
            'xData': ['左着地', '右着地', '左腾空', '右腾空', '左单步', '右单步', '左缓冲', '右缓冲', '左伸蹬', '右伸蹬'],
            'title':'运动员左右脚数据',
            'type': 'bar',
            'yAxis':['时间','s']},]
        
        if self.formWid is not None:
            self.formWid.close()
        self.formWid = formScrollArea(option1)
        self.layout.addWidget(self.formWid)
    def setContrast(self,data):
        self.contrastData = data
        self.setTable()
        # self.layout.wid
def formScrollArea(options):
    listW = setPage(options)
    # 展示区域
    qscrollarea = QtWidgets.QScrollArea()
    qscrollarea.setContentsMargins(0,0,0,0)
    qscrollarea.setGeometry(QRect(50,100,600,500))
    qscrollarea.setWidgetResizable(True)
    qscrollarea.setWidget(listW)
    # layout.addWidget(qscrollarea)
    qscrollarea.setObjectName('formArea')
    return qscrollarea
def setPage(options):
    layout = uQ.FlowLayout()
    wid = QGroupBox()
    wid.setLayout(layout)
    # w= Window({'data':x1,
    #     'title': 'ind点xz面位移图(俯视)',
    #     'yAxix': ['z axis','帧率']
    #     })
    for i in options:
        w = Window(i)
        layout.addWidget(w)
    
    container_layout = QVBoxLayout()
    container_layout.setContentsMargins(0,0,0,0)
    listW = QListWidget()
    listW.setContentsMargins(0,0,0,0)
    listW.setLayout(container_layout)
    wid.setContentsMargins(0,0,0,0)
    container_layout.addWidget(wid)
    # container_layout.addStretch()
    # l = QWidget()
    return listW
class Window(QWidget):
    def __init__(self, options):
        super().__init__()
        # 设置下尺寸
        self.resize(600,300)
        # 添加 PlotWidget 控件
        self.plotWidget_ted = pg.PlotWidget(self)
        # 设置该控件尺寸和相对位置
        self.plotWidget_ted.setGeometry(QtCore.QRect(0,0,600,300))
        self.setFixedWidth(600)
        self.setFixedHeight(300)
        self.setStyleSheet('''
            QWidget {
                margin: 0ex;
            }
            QWidget:enabled {
                border: 1px solid black;
            }
            QWidget::title {
                subcontrol-origin: margin;
                left: 1ex;
            }''')
        # 仿写 mode1 代码中的数据
        # 生成 300 个正态分布的随机数
        title = options['title']
        # self.plotWidget_ted.setYRange(-1,1)
        self.plotWidget_ted.setLabel("left",options['yAxis'][0],units=options['yAxis'][1])
        self.plotWidget_ted.setTitle(title)
        self.plotWidget_ted.setBackground((255, 255, 255))
        # self.plotWidget_ted.setConfigOption('WheelSpin', False)
        # self.plotWidget_ted.
        hasX = options['xData'] is not None
        if hasX:
            xdict = dict(enumerate(options['xData']))
            x = list(xdict.values())
            ticks = [(i, j) for i, j in zip(range(10), options['xData'])]
            if options['type'] == 'bar':
                barItem = pg.BarGraphItem(x=range(len(options['xData'])),height=options['data'],width=0.2,brush=(50,50,50))
                self.plotWidget_ted.addItem(barItem)
                data = np.arange(len(options['xData']))#range(len(options['xData']))
                if options['data2'] is not None:
                    barItem2 = pg.BarGraphItem(x=data+0.3, height=options['data2'],width=0.2,brush=(50,50,224))
                    self.plotWidget_ted.addItem(barItem2)
                self.plotWidget_ted.enableAutoRange()
            else:
                pen = pg.mkPen(color=(50, 50, 50))
                self.curve1 = self.plotWidget_ted.plot(options['data'], name="mode1", pen=pen)
                if options['data2'] is not None:
                    # i = pg.PlotItem(brush=(50,50,224))
                    pen = pg.mkPen(color=(50, 50, 224))
                    self.plotWidget_ted.plot(options['data2'], name="mode1", pen=pen)
            
            

            xax = self.plotWidget_ted.getAxis('bottom')
            xax.setTicks([ticks])
            # self.plotWidget_ted.bar
            # 显示图表
        # plot = FigureCanvasDemo3(
        #     width=self.ui.graphicsView.width() / 101,
        #     height=self.ui.graphicsView.height() / 101
        # )
        
        # graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
        # graphicsScene.addWidget(plot)
        # self.ui.graphicsView.setScene(graphicsScene)
        # self.ui.graphicsView.show()  # 调用show方法呈现图形
        else:
            self.curve1 = self.plotWidget_ted.plot(options['data'], name="mode1")
            
        
        
# class PyQtGraphHistWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
 
#         self.init_data()
#         self.init_ui()
#     def init_data(self):
#         self.color_bar = (107,200,224)
#         pass
#     def init_ui(self):
#         self.title_label = QtWidgets.QLabel('直方图')
#         self.title_label.setAlignment(Qt.AlignCenter)
#         xax = RotateAxisItem(orientation='bottom')
#         xax.setHeight(h=80)
#         self.pw = pg.PlotWidget(axisItems={'bottom': xax})
#         self.pw.setMouseEnabled(x=True, y=False)
#         # self.pw.enableAutoRange(x=False,y=True)
#         self.pw.setAutoVisible(x=False, y=True)
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.title_label)
#         layout.addWidget(self.pw)
#         self.setLayout(layout)
#         pass
#     def set_data(self,data:Dict[str,Any]):
#         title_str = data['title_str']
#         x = data['x']
#         y = data['y']
#         y_name = data['y_name']
#         xTick = [data['xTick']]
 
#         self.y_datas = y
#         self.x_data = xTick
#         self.x_Tick = data['xTick']
#         self.y_name = y_name
 
#         self.title_label.setText(title_str)
#         self.pw.setLabel('left', y_name)
#         xax = self.pw.getAxis('bottom')
#         xax.setTicks(xTick)
 
#         barItem = pg.BarGraphItem(x=x,height=y,width=0.8,brush=self.color_bar)
#         self.pw.addItem(barItem)
 
#         self.vLine = pg.InfiniteLine(angle=90, movable=False)
#         self.hLine = pg.InfiniteLine(angle=0, movable=False)
#         self.label = pg.TextItem()
 
#         self.pw.addItem(self.vLine, ignoreBounds=True)
#         self.pw.addItem(self.hLine, ignoreBounds=True)
#         self.pw.addItem(self.label, ignoreBounds=True)
#         self.vb = self.pw.getViewBox()
#         self.proxy = pg.SignalProxy(self.pw.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
#         self.pw.enableAutoRange()
#         pass
#     def mouseMoved(self,evt):
#         pos = evt[0]
#         if self.pw.sceneBoundingRect().contains(pos):
#             mousePoint = self.vb.mapSceneToView(pos)
#             index = int(mousePoint.x())
#             if index >= 0 and index < len(self.y_datas):
#                 x_str = str(self.x_Tick[index][1])
 
#                 y_str_html = ''
#                 y_str = str(self.y_datas[index])
#                 y_str_html += '&nbsp;' + y_str
#                 html_str = '<p style="color:black;font-size:18px;font-weight:bold;">&nbsp;' + x_str +'<br/>&nbsp;'+y_str_html+ '</p>'
#                 self.label.setHtml(html_str)
#                 self.label.setPos(mousePoint.x(), mousePoint.y())
#             self.vLine.setPos(mousePoint.x())
#             self.hLine.setPos(mousePoint.y())
#         pass
#     pass