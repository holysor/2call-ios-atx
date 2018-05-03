#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-07-13'

import unittest
import re,time
import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm

from Profile import config
import threading
from Profile import CloudApi


class Menutest(unittest.TestCase):

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

    # @pfm.ErrorHandle
    def test_01(self):
        '''
            Menu UI Test
        '''
        sleep(4)
        self.driver.wait("pic/menu.2208x1242.png",timeout=20.0)

        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        # self.driver(label="btn whitesidebar nomal").wait(timeout=10.0)
        # self.driver(label="btn whitesidebar nomal").click()
        # self.assertTrue(self.driver.exists('pic/settingList.2208x1242.png'))
        self.assertTrue(self.driver.exists('pic/2call_icon.2208x1242.png'))
        self.assertTrue(self.driver.exists('pic/add.2208x1242.png'))
        self.assertTrue(self.driver.exists('pic/number_selected.2208x1242.png'))
        self.assertTrue(self.driver.exists("pic/menu.2208x1242.png"))
        # self.assertTrue(self.driver.exists("pic/getcoins_icon.2208x1242.png"))
        # self.assertTrue(self.driver.exists("pic/generalsettings_icon.2208x1242.png"))
        # self.assertTrue(self.driver.exists("pic/support_icon.2208x1242.png"))

        account = self.driver(className = "StaticText")[2].text
        self.assertTrue((re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",account)!=None),'邮箱格式不正确')
        phonenum = self.driver(className = "StaticText")[2]
        phonenum_text =phonenum.text
        phonenum.click()
        sleep(1)
        # self.driver(label="btn whitesidebar nomal", name="btn whitesidebar nomal", className="Button").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label="2Call", name="2Call", className="Button").click()

        # self.assertEqual(self.driver(className = "StaticText")[0].text,phonenum_text,'2Call与菜单栏号码对比验证')
        # self.driver(label="btn whitesidebar nomal", name="btn whitesidebar nomal", className="Button").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        #切换账号
        self.driver(label=u"btn settings normal").click()
        sleep(2)
        if self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").exists:
            sleep(2)
            self.driver.swipe(600, 1400, 600, 600, 2.0)
            while not self.driver(label='Sure').exists:
                sleep(1)
                if self.driver(label=u"Change Account", name=u"Change Account", className="StaticText")[2].exists:
                    self.driver(label=u"Change Account", name=u"Change Account", className="StaticText")[2].click()
                else:
                    self.driver(label=u"Change Account").click()
        self.driver(label='Sure').click()

        self.driver(className="TextField").set_text('holysortester@sina.com')
        self.driver(className="SecureTextField").set_text('shanghai12')
        self.driver(label="return").click()
        sleep(3)
        self.driver(label="btn back nomal").click()
        # self.driver(label="btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        sleep(2)
        self.assertTrue(self.driver(label="holysortester@sina.com").exists)
        self.assertTrue(self.driver(label=u"Add New Number").exists)
        # self.assertTrue(self.driver(label="The Second Number").exists)
        # self.assertTrue(self.driver(label="The Third Number").exists)
        # self.assertTrue(self.driver(label="The Fourth Number").exists)

        #切换到原测试账号
        self.driver(label=u"btn settings normal").click()

        sleep(3)
        if self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").exists:
            sleep(2)
            self.driver.swipe(600, 1400, 600, 600, 2.0)
            while not self.driver(label='Sure').exists:
                self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").click()
        self.driver(label='Sure').click()
        self.driver(className="TextField").set_text('315325320@qq.com')
        self.driver(className="SecureTextField").set_text('shanghai12')
        self.driver(label="return").click()
        sleep(3)

        self.driver(label="btn back nomal").click()
        # self.driver(label="btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        sleep(3)
        self.assertTrue(self.driver(label="315325320@qq.com").exists)

    # @pfm.ErrorHandle
    def test_02(self):
        '''
            add number
        '''
        # self.driver(label = "btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        sleep(2)
        if not self.driver(label=u"315325320@qq.com").exists:
            self.driver(label=u"btn settings normal").click()

            if self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").exists:
                self.driver.swipe(600, 1400, 600, 600, 2.0)
                while not self.driver(label='Sure').exists:
                    self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").click()
            self.driver(label='Sure').click()
            self.driver(className="TextField").set_text('315325320@qq.com')
            self.driver(className="SecureTextField").set_text('shanghai12')
            self.driver(label="return").click()
            self.driver(label="btn whitesidebar nomal").click()

        self.driver(label=u"Add New Number").click()
        sleep(2)
        if self.driver(label="PURCHASE NUMBER").exists:
            self.driver(label="Next").click()
        self.assertTrue(self.driver(label=u"Select Package").exists)
        self.driver(label="btn back nomal").click()
        if self.driver(label="btn back nomal").exists:
            self.driver(label="btn back nomal").click()

    def test_03(self):
        '''
        Store
        '''
        # self.driver(label = "btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        sleep(2)
        if not self.driver(label=u"315325320@qq.com").exists:
            self.driver(label=u"btn settings normal").click()
            self.driver.swipe(600, 1400, 600, 600, 2.0)
            if self.driver(label=u"Change Account", name=u"Change Account", className="StaticText").exists:
                while not self.driver(label='Sure').exists:
                    self.driver(label=u"Change Account", name=u"Change Account", className="StaticText")[2].click()
            self.driver(label='Sure').click()
            self.driver(className="TextField").set_text('315325320@qq.com')
            self.driver(className="SecureTextField").set_text('shanghai12')
            self.driver(label="return").click()
            # self.driver(label="btn whitesidebar nomal").click()
            if self.driver(label=u"btn dotsidebar nomal").exists:
                self.driver(label=u"btn dotsidebar nomal").click()
            elif self.driver(label=u"btn whitesidebar nomal").exists:
                self.driver(label=u"btn whitesidebar nomal").click()

        sleep(3)
        self.driver(label="Store").click()
        sleep(2)
        self.assertTrue(self.driver(label="Get Coins").exists)
        self.assertTrue(self.driver(label=u"Get Coins", name=u"Get Coins", type="Button").exists)
        self.assertTrue(self.driver(label=u"Extend number").exists)

        self.assertTrue(self.driver(label="Account balance:").exists)
        self.assertTrue(self.driver(name="icon_coin").exists)
        self.assertTrue(self.driver(label="$ 1.99").exists)
        self.assertTrue(self.driver(label="$ 4.99").exists)
        self.assertTrue(self.driver(label="$ 9.99").exists)
        self.assertTrue(self.driver(label="$ 19.99").exists)
        self.assertTrue(self.driver(label="$ 49.99").exists)

        self.driver(label=u"Extend number").click()
        sleep(1)
        self.assertTrue(self.driver(label=u"Extend Number").exists)
        self.assertTrue(self.driver(label=u"Image Expansion").exists)
        self.assertTrue(self.driver(label=u"Message Expansion").exists)
        self.assertTrue(self.driver(label=u"Popular Expansion").exists)
        self.assertTrue(self.driver(label=u"200").exists)
        self.assertTrue(self.driver(label=u"300").exists)
        self.assertTrue(self.driver(label=u"600").exists)

        self.driver(label="btn back nomal").click()
        sleep(2)
        self.assertTrue(self.driver.exists('pic/TabBar.2208x1242.png'), '主页面底部栏')

    def test_03_freecoins(self):
        '''
            get free coins
        '''
        sleep(2)
        # if int(CloudApi.CLOUD_PARAMETER_SWITCH_CONTROL['freecoins']):
        # self.driver(label="btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label="Store").click()
        sleep(2)
        if self.driver(label=u"Get Free Coins").exists:

            self.assertTrue(self.driver(label=u"Get Free Coins").exists)
            if self.driver(label=u"Get Free Coins").exists:
                if self.driver(label=u"Get Free Coins").displayed:
                    self.driver(label=u"Get Free Coins").click()
                    if self.driver(label=u"If you love our app, please take a moment to feedback it in app store.").exists:
                        self.driver(label=u"Cancel").click()
                        return
                    self.assertTrue(self.driver(name=u"icon_inviteFriends_invite").exists)
                    self.assertTrue(self.driver(label=u"Successfully inviting friends can get 50 gold coins").exists)
                    self.assertTrue(self.driver(label=u"Invitation code:").exists)
                    self.assertIsNotNone(self.driver(xpath="//ScrollView//StaticText[3]").text)
                    self.assertEqual(self.driver(xpath="//ScrollView//Button[1]").text.split(' ')[0], 'Invite')
                    self.assertTrue(self.driver(xpath="//ScrollView//Button[1]").text.split('+')[1].isdigit())
                    self.driver(label=u"btn back nomal").click()


    def test_04(self):
        '''
            setting - ui
        :return:
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"btn settings normal").click()

        self.assertTrue(self.driver(label=u"General Settings").exists)
        self.assertTrue(self.driver(label=u"General").exists)
        self.assertTrue(self.driver(label=u"Ring", name=u"Ring", type="StaticText").exists)
        self.assertTrue(self.driver(label=u"Ring").exists)
        self.assertTrue(self.driver(label=u"Vibrate", name=u"Vibrate", type="StaticText").exists)
        self.assertTrue(self.driver(label=u"Vibrate").exists)
        self.assertTrue(self.driver(label=u"General").exists)
        self.assertTrue(self.driver(label=u"General").exists)
        self.assertTrue(self.driver(label=u"PIN lock", name=u"PIN lock", type="StaticText").exists)
        self.assertTrue(self.driver(label=u"PIN lock").exists)
        self.assertTrue(self.driver(label=u"Import Google Contacts").exists)
        self.assertTrue(self.driver(label=u"Start").exists)
        self.assertTrue(self.driver(label=u"Push Notification").exists)
        self.assertTrue(self.driver(label=u"Push Notification", name=u"Push Notification", type="StaticText").exists)
        self.assertTrue(self.driver(label=u"Push Notification", name=u"Push Notification", type="Switch").exists)
        self.assertTrue(self.driver(label=u"Push Message Content", name=u"Push Message Content", type="StaticText").exists)
        self.assertTrue(self.driver(label=u"Push Message Content", name=u"Push Message Content", type="Switch").exists)
        self.assertTrue(self.driver(label=u"Others").exists)
        self.assertTrue(self.driver(label=u"Support").exists)
        self.assertTrue(self.driver(label=u"Terms of use").exists)
        self.assertTrue(self.driver(label=u"Privacy Policy").exists)
        self.assertTrue(self.driver(nameContains=u"Version").exists)
        self.assertTrue(self.driver(label=u"Change Account").exists)
        self.assertTrue(self.driver(label="Change Account").exists)

    def test_05(self):
        '''
            Upgrade NUmber
        :return:
        '''
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 506-804-4620").click()
        self.driver(label="Upgrade number").click()
        sleep(3)
        self.assertTrue(self.driver(label=u"Upgrade Number").exists)
        self.assertTrue(self.driver(label=u"Get 1 month for $9.99").exists)
        self.assertTrue(self.driver(label=u"Get 12 months for $1.99/Month").exists)
        self.assertTrue(self.driver(label=u"Get 12 months for $4.99/Month").exists)
        self.driver(label=u"btn back nomal").click()

    def test_06(self):

        '''
            侧边栏-号码设置UI
        :return:
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text=='+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()

        sleep(2)
        self.assertTrue(self.driver(label=u"btn back nomal").exists)
        self.assertTrue(self.driver(label=u"+1 520-214-1991").exists)
        self.assertTrue(self.driver(label=u"Upgrade number").exists)
        self.assertTrue(self.driver(label=u"Extend number").exists)
        self.assertTrue(self.driver(label=u"2Call Info").exists)
        self.assertTrue(self.driver(label=u"Rename").exists)
        self.assertTrue(self.driver(label=u"Greetings").exists)
        self.assertTrue(self.driver(label=u"Notes").exists)
        self.assertTrue(self.driver(label=u"Recordings").exists)
        self.assertTrue(self.driver(label=u"Blocked").exists)
        self.assertTrue(self.driver(label=u"Notes").exists)
        self.assertTrue(self.driver(label=u"US").exists)

    def test_07(self):
        '''
            侧边栏-号码设置:Upgrade number/EXtend number
        '''

        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()
        sleep(2)
        self.driver(label=u"Upgrade number").click()
        self.driver(label=u"btn back nomal").click()
        sleep(1)
        self.driver(label=u"Extend number").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Extend Number").exists)
        self.driver(label="btn back nomal").click()

    def test_08(self):
        '''
            侧边栏-号码设置:Rename/
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()

        self.driver(label=u"Rename").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Number Name").exists)
        self.assertEqual(self.driver(className="TextField").text, 'US')
        self.assertTrue(self.driver(label=u"Cancel").exists)
        self.assertTrue(self.driver(label=u"   Save").exists)
        self.driver(label=u"   Save").click()
        self.driver(label=u"Rename").click()
        self.driver(label=u"Cancel").click()

    def test_09(self):
        '''
            侧边栏-号码设置:Greetings
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()
        self.driver(label=u"Greetings").click()

        self.assertTrue(self.driver(label=u"GREETING").exists)
        self.assertTrue(self.driver(label=u"Greeting").exists)
        self.assertTrue(self.driver(type="Switch").exists)
        # self.assertTrue(self.driver(label=u"Empty list").exists)
        self.assertTrue(self.driver(name=u"ic_greet_recording").exists)
        self.assertTrue(self.driver(label=u"Tap and hold to record.").exists)
        self.assertTrue(self.driver(label=u"Save").exists)
        self.assertTrue(self.driver(label=u"Cancel").exists)

    def test_10(self):
        '''
            Greeting 录音
        :return:
        '''

        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()
        self.driver(label=u"Greetings").click()
        check = threading.Thread(target=self.driver(name=u"ic_greet_recording").wait,args=(20,))
        check.start()
        self.driver(name=u"ic_greet_recording").tap_hold(10)
        sleep(1)
        self.assertTrue(self.driver(label=u"Button").exists)
        self.assertTrue(self.driver(labelContains=u"Audio").exists)
        sec = self.driver(labelContains=u"Audio").text.split('(')[1][:-1]
        self.assertTrue(':' in sec)
        self.assertTrue(self.driver(label=u"contact normal").exists)
        self.driver(label=u"contact normal").click()
        if self.driver(type="Switch").text=='1':
            self.driver(type="Switch").click()
        self.driver(type="Switch").click()
        sleep(1)
        self.assertTrue(self.driver(type="Switch").text=='1')
        self.driver(label=u"Save").click()
        sleep(1)
        self.assertTrue(self.driver(label="Uploading Audio file").exists)
        self.driver(label="Uploading Audio file").wait_gone(timeout=60)
        sleep(2)
        self.driver(label=u"Greetings").click()
        self.assertTrue(self.driver(type="Switch").text=='1')
        pfm.SwipeElement(self.driver,self.driver(type="Cell"),'left',timeout=3) #左划元素
        self.driver(label="DELETE").click()
        self.driver(type="Switch").click()
        self.driver(label=u"Save").click()
        sleep(4)
        self.driver(label=u"Greetings").click()
        self.assertTrue(self.driver(type="Switch").text=='0')



    def test_11(self):

        '''
            侧边栏-号码设置:Notes
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
           self.driver(xpath="//Cell[2]/Button").click()
        else:
           self.driver(xpath="//Cell[1]/Button").click()

        self.driver(label="Notes").click()
        self.assertTrue(self.driver(label=u"Memo").exists)
        self.assertTrue(self.driver(label=u"Done").exists)
        self.assertTrue(self.driver(className="Keyboard").exists)

        self.driver(className="TextView").clear_text()
        self.driver(className="TextView").set_text('This number is used for testing')
        self.driver(label=u"Done").click()
        self.driver(label=u"btn back nomal").click()
        self.driver(label="Notes").click()

        self.assertEqual(self.driver(className="TextView").text, 'This number is used for testing')
        self.driver(className="TextView").clear_text()
        self.driver(label=u"Done").click()
        self.driver(label=u"btn back nomal").click()


    def test_12(self):
        '''
            侧边栏-号码设置:Recordings
        '''
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()

        self.driver(label="Recordings").click()
        self.assertTrue(self.driver(label=u"Recording").exists)
        if self.driver(type="Cell").exists:
            while self.driver(type="Cell").exists:
                pfm.SwipeElement(self.driver,self.driver(type="Cell"),'left',timeout=2)
                self.driver(label="Delete").click()
                sleep(1)
        self.driver(label=u"btn back nomal").click()
        self.driver(label=u"btn back nomal").click() #退回到主界面

        self.driver(label="Keypad").click()
        sleep(2)
        if not self.driver(label=u"btn recording hd normal").exists:
            return
        if self.driver(label=u"HD Recording: On").exists:
            self.driver(label=u"btn recording hd normal").click()

        self.driver(label=u"btn recording hd normal").click()
        self.driver(label='OK').click()
        self.driver(label=u"HD Recording: On").wait(timeout=10.0)
        Phonenumber = '8008002775'
        for i in Phonenumber:
            self.driver(label=i, name=i, className="Button").click()

        self.assertTrue(self.driver(label=u"(800) 800-2775").exists)
        self.driver(label=u"btn answer nomal").click()
        self.driver(label=u"calling...").wait(timeout=10.0)
        self.driver(label=u"calling...").wait_gone(timeout=10.0)
        sleep(10)  # 延迟,增加通话时间
        self.driver(label=u"btn hangup nomal").click()
        self.driver(label=u"btn answer nomal").wait(timeout=10)
        sleep(2)
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()
        self.driver(label="Recordings").click()
        sleep(2)
        currentDate = time.strftime('%m/%d/%Y',time.localtime(time.time()))
        self.assertTrue(self.driver(label=currentDate).exists)
        self.assertTrue(self.driver(label=u"+1 800-800-2775").exists)
        self.assertTrue(self.driver(label=u"btn play normal").exists)

        sec = self.driver(xpath="//Cell[1]/StaticText[2]").text[:-1]
        recordTime = self.driver(xpath="//Cell[1]/StaticText[3]").text

        self.assertTrue(sec.isdigit())

        self.assertTrue(time.strftime('%Y/%m/%d',time.localtime(time.time())) in recordTime)
        self.driver(label=u"btn play normal").click()
        self.driver(label=u"btn stop normal").click()
        while self.driver(type="Cell").exists:
            pfm.SwipeElement(self.driver, self.driver(type="Cell"), 'left', timeout=2)
            self.driver(label="Delete").click()
            sleep(1)
        self.driver(label=u"btn back nomal").click()


    def test_13(self):
        '''
            侧边栏-号码设置:Blocked
        '''

        sleep(2)
        self.driver(label=u"Contacts", name=u"Contacts", type="Button").click()
        sleep(2)
        self.driver(label="Ca").click()
        ctc_number =self.driver(xpath="//Cell[1]/StaticText[2]").text

        if self.driver(label=u"Block This Number").exists:
            self.driver(label=u"Block This Number").click()
            self.driver(label=u"Sure").click()
        else:
            self.driver(label=u"UnBlock This Number").click()
            self.driver(label=u"Sure").click()
            self.driver(label=u"Block This Number").click()
            self.driver(label=u"Sure").click()

        self.driver(label=u"btn back nomal").click()
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        if self.driver(xpath="//Cell[2]/StaticText[2]").text == '+1 520-214-1991':
            self.driver(xpath="//Cell[2]/Button").click()
        else:
            self.driver(xpath="//Cell[1]/Button").click()
        self.driver(label="Blocked").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Blocked Numbers").exists)
        self.assertTrue(self.driver(label=ctc_number).exists)
        self.driver(label=ctc_number).click()
        sleep(1)
        self.assertTrue(self.driver(label=u"You can reveive calls and messages from this number if you unblock it.", name=u"You can reveive calls and messages from this number if you unblock it.", type="StaticText").exists)

        self.driver(label=u"Unblock").click()
        sleep(5)
        self.assertTrue(not self.driver(label=ctc_number).exists)
        self.assertTrue(self.driver(label="No Record!").exists)
        self.driver(label=u"btn back nomal").click()





