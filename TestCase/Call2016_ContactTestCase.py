#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-08-22'

import unittest

import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm
from Profile import config
import requests
import json

class ContactTest(unittest.TestCase):
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
            contact ui
        '''

        self.driver(label=u"Contacts").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Contacts").exists)
        self.assertTrue(self.driver(label=u"btn add normal").exists)

        # self.assertTrue(self.driver(label=u"btn whitesidebar nomal").exists)

        self.assertTrue(self.driver(label=u"table index").exists)
        self.assertTrue(self.driver(label=u"Search").exists)
        self.assertTrue(self.driver.exists('pic/contact_tabBar.2208x1242.png'), '底部栏')

    def test_02(self):
        '''
            Contacts- My number
        '''
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()

        self.driver(label=u"+1 520-214-1991").click()
        name = self.driver(xpath="//Cell[1]/StaticText[1]").text
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()

        self.driver(label=u"Contacts").click()

        sleep(2)
        self.assertTrue(self.driver(label=u"Contacts").exists)
        self.assertTrue(name,self.driver(xpath="//Cell[1]/StaticText[1]").text)
        self.assertTrue(self.driver(label=u"My Number: +1 520-214-1991").exists)



    def test_03(self):
        '''
            contacts - phone 获取系统联系人
        :return:
        '''

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

        self.driver(label=u"Contacts").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"My Number: +1 520-214-1991").exists)
        self.driver.start_app('com.apple.mobilephone')
        self.driver(label=u"Contacts").click()
        self.driver(label=u"Add").click()
        self.driver(type="TextField")[1].set_text('maskphone')
        self.driver(type="TextField")[2].set_text('test')
        self.driver(type="TextField")[3].set_text('lianjie')
        self.driver(label=u"Insert add phone").click()
        self.driver(type="TextField")[4].set_text('+15202144396')
        self.driver(label=u"Done").click()
        sleep(2)
        self.driver.start_app(config.PACKAGE_NAME)

        self.driver(label=u"Contacts").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"maskphone test").exists,'系统创建新联系人后,2call 联系人页面未正常显示')
        self.driver(label=u"maskphone test").click()
        self.assertTrue(self.driver(label=u"+15202144396").exists)
        self.driver.start_app('com.apple.mobilephone')
        self.driver(label=u"Contacts").click()
        self.driver(label=u"maskphone test", name=u"maskphone test", type="StaticText").click()
        self.driver(label=u"Edit").click()

        for i in range(6):
            if self.driver(label=u"Delete Contact").displayed:
                break
            self.driver.swipe(600, 1800, 600, 750, 1.0)
        self.assertTrue(self.driver(label=u"Delete Contact").displayed)
        self.driver(label=u"Delete Contact").click()
        self.driver(label = u"Delete Contact").click()


    def test_04(self):
        '''
            contact - 创建新的2call联系人
        :return:
        '''

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
        self.driver(label=u"Contacts").click()
        sleep(2)
        self.driver(label=u"btn add normal").click()
        self.driver(label=u"Contacts", name=u"Contacts", type="Button").click()
        sleep(2)
        self.assertEqual(self.driver(className="TextField")[0].text,'First')
        self.assertEqual(self.driver(className="TextField")[2].text,'Last')
        self.assertEqual(self.driver(className="TextField")[3].text,'Company')

        self.driver(className="TextField")[0].set_text("Tester")
        self.driver(className="TextField")[2].set_text("2call")
        self.driver(className="TextField")[3].set_text("lianjie")

        self.driver(className="TextField")[4].clear_text()
        self.driver(className="TextField")[4].set_text("19093036554")
        self.driver(label=u"Done", name=u"Done", className="Button").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"Tester 2call").exists)
        self.assertTrue(self.driver(label=u"+1 909-303-6554").exists)
        self.assertTrue(self.driver(label=u"2Call", name=u"2Call", className="StaticText").exists)
        self.assertTrue(self.driver(label=u"T").exists)

        for i in range(5):
            if self.driver(label=u"Tester 2call").displayed:
                break
            self.driver.swipe(600, 1800, 600, 750, 1.0)

        self.driver(label=u"Tester 2call", name=u"Tester 2call", type="StaticText").click()
        self.assertTrue(self.driver(label=u"+1 909-303-6554").exists)
        self.assertTrue(self.driver(label=u"Tester 2call").exists)
        self.driver(label=u"btn back nomal").click()

        sleep(2)
        while not self.driver(label=u"Delete").exists:
            pfm.SwipeElement(self.driver,self.driver(label=u"Tester 2call"),direction='left',timeout=2)
            if self.driver(label=u"btn back nomal").exists:
                self.driver(label=u"btn back nomal").click()
                sleep(2)
        self.driver(label=u"Delete").click()
        sleep(4)

    def test_05(self):
        '''
        2call-contact: search - all/phone/2call/google
        '''

        self.driver(label=u"Contacts").click()
        self.driver(label=u"Search").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"All").exists)
        self.assertTrue(self.driver(label=u"Phone").exists)
        self.assertTrue(self.driver(label=u"2Call").exists)
        self.assertTrue(self.driver(label=u"Google").exists)

        self.driver(label=u"All").click()
        self.driver(label=u"Phone", name=u"Phone", type="Button").click()
        sleep(2)
        self.assertTrue(self.driver(xpath="//Cell[1]/StaticText[@name='Phone']").displayed)
        sleep(1)
        self.driver(label=u"2Call", name=u"2Call", type="Button")[2].click()
        sleep(3)
        self.assertTrue(self.driver(xpath="//Table[1]/Cell[2]/StaticText[@name='2Call']").displayed)
        self.driver(label=u"Google").click()

        self.driver(label=u"All").click()
        self.driver(label=u"Search", name=u"Search", type="SearchField").set_text('Ca')
        sleep(2)
        self.assertTrue(self.driver(xpath="//Table[1]/Cell[1]/StaticText[@name='Ca']").exists)


    def test_06(self):
        '''
            contacts - groups
        '''

        self.driver(label=u"Contacts").click()
        self.driver(label=u"Groups").click()
        self.assertTrue(self.driver(label=u"Groups").exists)
        self.driver(label=u"New group").click()
        self.driver(label=u"Bird Fire").click()
        self.driver(label=u"Ca").click()
        self.driver(type="TextField").set_text('test group')
        self.driver(label=u"Done").click()
        sleep(2)

        self.assertTrue(self.driver(label=u"test group (2)").exists)
        self.driver(label=u"test group (2)").click()
        self.assertTrue(self.driver(label=u"Edit Group").exists)
        self.assertTrue(self.driver(label=u"Group name").exists)
        self.assertEqual(self.driver(type="TextField").text,'test group')
        self.assertTrue(self.driver(label=u"Group members (2)").exists)
        self.assertTrue(self.driver(label=u"Bird Fire").exists)
        self.assertTrue(self.driver(label=u"+1 909-303-6554").exists)
        self.assertTrue(self.driver(label=u"Ca").exists)
        self.assertTrue(self.driver(label=u"+1 450-924-0805").exists)

        self.driver(type="TextField").set_text('1')
        self.driver(label=u"Add member").click()
        sleep(1)
        self.driver(label=u"Tester 2").click()
        self.driver(label=u"NEXT").click()
        self.assertTrue(self.driver(label=u"Tester 2").exists)
        self.driver(label=u"Save").click()
        sleep(4)
        self.driver(label=u"btn back nomal").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"test group1 (2)").exists)
        while not self.driver(label="DELETE").exists:
            pfm.SwipeElement(self.driver,self.driver(label=u"test group1 (2)"),'left',timeout=3)

        self.driver(label="DELETE").click()
        sleep(2)
        self.assertTrue(not self.driver(label=u"test group1 (2)").exists)

    def test_07(self):
        '''
            添加联系人 - Group
        '''
        self.driver(label=u"Contacts").click()
        self.driver(label=u"btn add normal").click()
        self.driver(label=u"Group").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Group name", name=u"Group name", type="Other").exists)
        self.assertTrue(self.driver(label=u"table index").exists)
        self.assertTrue(self.driver(label=u"contact normal", name=u"contact normal", type="Button").exists)
        self.assertTrue(self.driver(type="TextField").exists)
        self.assertTrue(self.driver(label=u"Add New Group").exists)
        self.assertTrue(self.driver(label=u"Done").exists)
        self.driver(label=u"Cancel").click()