#-*- coding:utf-8 -*-

__author__ = 'Wu jiajia'
__date__ = '2017-08-22'

import unittest

import atx
from atx.ext.report import Report
from time import sleep
from Profile import profilemethod as pfm
from Profile import config
from Profile import CloudApi
import requests
import json

class TwoCallTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coins = 0 #金币数量
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
            2Call-UI
        '''

        sleep(2)
        # self.driver(label = u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label=u"+1 520-214-1991").click()

        phone_name = self.driver(xpath="//Cell[1]/StaticText[1]").text
        phone_number = self.driver(xpath="//Cell[1]/StaticText[2]").text
        mins = self.driver(xpath="//Cell[1]/StaticText[3]").text
        messages = self.driver(xpath="//Cell[1]/StaticText[4]").text
        days = self.driver(xpath="//Cell[1]/StaticText[5]").text
        self.driver(xpath="//Cell[1]").click()
        # self.driver(label=u"btn whitesidebar nomal").click()
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.driver(label="2Call").click()
        sleep(2)
        # self.assertTrue(self.driver(label=u"btn whitesidebar nomal").exists)
        if self.driver(label=u"btn dotsidebar nomal").exists:
            self.driver(label=u"btn dotsidebar nomal").click()
        elif self.driver(label=u"btn whitesidebar nomal").exists:
            self.driver(label=u"btn whitesidebar nomal").click()
        self.assertTrue(self.driver(label=u"2Call").exists)

        self.assertEqual(self.driver(type="StaticText")[2].text,phone_name)
        self.assertEqual(self.driver(type="StaticText")[3].text,phone_number)
        self.assertEqual(self.driver(type="StaticText")[4].text,mins)
        self.assertEqual(self.driver(type="StaticText")[5].text,days)
        self.assertEqual(self.driver(type="StaticText")[6].text,messages)

        self.assertTrue(self.driver(label=u"HISTORY").exists)
        self.assertTrue(self.driver(name=u"ic_more_recording").exists)
        self.assertTrue(self.driver(label=u"Recordings").exists)
        self.assertEqual(self.driver(label=u"2Call Info").count(),4)
        self.assertTrue(self.driver(name=u"ic_block").exists)
        self.assertTrue(self.driver(label=u"Blocked numbers").exists)
        self.assertTrue(self.driver(name=u"ic_look up").exists)
        self.assertTrue(self.driver(label=u"Look up numbers").exists)
        self.assertTrue(self.driver(label=u"TOOL").exists)
        self.assertTrue(self.driver(name=u"ic_yellow pages").exists)
        self.assertTrue(self.driver(label=u"Yellow Pages").exists)


    def test_02(self):
        '''
            2Call-Recordings/Blocked numbers
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Recordings").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Recording").exists)
        self.driver(label=u"btn back nomal").click()
        self.driver(label=u"Blocked numbers").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Blocked Numbers").exists)
        self.driver(label=u"btn back nomal").click()



    def test_03(self):
        '''
            2Call - Lookup-UI
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Look up numbers").click()
        self.assertTrue(self.driver(label=u"Phone Lookup").exists)
        self.assertTrue(self.driver(label=u"Type a phone number:").exists)
        self.assertTrue(self.driver(label=u"btn history normal").exists)
        self.assertTrue(self.driver(label=u"Button").exists)
        self.assertEqual(self.driver(type="TextField").text,'+1')
        for i in range(10):
            self.assertTrue(self.driver(label=u"%s"%i).exists)
        self.assertTrue(self.driver(label=u"*").exists)
        self.assertTrue(self.driver(label=u"#").exists)
        self.assertTrue(self.driver(label=u"LOOK UP").exists)

    def test_04(self):
        '''
            号码查询
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Look up numbers").click()
        phonenumber = '5202141993'
        for i in phonenumber:
            self.driver(label=i, name=i, className="Button").click()
        self.driver(label=u"LOOK UP").click()
        sleep(5)
        self.assertTrue(self.driver(label=u"+1 520-214-1993").exists)
        self.assertTrue(self.driver(label=u"Unlock all details with a Premium Search").exists)
        self.driver(label=u"btn back nomal").click()
        self.driver(label=u"btn history normal").click()
        self.assertTrue(self.driver(label = u"New Lookup").exists)
        self.assertTrue(self.driver(label=u"Phone Lookup").exists)
        self.driver(label=u"btn back nomal").click()

    def test_05(self):
        '''
            2call-contact: yellow page - ui
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Yellow Pages").click()
        sleep(2)
        self.assertTrue(self.driver(label=u"Restaurants").exists)
        self.assertTrue(self.driver(label=u"Pizza").exists)
        self.assertTrue(self.driver(label=u"Hotels").exists)
        self.assertTrue(self.driver(label=u"Banks").exists)
        self.assertTrue(self.driver(label=u"Doctors").exists)
        self.assertTrue(self.driver(label=u"Dentists").exists)
        self.assertTrue(self.driver(label=u"Department").exists)
        self.assertTrue(self.driver(label=u"Hardware").exists)
        self.assertTrue(self.driver(label=u"Taxi Cabs").exists)
        self.assertTrue(self.driver(label=u"Pharmacies").exists)
        self.assertTrue(self.driver(label=u"Gas Stations").exists)
        self.assertTrue(self.driver(label=u"table index").exists)
        self.assertTrue(self.driver(label=u"ic location normal").exists)
        self.driver(label=u"btn back nomal").click()

    def test_06(self):
        '''
            more - yellow page:定位功能
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Yellow Pages").click()
        sleep(2)
        self.driver(label=u"ic location normal").click()

        self.driver(label=u"btn back nomal").exists
        self.assertTrue(self.driver(label=u"Choose City").exists)
        self.assertTrue(self.driver(label=u"Current Location").exists)
        self.assertTrue(self.driver(label=u"Minhang, Shanghai").exists)
        self.driver(label=u"Minhang, Shanghai").click()
        self.driver(label=u"Restaurants").click()
        self.driver.wait('pic/noresults.2208x1242.png', timeout=15.0)
        self.driver(label=u"ic location normal").click()
        self.driver(label=u"Adelaide, SA, AU").click()
        sleep(3)
        self.driver(label=u"Restaurants").click()
        self.driver(label=u"Location").wait(timeout=20.0)

        # self.assertTrue(self.driver(label=u"A-Z").eixsts)
        self.driver(label=u"btn back nomal").click()
        self.driver(label=u"ic location normal").click()
        sleep(2)
        # self.assertTrue(self.driver(xpath="//StaticText[@label='Adelaide, SA, AU']").exists)
        self.assertTrue(self.driver(label='Adelaide, SA, AU').exists)
        self.assertTrue(self.driver(label=u"table index").exists)
        # 搜索城市
        self.driver(label=u"Enter city name").set_text("Abilene")
        self.driver(label=u"Search").click()
        sleep(2)
        self.assertTrue(self.driver(label="Abilene, TX").exists)
        self.driver(label="Abilene, TX").click()
        sleep(2)

    def test_07(self):
        '''
            2call-contact:yellow page-搜索附近列表结果
        '''
        sleep(2)
        self.driver(label="2Call").click()
        self.driver(label=u"Yellow Pages").click()
        sleep(2)
        self.driver(label=u"ic location normal").click()
        self.driver(label=u"Adelaide, SA, AU").click()
        self.driver(label=u"Restaurants").click()
        self.driver(label=u"Location").wait(timeout=20.0)

        self.assertTrue(self.driver(label=u"A-Z").exists)
        self.assertTrue(self.driver(label=u"Rating").exists)

        # 获取附近Restaurants接口返回数据
        URL = "https://fews.avantar.us/listings.php?device=iPhone&what=Restaurants&administrative_area_code=SA&uid=6c698a647c4147f5aed8f64cac536ae2&app_version=7.11.1&featured=12&longitude=138.599884&latitude=-34.926102&type=yp&os=iOS&sdk=10.2&app=yellowpages&where=Adelaide,%20SA%2005000&deviceid=F8B40545-5471-476B-BA95-5AD32FC31622&postal_code=05000&nav=0&page=Custom&locality=Adelaide&country_code=AU"
        RES = requests.get(URL)
        DATA = json.loads(RES.content)

        total = DATA["results"]["organic"]["total"]  # 获取商店数量
        business_name = DATA["results"]["organic"]["listings"][0]["details"]["business_name"]
        address1 = DATA["results"]["organic"]["listings"][0]["placemark"]["address_1"]
        address2 = DATA["results"]["organic"]["listings"][0]["placemark"]["address_2"]
        phone = DATA["results"]["organic"]["listings"][0]["details"]["phone"]
        distance = DATA["results"]["organic"]["listings"][0]["placemark"]["distance"]
        rating = DATA["results"]["organic"]["listings"][0]["details"]["rating"]

        self.assertEqual(self.driver(className="Cell").count(), total)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[1]").text, business_name)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[2]").text, address1 + ' ' + address2)
        self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[3]").text, distance)
        if rating == "null":
            self.assertEqual(self.driver(xpath="//Cell[1]/StaticText[4]").text, 'No rating')

        self.driver(xpath="//Cell[1]").click()
        self.assertTrue(self.driver(label='Restaurants').exists)
        self.assertEqual(self.driver(className="StaticText")[2].text, 'Name: ' + business_name)
        self.assertEqual(self.driver(className="StaticText")[3].text, 'Address: : ' + address1 + ' ' + address2)
        phonenumber = '(' + phone[:3] + ')' + phone[3:6] + '-' + phone[6:10]
        self.assertEqual(self.driver(className="StaticText")[4].text, 'Phone: ' + phonenumber)
        if rating == "null":
            self.assertEqual(self.driver(className="StaticText")[5].text, 'Grade: ' + 'No rating')
        self.assertEqual(self.driver(className="StaticText")[6].text, 'Distance: ' + distance)
        self.assertEqual(self.driver(className="Button")[3].text, phonenumber)
        self.assertTrue(self.driver(label=u"Map pin").exists)

        self.driver(className="Button")[3].click()
        sleep(2)
        self.assertTrue(self.driver(label=phonenumber).exists)
        self.driver(label="Cancel").click()
        self.driver(label=u"btn back nomal").click()

        # a~z
        self.driver(label=u"A-Z").click()
        words = []
        for word in range(5):
            words.append(self.driver(xpath="//Cell[%d]/StaticText[1]" % (word + 1)).text)
        self.assertTrue(words == sorted(words))
        self.driver(label=u"btn back nomal").click()

    @unittest.skip('test_011:待完善')
    def test_08(self):
        '''
            2Call - Recording :待完善
        '''
        self.driver(label="2Call").click()
        if not self.driver(label=u"US +1 520-214-1991").exists:
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
        self.driver(label=u"Recording").click()

        self.assertTrue(self.driver(label = u"Recording").exists)
        self.driver(label=u"btn back nomal").click()











