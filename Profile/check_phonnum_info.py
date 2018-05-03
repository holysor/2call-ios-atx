

import requests
import json
_url = "https://api.maxleap.com/2.0/functions/getPhoneInfo"

_data = {
	"email": "315325320@qq.com",
	"type": 1,
	"phoneNumber": "+15209546859",
}

_headers = {
        "Host": "api.maxleap.com",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": "com.jinming.call/237 iOS/10.3.3",
        "X-ML-Session-Token": "9Zh_2jUwdJkHOAXz4DVtE-QBF9CrxhHmjVlWhHr-l5k",
        "X-ML-AppId": "581fe2334c146e0001b37c7a",
}

def result_num_info():

    res = requests.post(_url,headers=_headers,data=json.dumps(_data))

    print res.text

result_num_info()