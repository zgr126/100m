import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PySide6.QtCore import QThread, QObject, Signal
import time

# 工作类，并继承QObject
class Worker(QObject):
    progress = Signal(int)
    completed = Signal(int)
	
    # 需要执行的耗时任务
    def do_work(self, n):
        for i in range(1, n+1):
            time.sleep(1)
            self.progress.emit(i)

        self.completed.emit(i)


class MainWindow(QMainWindow):
    a = Signal(int) #全局信号

    def __init__(self):
        super(MainWindow, self).__init__()

        # ui部分
        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('QThread Demo')
        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)       
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.btn_start = QPushButton('Start', clicked=self.start)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.btn_start)
		
        # 创建一个线程和一个工作实例
        self.worker = Worker()
        self.worker_thread = QThread()
        ###########注意#########################################################################################
        # 官方还有一个deleteLater()方法，该方法来自工作实例（即self.worker），因为继承了QObject
        # 有什么作用？大白话就是把刚放进线程里的工作实例释放掉（拿出来、删掉），这样，线程里就什么都没有了
        # 例子：self.worker_thread.finished.connect(self.worker.deleteLater)
        # 线程里没有工作实例了，自然就无法再次调用了，看如下报错
        # Traceback (most recent call last):
        #    File "D:\Py Workspace\baseqt\test.py", line 49, in <lambda>
        #        self.worker_thread.finished.connect(lambda: print(self.worker))
        # RuntimeError: Internal C++ object (Worker) already deleted.
        # 报错已经说的很明白了，object (Worker) already deleted
        # 什么时候用？多数是不用的，看情况而定吧！
        # 那他是为了什么？一种优化，释放掉不用的对象，释放内存呗，注意了，你的对象还要用就不要去释放了
        #######################################################################################################
        # self.worker_thread.finished.connect(self.worker.deleteLater)
        # self.worker_thread.finished.connect(lambda: print(self.worker)) # 测试释放掉对象后的报错

        # 线程里的progress信号与进度条更新函数绑定
        self.worker.progress.connect(self.update_progress)
        # 线程里的completes信号与完成函数绑定
        self.worker.completed.connect(self.complete)
		
        # 全局信号绑定工作实例的方法
        self.a.connect(self.worker.do_work)

        # 把工作实例放进线程里
        self.worker.moveToThread(self.worker_thread)

        # 开始线程
        self.worker_thread.start()

    def start(self):
        self.btn_start.setEnabled(False)
        n = 5
        self.progress_bar.setMaximum(n)
        self.a.emit(n) # 给全局信号发信号，触发线程内工作实例的方法执行

    def update_progress(self, v):
        self.progress_bar.setValue(v) # 与线程内的progress信号绑定，更新进度条

    def complete(self, v): # 与线程内completed信号绑定，线程工作一结束就会触发此函数
        self.progress_bar.setValue(v)
        self.btn_start.setEnabled(True)

        # 线程内的耗时任务执行完了，但创建的这个线程不一定也会结束，所以还需下面几句来主动退出
        print(self.worker_thread.isRunning()) # 打印True表示线程还在
        self.worker_thread.quit() # 结束线程
        self.worker_thread.wait() # 等待线程结束
        print(self.worker_thread.isRunning()) # 打印False表示线程已退出
        # 注意：没有quit()和wait()，在x掉窗口时控制台会报“QThread: Destroyed while thread is still running”


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())