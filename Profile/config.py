#-*- coding:utf-8 -*-

import os
import time

DAY = time.strftime('%Y-%m-%d')

PACKAGE_NAME= 'com.jinming.call'
CASE_REPORT_PATH = os.getcwd() + '/result/' + DAY +os.sep + 'case_report'+os.sep

CURRENT_DAY = time.strftime('%d',time.localtime(time.time()-86400))
CURRENT_YEAR = time.localtime().tm_year

Purchase_Account = "jinmingtext1998@sina.com"

Purchase_Password = "Qazwsx12@"

PRICE_LIST_PURCHASEINFO = {
    "Get 7 days for $3.99":"Pay ¥27.00 for this 7‑day subscription starting %s November %s.\n\n[Environment: Sandbox]"%(CURRENT_DAY,CURRENT_YEAR),
    "Get 1 month for $9.99":"Pay ¥68.00 for this 1‑month subscription starting %s November %s.\n\n[Environment: Sandbox]"%(CURRENT_DAY,CURRENT_YEAR),
    "Get 12 months for $1.99/Month":"Pay ¥173.00 for this 1‑year subscription starting %s November %s.\n\n[Environment: Sandbox]"%(CURRENT_DAY,CURRENT_YEAR),
    "Get 12 months for $4.99/Month":"Pay ¥408.00 for this 1‑year subscription starting %s November %s.\n\n[Environment: Sandbox]"%(CURRENT_DAY,CURRENT_YEAR),
}


# print PRICE_LIST_PURCHASEINFO['Get 7 days for $3.99']
