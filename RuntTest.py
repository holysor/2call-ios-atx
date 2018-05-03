#-*- coding:utf-8 -*-
import unittest
import os
import time

from Profile import HTMLTestReport

from TestCase import TestForReportTestCase


def all_case():
    testcase = unittest.TestSuite()
    casepath = os.getcwd()+os.sep+'TestCase'
    if os.path.exists(casepath):
        discover = unittest.defaultTestLoader.discover(casepath, pattern='*TestCase.py', top_level_dir=None)
    else:
        raise OSError,'目录不存在:'+casepath

    for testsuite in discover:
        for case in testsuite:
            testcase.addTest(case)

    print "测试用例数:",testcase.countTestCases(),'条'
    return testcase

def outPutWithHTML(testcase):
    import shutil
    now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    print '开始时间:',now
    day = time.strftime('%Y-%m-%d')
    file_is_exist = os.path.exists('./result/' + day)
    if not os.path.exists('./result'):
        os.mkdir('./result')
    if file_is_exist:
        shutil.rmtree('./result/' + day)
    os.mkdir('./result/' + day)
    # os.mkdir('./result/' + day + '/screencap')
    filename = './result/' + day + '/result.html'
    runner = HTMLTestReport.HTMLTestRunner(title=u'自动化测试报告',
                                           description=u'2Call-2016版本自动化测试',
                                           stream=open(filename,"wb"),verbosity=2,retry=1)
    runner.run(testcase)

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    # testsuite.addTest(TestForReportTestCase.Test('test_fail1'))
    # testsuite.addTest(TestForReportTestCase.Test('test_fail2'))
    # testsuite.addTest(TestForReportTestCase.Test('test_error1'))
    # testsuite.addTest(TestForReportTestCase.Test('test_error2'))
    # testsuite.addTest(TestForReportTestCase.Test('test_pass'))


    outPutWithHTML(all_case())

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(all_case())