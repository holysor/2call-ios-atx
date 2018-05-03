#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'

from functools import wraps
import os,sys
import time
import traceback

def ErrorHandle(func):
    """
        用例失败截图
    """
    funcname = func.__name__ + '.png'
    day = time.strftime('%Y-%m-%d')
    path = os.getcwd() +'/result/' + day + '/screencap/'
    imagepath = path + funcname

    if os.path.exists(path):
        if os.path.exists(imagepath):
            os.remove(imagepath)
    else:
        os.makedirs(path)

    @wraps(func)
    def _deco(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            if args:
                args[0].__init__.im_self.driver.screenshot().save(imagepath)
            traceback.print_exc()
            info = sys.exc_info()
            raise info[0],info[1]
        finally:
            pass
    return _deco


def SwipeElement(driver,ele,direction,timeout=0.2):
    '''
     元素滑动
    :param driver:
    :param ele:
    :param direction:
    :return:
    '''
    rect = ele.bounds
    scale = driver.scale


    if direction=='right':
        driver.swipe((rect.x + rect.width/2) * scale,
                     (rect.y + rect.height-1) * scale,
                     (rect.x + rect.width-1) * scale,
                     (rect.y + rect.height-1) * scale, timeout)
    elif direction == 'left':
        driver.swipe((rect.x + rect.width-1) * scale,
                     (rect.y + rect.height-1) * scale,
                     (rect.x + rect.width/2) * scale,
                     (rect.y + rect.height-1) * scale, timeout)
    elif direction == 'up':
        driver.swipe((rect.x + rect.width-1) * scale,
                     (rect.y + rect.height-1) * scale,
                     (rect.x + rect.width-1) * scale,
                     (rect.y + rect.height/2) * scale, timeout)
    elif direction == 'down':
        driver.swipe((rect.x + rect.width-1) * scale,
                     (rect.y + rect.height/2) * scale,
                     (rect.x + rect.width-1) * scale,
                     (rect.y + rect.height-1) * scale, timeout)
    else:
        return