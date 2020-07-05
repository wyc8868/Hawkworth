import requests
 # token
def test_token():
    #企业ID
    corpid = "wwde0a96e958fb4d5a"
    #应用凭证秘钥
    corpsecret = "gA5inNMF0u-SDTDzu-0LFD-anSeEZLDD9XtWyY_NJ30"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]

# 获取部门列表

def test_getbm():
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}&id=1")
    print(res.json())

# 创建部门

def test_createbm():
    buildData = {
        "name": "测试三部",
        "parentid": 1,
        "order":3,
        "id":3
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",
                        json=data)
    print(res.json())

# 更新部门

def test_updatebm():
    dpdatData = {
        "id": 2,
        "name": "测试总部",
        "parentid":1,
        "order":2
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",json=dpdatData)
    print(res.json())
# 删除部门

def test_deletebm():
    
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2")
    print(res.json())