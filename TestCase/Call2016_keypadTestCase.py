#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-08-22'

import unittest

import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm
from Profile import config

import time



class Keypadtest(unittest.TestCase):
    def setUp(self):
        self.driver = atx.connect('http://localhost:8100', platform='ios')
        # self.driver.home()
        # self.report = Report(self.driver, save_dir=config.CASE_REPORT_PATH + self._testMethodName)
        # self.report.info("Test Start")
        self.driver.start_app(config.PACKAGE_NAME)
        if self.driver(label=u"Rate 2Call", name=u"Rate 2Call", className="StaticText").exists:
            self.driver(label=u"No, thanks").click()

    def tearDown(self):
        self.driver.stop_app(config.PACKAGE_NAME)
        # self.report.close()

    def test_01(self):
        '''
            keypad ui
        '''
        self.driver(label="Keypad").click()
        sleep(1)
        if self.driver(label="I Know it").exists:
            self.driver(label="I Know it").click()
        self.assertTrue(self.driver.exists('pic/keypad_icon.2208x1242.png'),'键盘')
        self.assertTrue(self.driver.exists('pic/dialing.2208x1242.png'),'拨号键')
        self.assertTrue(self.driver.exists('pic/search_numInfo.2208x1242.png'),'搜索键')
        self.assertTrue(self.driver.exists('pic/clear_num_bt.2208x1242.png'), '清楚键')

        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").exists
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.assertTrue(self.driver(label=u"btn whitesidebar nomal").exists)
        self.assertTrue(self.driver(label=u"btn delete normal").exists)
        self.assertTrue(self.driver(label=u"btn check 01").exists)
        self.assertTrue(self.driver(label=u"btn answer nomal").exists)

    def test_02(self):
        '''
            按键,清除按钮测试
        '''

        self.driver(label="Keypad").click()

        phonenumber = '123456789*0#'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()

        self.assertTrue(self.driver(label=u"123456789*0#").exists)
        self.driver(label=u"btn delete normal").click()
        self.assertEqual(self.driver(className = "StaticText")[2].text,"123456789*0")
        while self.driver(type = "StaticText")[2].text:
            self.driver(label=u"btn delete normal").click()

    def test_03(self):
        '''
            国家区号选择测试
        '''

        self.driver(label="Keypad").click()
        self.assertEqual(self.driver(xpath="//Other/Button[1]").text,'+1','默认国家区号+1')
        # self.assertTrue(self.driver.exists('pic/china.2208x1242.png'), '中国旗帜')
        self.driver(xpath="//Other/Button[1]").click()
        self.assertTrue(self.driver(label=u"Choose Country").exists)
        self.assertTrue(self.driver(label=u"Cancel").exists)
        # self.assertTrue(self.driver.exists('pic/choosecountry.2208x1242.png'), '国家区号列表')

        self.driver(label=u"Aland Islands").click()
        self.assertTrue(self.driver(label=u"+35818").exists)
        self.driver(label=u"+35818").click()
        # self.assertTrue(self.driver.exists('pic/after_selected_code.2208x1242.png'), '选择记录')


    def test_04(self):
        '''
            字母快捷滚动条,搜索栏
        '''

        #字母快捷滚动条
        self.driver(label="Keypad").click()
        self.driver(xpath="//Other/Button[1]").click()
        self.assertTrue(self.driver(label=u"table index").exists,'字母滚动条')
        self.driver.click(1215, 1479)
        sleep(3)
        self.assertTrue(self.driver.exists('pic/scrollbar.2208x1242.png'), '点击s得出搜索结果')
        self.driver(label=u"Cancel").click()
        self.driver(xpath="//Other/Button[1]").click()

        #搜索栏
        self.driver(label=u"enter country name or country code").click()
        self.driver(label=u"Cancel").click()
        self.driver(label=u"enter country name or country code").click()
        self.driver(label=u"enter country name or country code").set_text("us")
        self.driver(label=u"Search").click()
        sleep(2)
        self.assertTrue(self.driver.exists('pic/search_result.2208x1242.png'), '搜索结果')
        self.driver(label=u"Cancel").click()
        self.driver(label=u"enter country name or country code").click()
        self.driver(label=u"enter country name or country code").set_text("86")
        self.assertTrue(self.driver.exists('pic/search_code.2208x1242.png'), 'code搜索结果')

    def test_05(self):
        '''
            查询号码信息页面-未付费UI
        '''
        self.driver(label="Keypad").click()
        self.driver(xpath="//Other/Button[1]").click()
        self.driver.click(1221, 1560)
        self.driver.wait("pic/usa.2208x1242.png", timeout=10.0)
        self.driver.click_image("pic/usa.2208x1242.png")
        sleep(2)
        # self.driver(label=u"United States", name=u"United States", className="StaticText").click()
        phonenumber = '5202145869'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.assertTrue(self.driver(label=u"(520) 214-5869").exists)

        self.driver(label=u"btn check 01").click()

        self.driver(label=u"Unlock all details with a Premium Search").wait(timeout=10)
        sleep(2)
        self.assertTrue(self.driver(label=u"Map pin").exists)
        self.assertTrue(self.driver(label=u"Tucson, AZ 85701").exists)
        self.assertTrue(self.driver(label=u"PREMIUM").exists)
        # self.assertTrue(self.driver.exists('pic/phonecheckinfo.2208x1242.png'), '查询号码信息页面')
        self.assertTrue(self.driver(label=u"Go 100").exists)
        self.driver.swipe(600, 1800, 600, 750, 2.0)
        # self.assertTrue(self.driver.exists('pic/afterswipcheckinfo.2208x1242.png'), '滑动显示隐藏号码信息页面')
        self.driver(label=u"btn back nomal").click()


    def test_06(self):
        '''
            查询号码信息页面-已付费UI

        '''
        self.driver(label="Keypad").click()
        self.driver(xpath="//Other/Button[1]").click()
        self.driver.click(1221, 1560)
        self.driver.wait("pic/usa.2208x1242.png", timeout=10.0)
        self.driver.click_image("pic/usa.2208x1242.png")
        sleep(2)
        # self.driver(label=u"United States", name=u"United States", className="StaticText").click()
        phonenumber = '5209546857'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.assertTrue(self.driver(label=u"(520) 954-6857").exists)
        self.driver(label=u"btn check 01").click()
        sleep(3)
        self.driver.swipe(600, 1800, 600, 850, 1.0)
        sleep(1)
        if self.driver.exists('pic/phonecheckinfo.2208x1242.png'):
            self.driver(className="Button")[-1].click()
            self.driver.wait_gone("pic/phonecheckinfo.2208x1242.png")
            sleep(3)
            self.driver.swipe(600, 1800, 600, 850, 1.0)
        sleep(2)
        # self.assertTrue(not self.driver(label=u"Unlock all details with a Premium Search").exists)
        if self.driver(label=u"Unlock all details with a Premium Search").exists:
            self.driver(label=u"Go 100").click()

        sleep(2)
        self.assertTrue(not self.driver(label=u"Unlock all details with a Premium Search").exists)


        # self.assertTrue(self.driver.exists("pic/result_check_info.2208x1242.png"),'付费显示号码信息结果')

    def test_07(self):

        '''
            录音测试--打开/关闭
        '''

        self.driver(label="Keypad").click()
        if not self.driver(label=u"btn recording hd normal").exists:
            return
        self.assertTrue(self.driver(label=u"Recording Mode: Off").exists)
        self.driver(label=u"btn recording hd normal").click()
        hdmsg = u"HD recording can record your call clearly, the record will be saved in the app after the recording. HD recording will cost double call length. Please don’t enable this function if not necessary."
        sleep(2)
        self.assertTrue(self.driver(label=hdmsg).exists)
        self.assertTrue(self.driver(label=u"HD Recording").exists)
        self.driver(label='Cancel').click()
        self.driver(label=u"btn recording hd normal").click()
        sleep(2)
        self.driver(label='OK').click()
        self.driver(label=u"HD Recording: On").wait(timeout=10.0)
        self.driver(label=u"btn recording hd normal").click()
        self.driver(label=u"Recording Mode: Off").wait(timeout=10.0)

        self.driver(label=u"btn recording normal").click()
        sleep(2)
        msg = u"Speaker recording is free while it may not be clear enough because of the intercom environment. Please choose HD recording if needed."
        self.assertTrue(self.driver(label=msg).exists)
        self.assertTrue(self.driver(label="Speaker Recording").exists)
        self.driver(label='Cancel').click()

        self.driver(label=u"btn recording normal").click()
        sleep(2)
        self.driver(label='OK').click()
        self.driver(label=u"Speaker Recording: On").wait(timeout=10.0)


        self.driver(label=u"btn recording normal").click()
        self.driver(label=u"Recording Mode: Off").wait(timeout=10.0)

    def test_08(self):
        '''
            录音测试
        '''
        sleep(2)
        self.driver(label="Keypad").click()
        if not self.driver(label=u"btn recording hd normal").exists:
            return

        if not self.driver(label=u"+1 520-214-1991").exists:
            # self.driver(label=u"btn whitesidebar nomal").click()
            if self.driver(label=u"btn dotsidebar nomal").exists:
                self.driver(label=u"btn dotsidebar nomal").click()
            elif self.driver(label=u"btn whitesidebar nomal").exists:
                self.driver(label=u"btn whitesidebar nomal").click()
            self.driver(label=u"+1 520-214-1991").click()
            # self.driver(label=u"btn whitesidebar nomal").click()
            if self.driver(label=u"btn dotsidebar nomal").exists:
                self.driver(label=u"btn dotsidebar nomal").click()
            elif self.driver(label=u"btn whitesidebar nomal").exists:
                self.driver(label=u"btn whitesidebar nomal").click()
            self.driver(label="Keypad").click()

        if not self.driver(label=u"+1").exists:
            self.driver(xpath="//Other/Button[1]").click()
            self.driver.click(1221, 1560)
            self.driver.wait("pic/usa.2208x1242.png", timeout=10.0)
            self.driver.click_image("pic/usa.2208x1242.png")

        phonenumber = '8008002775'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.assertTrue(self.driver(label=u"(800) 800-2775").exists)

        if not self.driver(label=u"Recording Mode: Off").exists:
            self.driver(label=u"btn recording hd normal").click()
            sleep(1)
            self.driver(label=u"Recording Mode: Off").wait(timeout=20)
        sleep(3)

        self.driver(label=u"btn recording hd normal").click()
        self.driver(label='OK').click()
        self.driver(label=u"HD Recording: On").wait(timeout=10.0)
        self.driver(label=u"btn answer nomal").click()
        self.driver(label=u"calling...").wait(timeout=10.0)
        while True:
            if not self.driver(label=u"calling...").exists:
                if not self.driver(label=u"btn hangup nomal").exists:
                    self.assertTrue(False, '无法正常拨号')
                    break
                sleep(10)          #延迟,增加通话时间
                break
        self.driver(label=u"btn hangup nomal").click()
        self.driver(label=u"2Call").click()
        self.driver(label=u"Recordings").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"+1 800-800-2775").exists)
        nowtime = time.strftime('%m/%d/%Y',time.localtime(time.time()))
        self.assertTrue(self.driver(label=nowtime).exists)

        self.driver(label=u"btn back nomal").click()
        self.driver(label="Keypad").click()
        self.driver(label=u"btn recording hd normal").click()
        self.driver(label=u"Recording Mode: Off").wait(timeout=10.0)

    def test_09(self):

        '''
            mins left 显示剩余通话时间
        '''
        self.driver(label="Keypad").click()
        sleep(2)
        if not self.driver(label=u"btn recording hd normal").exists:
            calltime_befor = int(self.driver(className="StaticText")[2].text.split(' ')[0])
        else:
            calltime_befor = int(self.driver(className="StaticText")[3].text.split(' ')[0])

        sleep(2)
        if self.driver(label=u"btn recording hd normal").exists:
            if not self.driver(label=u"Recording Mode: Off").exists:
                self.driver(label=u"btn recording hd normal").click()
        self.driver(xpath="//Other/Button[1]").click()
        self.driver.click(1221, 1560)
        self.driver.wait("pic/usa.2208x1242.png", timeout=10.0)
        self.driver.click_image("pic/usa.2208x1242.png")
        phonenumber = '8008002775'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.assertTrue(self.driver(label=u"(800) 800-2775").exists)
        self.driver(label=u"btn answer nomal").click()
        self.driver(label=u"calling...").wait(timeout=10.0)
        self.driver(label=u"calling...").wait_gone(timeout=10.0)


        sleep(8)  # 延迟,增加通话时间

        self.driver(label=u"btn hangup nomal").click()
        self.driver(label=u"btn answer nomal").wait(timeout=10)

        sleep(2)
        self.driver.start_app(config.PACKAGE_NAME)
        self.driver(label=u"2Call").click()

        self.driver(label=str(calltime_befor-1) + " Mins").wait(timeout=20.0)
        self.driver(label="Keypad").click()

        if self.driver(label=u"btn recording hd normal").exists:
            calltime_after = int(self.driver(className="StaticText")[3].text.split(' ')[0])
        else:
            calltime_after = int(self.driver(className="StaticText")[2].text.split(' ')[0])

        self.assertEqual(calltime_befor,calltime_after+1)
        self.assertTrue(self.driver(label=str(calltime_befor-1) + " mins left").exists)


