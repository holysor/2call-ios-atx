
import requests
import json

__author__= "wujiajia"
__data__ = "2017/09/25"

"""
    Get 2016 2Call cloud parameter.
"""


headers ={
    "Host":"api.zcloud.io",
    "User-Agent": "MaskedPhone2016/243 CFNetwork/887 Darwin/17.0.0",
    "Content-Type": "application/json",
    "X-ZCloud-Hash": "eecc05cc2fc31f1dbc8c035ea51732cc5579714597759f802fed844ed42a1046",
    "X-ZCloud-AppId": "f015c0e0ec3811e6903022000a260de5",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-us",
}

url = "http://api.zcloud.io/1.0/cparams?locale=en_CN&devId=oa0de15fdca68cf325d5188c342f6e686599f30cb&appId=f015c0e0ec3811e6903022000a260de5&version=3.4"

res = requests.get(url,headers=headers)

CLOUD_PARAMETER_SWITCH_CONTROL = json.loads(res.content)
# print CLOUD_PARAMETER_SWITCH_CONTROL