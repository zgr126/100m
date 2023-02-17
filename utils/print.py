# Time: ${DATE} ${TIME}         
# Author: 自己名字                   
# File: ${NAME}.py             
# Software: ${PRODUCT_NAME}   

from builtins import print as _print
from sys import _getframe

# 自定义print函数
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'        # 注此处需加参数 1。
    return _print(f"《{__name__}》-{s}", *arg, **kw)

print("此处显示行数。")                   
