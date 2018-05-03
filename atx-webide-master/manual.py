# -*- encoding: utf-8 -*-
#
# Created on: Tue Jul 25 13:59:05 2017


import os
import atx
from time import sleep

d = atx.connect(os.getenv("SERIAL"))
d.start_app("com.jinming.call")
print('启动成功！')

# d.wait(u"pic/detail.2208x1242.png",timeout=20.0)
# sleep(5)
# c = 1
# for i in d(className="StaticText"):
#     print(c,i.text)
#     c=c+1