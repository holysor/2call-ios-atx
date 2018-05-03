#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-11-2'

import unittest

import atx
from time import sleep
from Profile import profilemethod as pfm
from Profile import config

class BuyNumberTest(unittest.TestCase):

    def setUp(self):
        self.driver = atx.connect('http://localhost:8100', platform='ios')
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
            购买号码-套餐界面
        :return:
        '''
        sleep(2)
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()

        self.driver(label=u"Add New Number").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Select a package for your phone number.").exists)

        package_1_name = self.driver(xpath="//Cell[1]/StaticText[1]").text
        package_1_messages = self.driver(xpath="//Cell[1]/StaticText[2]").text
        package_1_pic = self.driver(xpath="//Cell[1]/StaticText[3]").text
        package_1_mins = self.driver(xpath="//Cell[1]/StaticText[4]").text
        package_1_price = self.driver(xpath="//Cell[1]/Button").text

        package_2_name = self.driver(xpath="//Cell[2]/StaticText[1]").text
        package_2_messages = self.driver(xpath="//Cell[2]/StaticText[2]").text
        package_2_pic = self.driver(xpath="//Cell[2]/StaticText[3]").text
        package_2_mins = self.driver(xpath="//Cell[2]/StaticText[4]").text
        package_2_price = self.driver(xpath="//Cell[2]/Button").text

        package_3_name = self.driver(xpath="//Cell[3]/StaticText[1]").text
        package_3_messages = self.driver(xpath="//Cell[3]/StaticText[2]").text
        package_3_pic = self.driver(xpath="//Cell[3]/StaticText[3]").text
        package_3_mins = self.driver(xpath="//Cell[3]/StaticText[4]").text
        package_3_price= self.driver(xpath="//Cell[3]/Button").text

        package_4_name = self.driver(xpath="//Cell[4]/StaticText[1]").text
        package_4_messages = self.driver(xpath="//Cell[4]/StaticText[2]").text
        package_4_pic = self.driver(xpath="//Cell[4]/StaticText[3]").text
        package_4_mins = self.driver(xpath="//Cell[4]/StaticText[4]").text
        package_4_price = self.driver(xpath="//Cell[4]/Button").text

        self.assertEqual(package_1_messages,'10 Messages')
        self.assertEqual(package_1_mins,'10 Minutes')
        self.assertEqual(package_1_pic,'0 Pics')
        self.assertEqual(package_1_price,'Get 7 days for $3.99')

        self.assertEqual(package_2_messages, '300 Messages')
        self.assertEqual(package_2_mins, '120 Minutes')
        self.assertEqual(package_2_pic, '20 Pics')
        self.assertEqual(package_2_price, 'Get 1 month for $9.99')

        self.assertEqual(package_3_messages, '360 Messages')
        self.assertEqual(package_3_mins, '120 Minutes')
        self.assertEqual(package_3_pic, '0 Pics')
        self.assertEqual(package_3_price, 'Get 12 months for $1.99/Month')

        self.assertEqual(package_4_messages, '1800 Messages')
        self.assertEqual(package_4_mins, '720 Minutes')
        self.assertEqual(package_4_pic, '120 Pics')
        self.assertEqual(package_4_price, 'Get 12 months for $4.99/Month')

    def test_02(self):
        '''
            Buy number :
            1.设置中登出appstore 账号
            2.进入2call 套餐页面选择购买
            3.输入内购账号和密码

        :return:
        '''
        sleep(2)

        #处理内购弹窗阻碍
        if self.driver(label=u"Sign-In Required", name=u"Sign-In Required", type="StaticText").exists:
            self.driver(label='Cancel').click()
        if self.driver(label=u"Sign In to iTunes Store", name=u"Sign In to iTunes Store", type="StaticText").exists:
            self.driver(label='Cancel').click()
        if self.driver(label=u"Confirm purchase", name=u"Confirm purchase", type="StaticText").exists:
            self.driver(label='Cancel').click()


        self.driver.start_app('com.apple.Preferences')
        sleep(3)
        if self.driver(label=u"Settings", name=u"Settings", type="Button").exists:
            self.driver(label=u"Settings", name=u"Settings", type="Button").click()
            sleep(2)
        self.driver(label=u"iTunes & App Store", name=u"iTunes & App Store", type="StaticText").wait(timeout=15)
        #滑动查找 设置中商店账号设置栏
        while not self.driver(label=u"iTunes & App Store", name=u"iTunes & App Store", type="StaticText").displayed:
            self.driver.swipe(600, 1800, 600, 750, 2.0)
        self.driver(label=u"iTunes & App Store", name=u"iTunes & App Store", type="StaticText").click()
        sleep(2)
        if not self.driver(label=u"Sign In", name=u"Sign In", type="StaticText").exists:
            self.driver(textContains="Apple ID:").click()
            sleep(2)
            self.driver(label=u"Sign Out").click()
        self.driver(label=u"Sign In", name=u"Sign In", type="StaticText").wait(timeout=20)

        self.driver.start_app(config.PACKAGE_NAME)
        sleep(2)
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()


        self.driver(label=u"Add New Number").click()
        sleep(2)

        self.driver(label=u"Get 7 days for $3.99").wait(timeout=20)
        self.driver(label=u"Get 7 days for $3.99").click()

        self.driver(label=u"Sign In", name=u"Sign In", type="StaticText").wait(timeout=30)

        self.driver(label=u"Use Existing Apple ID").click()

        exit_count = 0
        while True:
            if self.driver(label=u"Sign-In Required", name=u"Sign-In Required", type="StaticText").exists or self.driver(label=u"Sign In to iTunes Store", name=u"Sign In to iTunes Store", type="StaticText").exists:
                break
            sleep(0.2)
            exit_count+=1
            if exit_count==100:
                self.assertTrue(False,'No login account popup!')

        self.driver(type="TextField").set_text(config.Purchase_Account)
        self.driver(type="SecureTextField").set_text(config.Purchase_Password)
        if self.driver(label=u"Buy").exists:
            self.driver(label=u"Buy").click()
        elif self.driver(label=u"OK").exists:
            self.driver(label=u"OK").click()


        self.driver(label=u"Confirm purchase", name=u"Confirm purchase", type="StaticText").wait(timeout=250)
        self.assertEqual(self.driver(textContains='Environment: Sandbox').text.encode('utf-8'),config.PRICE_LIST_PURCHASEINFO['Get 7 days for $3.99'])
        self.driver(label=u"Cancel").click()

        self.driver(label='Get 1 month for $9.99').click()
        self.driver(label=u"Confirm purchase", name=u"Confirm purchase", type="StaticText").wait(timeout=250)
        self.assertEqual(self.driver(textContains='Environment: Sandbox').text.encode('utf-8'),
                         config.PRICE_LIST_PURCHASEINFO['Get 1 month for $9.99'])
        self.driver(label=u"Cancel").click()

        self.driver(label='Get 12 months for $1.99/Month').click()
        self.driver(label=u"Confirm purchase", name=u"Confirm purchase", type="StaticText").wait(timeout=250)
        self.assertEqual(self.driver(textContains='Environment: Sandbox').text.encode('utf-8'),
                         config.PRICE_LIST_PURCHASEINFO['Get 12 months for $1.99/Month'])
        self.driver(label=u"Cancel").click()

        self.driver.swipe(600, 1800, 600, 750, 2.0)

        self.driver(label='Get 12 months for $4.99/Month').click()
        self.driver(label=u"Confirm purchase", name=u"Confirm purchase", type="StaticText").wait(timeout=250)
        self.assertEqual(self.driver(textContains='Environment: Sandbox').text.encode('utf-8'),
                         config.PRICE_LIST_PURCHASEINFO['Get 12 months for $4.99/Month'])
        self.driver(label=u"Cancel").click()
        # self.driver(label=u"Continue").click()

