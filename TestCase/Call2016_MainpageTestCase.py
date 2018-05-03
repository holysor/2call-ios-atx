#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-07-13'

import unittest

import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm
from Profile import config

class Mainpagetest(unittest.TestCase):

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
            main page
        '''
        sleep(5)
        # self.report.assert_image_exists('pic/TabBar.2208x1242.png',timeout=20.0,safe=True)
        self.assertTrue(self.driver.exists('pic/TabBar.2208x1242.png'),'TabBar')
        # self.assertTrue(self.driver.exists('pic/CallsUi.2208x1242.png'),'TabBar')
        self.assertTrue(self.driver(label="Calls", name="Calls", className="Button").exists)
        self.assertTrue(self.driver(label="Messages", name="Messages", className="Button").exists)
        self.assertTrue(self.driver(label="Contacts", name="Contacts", className="Button").exists)
        self.assertTrue(self.driver(label="Keypad", name="Keypad", className="Button").exists)
        self.assertTrue(self.driver(label="2Call", name="2Call", className="Button").exists)
        self.assertTrue(self.driver(label="Call", name="Call", className="StaticText").exists)
        # self.assertTrue(self.driver(label="btn whitesidebar nomal", name="btn whitesidebar nomal", className="Button").exists)


        self.assertTrue(self.driver(className="StatusBar").exists)



    def test_02(self):
        '''
            2call:call tabbar test
        '''
        sleep(2)
        while self.driver(className="Cell").exists:
            if not self.driver(label="Edit").exists:
                self.driver(label="Messages").click()
                self.driver(label="Calls").click()
                self.driver(label = "Edit").click()
            if self.driver(label="Edit").exists:
                self.driver(label = "Edit").click()
            self.driver.click_image('pic/delete_icon.2208x1242.png')
            self.driver(label="Delete").click()
            if self.driver(label="Done").exists:
                self.driver(label="Done").click()

        self.driver(label="Keypad", name="Keypad", className="Button").click()
        phonenumber = '8008002775'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        calltime = self.driver(xpath="//StatusBar/Other[2]/Other[3]").text
        self.driver(label="btn answer nomal").click()

        sleep(5)
        self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
        self.driver(label="Calls").click()
        sleep(10)
        self.assertEqual(self.driver(type = "StaticText")[3].text,'+1 800-800-2775')
        # self.assertEqual(self.driver(xpath="//StaticText")[3].text,calltime,'拨号时间显示')

        if not self.driver.exists('pic/detail.2208x1242.png'):
            self.driver(label="Messages").click()
            self.driver(label="Calls").click()
            self.driver(label="Done").click()

        self.assertTrue(self.driver.exists('pic/detail.2208x1242.png'))
        sleep(2)
        while self.driver(className="Cell").exists:
            if not self.driver(label="Edit").exists:
                self.driver(label="Messages").click()
                self.driver(label="Calls").click()
                self.driver(label="Edit").click()
            if self.driver(label="Edit").exists:
                self.driver(label="Edit").click()
            self.driver.click_image('pic/delete_icon.2208x1242.png')
            self.driver(label="Delete").click()
            if self.driver(label="Done").exists:
                self.driver(label="Done").click()

    def test_03(self):
        '''
            详情页面UI
        '''

        self.driver(label="Keypad", name="Keypad", className="Button").click()
        phonenumber = '8008002775'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.driver(label="btn answer nomal").click()
        sleep(5)
        self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
        self.driver(label="Calls").click()
        self.driver(label="Messages").click()
        self.driver(label="Calls").click()
        self.driver(label="btn call detial nomal").wait(timeout=10.0)
        calltime = self.driver(className="StaticText")[4].text
        self.driver(label="btn call detial nomal").click()
        sleep(3)
        self.assertTrue(self.driver(name=u"ic_head").exists)
        self.assertTrue(self.driver(label=u"Message").exists)
        self.assertTrue(self.driver(label=u"Call", name=u"Call", type="Button").exists)
        self.assertTrue(self.driver(label=u"Share").exists)
        self.assertTrue(self.driver(label=u"Look up").exists)

        self.assertEqual(self.driver(className='StaticText')[3].text,calltime)
        self.assertEqual(self.driver(className='StaticText')[4].text,calltime)
        self.assertEqual(self.driver(className='StaticText')[5].text,'Outgoing Call')
        self.assertTrue('seconds' in self.driver(className='StaticText')[6].text)

        self.assertTrue(self.driver(label="Send Message").exists)

        self.assertTrue(self.driver(label=u"Share Contacts").exists)
        self.assertTrue(self.driver(label=u"Block this Caller").exists)
        self.assertTrue(self.driver(label=u"Look up", name=u"Look up", type="StaticText").exists)

        # self.assertTrue(self.driver(label="Create New Contact Inside the APP").exists)
        # self.assertTrue(self.driver(label='+86 '+phonenumber).exists)


    @unittest.skip('test_04:待完善')
    def test_04(self):
        '''
            通话记录-详情页面-短信,电话,创建联系人
        '''
        self.driver(label="btn call detial nomal").wait(timeout=10.0)
        phonenum = self.driver(xpath="//Cell[1]/StaticText[2]").text

        self.driver(label="btn call detial nomal").click()

        self.assertTrue(self.driver(label=phonenum).exists)
        self.assertTrue(self.driver(label="mobile").exists)
        self.assertEqual(self.driver(className="StaticText")[1].text,phonenum)
        # self.assertTrue(self.driver(label="Create New Contact Inside the APP").exists)
        # self.assertTrue(self.driver(label="icon call use").exists)
        self.assertTrue(self.driver(label="Block This Number").exists)
        self.driver(label="icon call use").click()
        self.driver(label="btn hangup nomal").click()
        # self.driver(label="Create New Contact Inside the APP").click()
        sleep(3)
        # self.assertTrue(self.driver.exists("pic/create_contact_icon.2208x1242.png"))
        # self.driver(label="Cancel").click()
        self.driver(label="Block This Number").click()
        message = "Sure to block? You'll not receive phone calls or messages from people on the block list."
        self.assertEqual(self.driver.session.alert.text,"Oops\n"+message)

        self.driver(label="Cancel").click()
        self.driver(label="btn back nomal").click()
        self.driver(label="Cancel").click()
        self.driver(label="Send Message").click()
        self.driver(label="Cancel").click()
        # self.driver(label="Create New Contact Inside the APP").click()
        # sleep(3)
        # self.assertTrue(self.driver.exists("pic/create_contact_icon.2208x1242.png"))
        # self.driver(label="Cancel").click()
        # self.driver(label = "btn back nomal").click()

    def test_05(self):
        '''
            通话详情页面-拨号
        :return:
        '''
        self.driver(label="btn call detial nomal").wait(timeout=10.0)
        self.driver(label="btn call detial nomal").click()
        self.driver(label=u"Call", name=u"Call", type="Button")[2].click()
        self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
        sleep(4)
        self.driver(name=u"ic_head").wait(timeout=10.0)

    def test_06(self):
        '''
            通话详情页面-分享
        :return:
        '''
        self.driver(label="btn call detial nomal").wait(timeout=10.0)
        self.driver(label="btn call detial nomal").click()
        self.driver(label=u"Share").click()
        self.driver(label=u"Mail").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"New Message").exists,'New Message')
        self.assertTrue(self.driver(text="Number: +18008002775").exists)
        self.driver(label="Cancel").click()
        self.driver(label="Delete Draft").click()
        self.driver(name=u"ic_head").wait(timeout=10.0)

        self.driver.swipe(600, 1800, 600, 750, 2.0)
        self.driver(label=u"Share Contacts").click()
        sleep(3)
        self.assertTrue(self.driver(name=u"ActivityListView").exists)


    def test_07(self):
        '''
            通话详情页面-Look up 查询号码
        :return:
        '''
        self.driver(label="btn call detial nomal").wait(timeout=10.0)
        self.driver(label="btn call detial nomal").click()
        self.driver(label=u"Look up").click()
        sleep(3)
        self.assertTrue(self.driver(type=u"Map").exists)
        self.driver(label=u"btn back nomal").click()
        self.driver.swipe(600, 1800, 600, 750, 2.0)
        self.driver(label=u"Look up", name=u"Look up", type="StaticText").click()
        sleep(3)
        self.assertTrue(self.driver(type=u"Map").exists)

    def test_8(self):
        '''
            call页面,显示通话记录,点击直接拨号
        '''
        sleep(2)
        if self.driver(className="Cell").exists:
            if self.driver(type = "StaticText")[3].text != '+1 800-800-2775':
                while self.driver(className="Cell").exists:
                    if not self.driver(label="Edit").exists:
                        self.driver(label="Messages").click()
                        self.driver(label="Calls").click()
                        self.driver(label="Edit").click()
                    if self.driver(label="Edit").exists:
                        self.driver(label="Edit").click()
                    self.driver.click_image('pic/delete_icon.2208x1242.png')
                    self.driver(label="Delete").click()
                    if self.driver(label="Done").exists:
                        self.driver(label="Done").click()
                self.driver.start_app(config.PACKAGE_NAME)

                self.driver(label="Keypad", name="Keypad", className="Button").click()
                phonenumber = '8008002775'
                for i in phonenumber:
                    self.driver(label=i, name=i, className="Button").click()
                self.driver(label="btn answer nomal").click()

                sleep(5)
                self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()

                self.driver(label="Calls").click()
                sleep(5)
        else:
            self.driver(label="Keypad", name="Keypad", className="Button").click()
            phonenumber = '8008002775'
            for i in phonenumber:
                self.driver(label=i, name=i, className="Button").click()
            self.driver(label="btn answer nomal").click()

            sleep(5)
            self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()

            self.driver(label="Calls").click()
            sleep(5)

        if not self.driver(label=u"+1 800-800-2775").exists:
            self.driver.start_app(config.PACKAGE_NAME)
            sleep(4)
            self.assertTrue(self.driver(label=u"+1 800-800-2775").exists)

        self.driver(className="Cell")[0].click()
        self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
        sleep(4)
        self.assertTrue(self.driver.exists('pic/TabBar.2208x1242.png'), 'TabBar')
        while self.driver(className="Cell").exists:
            if not self.driver(label="Edit").exists:
                self.driver(label="Messages").click()
                self.driver(label="Calls").click()
                self.driver(label="Edit").click()
            if self.driver(label="Edit").exists:
                self.driver(label="Edit").click()
            self.driver.click_image('pic/delete_icon.2208x1242.png')
            self.driver(label="Delete").click()
            if self.driver(label="Done").exists:
                self.driver(label="Done").click()





    # @pfm.ErrorHandle
    # def test_05(self):
    #     '''
    #         同一号码,多次通话,记录次数[存在BUG]
    #     '''
    # sleep(2)
    # while self.driver(className="Cell").exists:
    #     if not self.driver(label="Edit").exists:
    #         self.driver(label="Messages").click()
    #         self.driver(label="Calls").click()
    #         self.driver(label="Edit").click()
    #     if self.driver(label="Edit").exists:
    #         self.driver(label="Edit").click()
    #     self.driver.click_image('pic/delete_icon.2208x1242.png')
    #     self.driver(label="Delete").click()
    #     if self.driver(label="Done").exists:
    #         self.driver(label="Done").click()
    # self.driver.start_app(config.PACKAGE_NAME)
    #
    # self.driver(label="Keypad", name="Keypad", className="Button").click()
    # phonenumber = '8008002775'
    # for i in phonenumber:
    #     self.driver(label=i, name=i, className="Button").click()
    # self.driver(label="btn answer nomal").click()
    #
    # sleep(5)
    # self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
    #
    # self.driver(label="Calls").click()
    # sleep(5)
    # self.assertTrue(self.driver(label="+86 8008002775", name="+86 8008002775", className="StaticText").exists)
    #
    # self.driver(className="Cell")[0].click()
    # self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
    # sleep(5)
    # self.driver(label="Keypad", name="Keypad", className="Button").click()
    # self.driver(label="Calls").click()
    # sleep(2)
    # self.driver(label="Calls").click()
    # sleep(5)
    # self.driver(label="btn hangup nomal", name="btn hangup nomal", className="Button").click()
    # sleep(3)
    #
    # text = self.driver(label="Calls")[0].text
    # self.assertTrue(text.split(' ')[-1][1].isdigit())
