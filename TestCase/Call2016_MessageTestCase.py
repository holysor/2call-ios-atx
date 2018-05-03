#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-08-24'

import unittest

import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm
from Profile import config

import time



class Messagetest(unittest.TestCase):
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
            短信UI--有短信/无短信
        '''

        self.driver(label=u"Messages").click()

        while self.driver(className="Cell")[0].exists:
            sleep(1)
            self.driver.swipe(1200,280,500,280,2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()


        self.assertTrue(self.driver(name=u"ic_call_defaultimg").exists)
        self.assertTrue(self.driver(label=u"No message records").exists)
        self.assertTrue(self.driver(label = u"btn whitesidebar nomal").exists)
        self.assertTrue(self.driver(label=u"btn addnew nomal").exists)
        self.assertTrue(self.driver.exists("pic/messages_tabBar.2208x1242.png"))

        #Crete new message
        self.driver(label = u"btn addnew nomal").click()
        self.driver(label=u"Address Bar Text View").set_text("19093036369")
        self.driver(label=u"+1 909-303-6369").click()
        self.driver(label = u"Message Input Toolbar Text Input View").set_text('Hi~')
        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"+1 909-303-6369").exists)
        self.driver(label=u"Cancel").click()
        sleep(2)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText").text,'+1 909-303-6369')
        self.assertTrue(not self.driver(label=u"No message records").exists)
        self.assertTrue(not self.driver(name=u"ic_call_defaultimg").exists)

        while self.driver(className="Cell")[0].exists:
            sleep(1)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()

    def test_02(self):
        '''
            编辑短信入口-UI
        '''
        self.driver(label=u"Messages").click()
        self.driver(label = u"btn addnew nomal").click()

        self.assertTrue(self.driver(label=u"New Message").exists)
        self.assertTrue(self.driver(label=u"Cancel").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Camera Button").exists)
        self.assertTrue(self.driver(label=u"Cancel").exists)
        self.assertTrue(self.driver(label=u"To:").exists)
        self.assertTrue(self.driver(label=u"Address Bar Text View").exists)
        self.assertTrue(self.driver(label=u"Add Contacts Button").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Text Input View").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Send Button").exists)
        self.assertTrue(self.driver(label=u"Enter Message").exists)
        self.assertTrue(self.driver(className="Key").exists)

        self.driver(label=u"Cancel").click()
        self.assertTrue(self.driver.exists("pic/messages_tabBar.2208x1242.png"))

    def test_03(self):
        '''
            编辑短信入口--输入收件人号码发送短信
        '''
        self.driver(label=u"Messages").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()

        self.driver(label = u"btn addnew nomal").click()
        self.driver(label=u"Address Bar Text View").set_text("19093036369")
        self.driver(label=u"+1 909-303-6369").click()

        #添加文字
        self.driver(label = u"Message Input Toolbar Text Input View").set_text("Hi~ this is test message ,wish you happy every day")
        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"+1 909-303-6369").exists)
        self.driver(label=u"Cancel").click()
        sleep(2)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[1]").text,'+1 909-303-6369')
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[2]").text,'Hi~ this is test message ,wish you happy every day')
        self.driver(className="Cell").click()
        sleep(2)
        self.assertEqual(self.driver(className="TextView")[2].text,"Hi~ this is test message ,wish you happy every day")
        self.driver(label=u"btn back nomal").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()

    def test_04(self):
        '''
            编辑短信入口--从联系人添加,发送图片
        '''

        # self.driver(label = u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").wait(timeout=10.0)
        self.driver(label=u"+1 520-214-1991").click()
        self.driver(label=u"btn whitesidebar nomal").click()

        self.driver(label=u"Messages").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()

        self.driver(label=u"btn addnew nomal").click()
        self.driver(label = u"Add Contacts Button").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Contacts").exists)

        self.driver(label=u"Ca").click()
        self.driver(label="NEXT").click()
        sleep(2)
        self.assertEqual(self.driver(label="Address Bar Text View").text,'Ca, ')

        # 添加图片
        self.driver(label = u"Message Input Toolbar Camera Button").click()
        self.driver(className="Cell")[0].click()
        self.assertTrue(self.driver(name=u"ImageSelectedOn").exists)
        self.driver(label=u"Send").click()
        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(2)
        self.driver(label=u"Cancel").click()
        sleep(2)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[1]").text, 'Ca')
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[2]").text,'[pic]')
        self.driver(className="Cell").click()
        self.assertTrue(not self.driver(xpath="//Cell[1]/StaticText[2]").exists)
        self.driver(label=u"btn back nomal").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
            if self.driver(label=u"Delete").exists:
                self.driver(label=u"Delete").click()

    def test_05(self):

        '''
            短信收发界面
        '''

        self.driver(label=u"Messages").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            self.driver(label=u"Delete").click()

        self.driver(label=u"btn addnew nomal").click()
        self.driver(label=u"Address Bar Text View").set_text("19093036369")
        self.driver(label=u"+1 909-303-6369").click()

        # 添加文字
        self.driver(label=u"Message Input Toolbar Text Input View").set_text(
            "Hi~ this is test message ,wish you happy every day")
        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(2)
        self.driver(label=u"Cancel").click()
        sleep(2)
        self.driver(className="Cell").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Details").exists)
        self.assertTrue(self.driver(label=u"btn back nomal").exists)
        # self.assertTrue(self.driver(label=u"+1 909-303-6369").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Camera Button").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Text Input View").exists)
        self.assertTrue(self.driver(label=u"Message Input Toolbar Send Button").exists)
        if self.driver(label=u"btn back nomal").exists:
            self.driver(label=u"btn back nomal").click()
        else:
            self.driver(className="Button")[0].click()
        sleep(2)
        self.driver.swipe(1200, 280, 300, 280, 3.0)
        self.driver(label=u"Delete").click()


    def test_06(self):
        '''
           短信收发界面-短信发送-短信及图片
        '''
        self.driver(label=u"Messages").click()

        while self.driver(className="Cell")[0].exists:
            sleep(2)
            self.driver.swipe(1200, 280, 500, 280, 2.0)
            self.driver(label=u"Delete").click()

        self.driver(label=u"btn addnew nomal").click()
        self.driver(label=u"Address Bar Text View").set_text("19093036369")
        self.driver(label=u"+1 909-303-6369").click()

        # 添加文字
        self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                "Hi~ this is test message ,wish you happy every day")
        self.driver(label=u"Message Input Toolbar Send Button").click()
        self.driver(className="Cell").click()

        self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                "Thank you for your wishes")
        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(2)
        self.assertEqual(self.driver(className="TextView")[3].text,
                         'Thank you for your wishes')

        #发送图片--快捷图片
        self.driver(label=u"Message Input Toolbar Camera Button").click()
        self.driver(className="Cell")[3].click()
        self.assertTrue(self.driver(name=u"ImageSelectedOn").exists)
        self.driver(className="Cell")[4].click()
        sleep(1)
        self.assertTrue(self.driver(label=u"You can only choose 1 images").exists)
        self.driver(label="OK").click()
        self.driver(label=u"Send").click()
        self.driver(label=u"Message Input Toolbar Text Input View").click()


        # #发送图片--拍照
        # self.driver(label=u"Message Input Toolbar Camera Button").click()
        # self.driver(label=u"Take Photo").click()
        # sleep(3)
        # self.assertTrue(self.driver(label=u"Camera Mode").exists)
        # self.assertTrue(self.driver(label=u"Cancel").enabled)
        # self.assertTrue(self.driver(label=u"Camera chooser").enabled)
        # self.driver(label = u"Take Picture").click()
        # self.assertTrue(self.driver(label=u"Retake").enabled)
        # sleep(2)
        # self.driver(label=u"Use Photo", name=u"Use Photo", className="Button").click()
        # sleep(2)
        # self.driver(label=u"Message Input Toolbar Text Input View").click()
        # sleep(2)
        # while not self.driver(label=u"Enter Message").exists:
        #     self.driver(label=u"delete").click()  # 删除输入框内图片

        #发送图片--图库
        self.driver(label=u"Message Input Toolbar Camera Button").click()
        self.driver(label=u"Photo Library").click()
        # self.driver(label=u"Camera Roll").click()
        # self.driver(label=u"Photos").click()
        # sleep(2)
        if self.driver(label="Fast Repost").exists:
            self.driver(label="Fast Repost").click()
        else:
            self.driver(label="All Photos").click()
        sleep(2)
        self.driver(className="Cell")[-1].click()

        # self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(2)
        if self.driver(label=u"btn back nomal").exists:
            self.driver(label=u"btn back nomal").click()
        else:
            self.driver(label=u"Cancel").click()

        while self.driver(type="Cell").exists:
            sleep(2)
            pfm.SwipeElement(self.driver,self.driver(type="Cell"),'left',3)
            self.driver(label=u"Delete").click()
        sleep(1)

    def test_07(self):
        '''
            短信扣费-扣除套餐短信条数
        '''
        self.driver(label=u"Messages").click()
        while self.driver(className="Cell").exists:
            sleep(2)
            pfm.SwipeElement(self.driver,self.driver(type="Cell"),'left',3)
            self.driver(label=u"Delete").click()

        self.driver(label="2Call").click()

        messages_send_before = int(self.driver(xpath="//Table/StaticText[5]").text.split(' ')[0])

        self.assertTrue(messages_send_before>0)
        self.driver(label=u"Messages").click()

        self.driver(label=u"btn addnew nomal").click()
        self.driver(label=u"Address Bar Text View").set_text("19093036369")
        self.driver(label=u"+1 909-303-6369").click()
        self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                "Hi~ this is test message ,wish you happy every day")

        self.driver(label=u"Message Input Toolbar Send Button").click()
        sleep(1)
        self.driver(label="Cancel").click()
        sleep(2)

        self.driver(label="2Call").click()
        self.driver(label=str(messages_send_before-1)+" Messages").wait(timeout=20.0)
        self.driver(label=u"Messages").click()
        while self.driver(className="Cell").exists:
            sleep(2)
            pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
            self.driver(label=u"Delete").click()


    def test_08(self):
        '''
            短息收发界面--detail
        '''
        self.driver(label=u"Messages").click()
        if not self.driver(className="Cell")[0].exists:
            self.driver(label=u"btn addnew nomal").click()
            self.driver(label=u"Address Bar Text View").set_text("19093036369")
            self.driver(label=u"+1 909-303-6369").click()
            self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                    "Hi~ this is test message ,wish you happy every day")
            self.driver(label=u"Message Input Toolbar Send Button").click()
            self.driver(label="Cancel").click()

        self.driver(className="Cell")[0].click()
        self.driver(label=u"Details").click()

        #UI 元素验证
        self.assertTrue(self.driver(label = u"+1 909-303-6369").exists)
        self.assertTrue(self.driver(label=u"icon call use").exists)
        if not self.driver(label=u"Block This Number").exists:
            self.assertTrue(self.driver(label=u"UnBlock This Number").exists)
            self.driver(label=u"UnBlock This Number").click()
            self.driver(label="Sure").click()
            sleep(3)
        self.assertTrue(self.driver(label=u"Block This Number").exists)

        #拨号
        self.driver(label = u"icon call use").click()
        self.driver(label=u"btn hangup nomal").click()

        #block
        self.driver(label=u"Block This Number").click()
        sleep(1)
        self.assertEqual(self.driver.session.alert.text,"Oops\nSure to block? You'll not receive phone calls or messages from people on the block list.")


        self.driver(label="Sure").click()
        sleep(3)
        if not self.driver(label=u"UnBlock This Number").exists:
            self.driver(label=u"Block This Number").click()
            self.driver(label="Sure").click()
            sleep(3)
        self.assertTrue(self.driver(label=u"UnBlock This Number").exists)
        self.driver(label=u"UnBlock This Number").click()

        self.assertEqual(self.driver.session.alert.text,
                         "Oops\nAre you sure to unblock this number? You may receive messages and calls from this number then.")

        self.driver(label="Sure").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Block This Number").exists)


    def test_09(self):
        '''
            短信保存联系人至本地:短信--detail--edit
        '''
        self.driver(label=u"Messages").click()
        if not self.driver(className="Cell")[0].exists:
            self.driver(label=u"btn addnew nomal").click()
            self.driver(label=u"Address Bar Text View").set_text("18008002775")
            self.driver(label=u"+1 909-303-6369").click()
            self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                    "Hi~ this is test message ,wish you happy every day")
            self.driver(label=u"Message Input Toolbar Send Button").click()
            self.driver(label="Cancel").click()

        self.driver(className="Cell")[0].click()
        self.driver(label=u"Details").click()
        self.driver(label=u"Edit").click()
        self.driver(className="TextField")[0].clear_text()

        self.driver(className="TextField")[0].set_text('A_Tester')
        self.driver(label=u"Done").click()
        self.driver(label=u"btn back nomal").click()
        self.driver(label=u"btn back nomal").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"A_Tester").exists)

        self.driver(label=u"Contacts").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"A_Tester").exists)
        self.driver(label=u"A_Tester").click()
        self.assertTrue(self.driver(label=u"+1 800-800-2775").exists)
        sleep(2)
        self.driver(label=u"Edit").click()
        self.driver(className="TextField")[0].clear_text()
        sleep(2)
        self.driver(label=u"Done").click()
        sleep(3)

    def test_10(self):

        '''
            短信列表-左划功能菜单:2Call,call
        '''

        self.driver(label=u"Messages").click()
        sleep(2)
        while self.driver(className="Cell").exists:
            sleep(2)
            pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
            self.driver(label=u"Delete").click()
        if not self.driver(className="Cell")[0].exists:
            self.driver(label=u"btn addnew nomal").click()
            self.driver(label=u"Address Bar Text View").set_text("19093036369")
            self.driver(label=u"+1 909-303-6369").click()
            self.driver(label=u"Message Input Toolbar Text Input View").set_text(
                    "Hi~ this is test message ,wish you happy every day")
            self.driver(label=u"Message Input Toolbar Send Button").click()
            self.driver(label="Cancel").click()

        sleep(2)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
        sleep(2)
        self.driver(className='Cell').child(label=u"2Call").click()
        self.driver(label="Add to App Contacts").click()
        self.driver(label=u"Cancel").click()
        sleep(2)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)

        sleep(2)
        self.driver(className='Cell').child(label=u"2Call").click()

        self.driver(label="Copy Number").click()
        sleep(3)
        self.driver(className="Cell")[0].click()
        self.driver(label=u"Message Input Toolbar Text Input View").click()

        self.driver(label=u"Message Input Toolbar Text Input View").tap_hold(3)
        self.driver(label=u"Paste").click()
        self.assertEqual(self.driver(label=u"Message Input Toolbar Text Input View").text,'+19093036369')
        self.driver(label=u"btn back nomal").click()
        sleep(2)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
        sleep(2)
        self.driver(className='Cell').child(label=u"2Call").click()
        self.driver(label=u"Block This Number").click()
        self.driver(label="Sure").click()
        sleep(6)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
        sleep(2)
        self.driver(className='Cell').child(label=u"2Call").click()
        self.driver(label=u"UnBlock This Number").click()
        self.driver(label="Sure").click()
        sleep(5)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 4)
        sleep(2)
        self.driver(className='Cell').child(label=u"2Call").click()
        self.assertTrue(self.driver(label=u"Block This Number").exists)
        self.driver(label="Cancel").click()

        sleep(3)
        pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', 3)
        sleep(2)
        self.driver(label="Call").click()
        self.driver(label=u"btn hangup nomal").click()


