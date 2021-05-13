import requests
import time
import pyupbit
import datetime

access = "bIQ17TlUSVILX0s5tOowdiAoxSWuJosT1DxYVQNd"          # 본인 값으로 변경
secret = "x31ywPx6LtJueY2yP2ZIcG3ypB9a34erWnPAn7Ow" 
myToken = "xoxb-2018501947909-2045383410448-9u3Jofj9z5Y3xqBs1n8udRek"

url = "https://api.upbit.com/v1/candles/minutes/1"

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]


def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_balance(coin):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

#데이터 개수 ex. n=2면 캔들 2개. 즉, 여기선 1분짜리 2개.
n=3

querystring = {"market":"KRW-EOS","count":n}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

a = response.text
list_a = a.split(",")

#list_a[11*i-9].split("T")[1] 자료 현재시간
list_ = []
for i in range(1, n+1) :
    raw_open_price = list_a[11*i -8]
    open_price = float(raw_open_price.split(":")[1])
    dict_ = {}
    dict_['open'] = open_price


    raw_high_price = list_a[11*i -7]
    high_price = float(raw_high_price.split(":")[1])
    dict_['high'] = high_price

    raw_closed_price = list_a[11*i -5]
    closed_price = float(raw_closed_price.split(":")[1])
    dict_['closed'] = closed_price
    list_.append(dict_)

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#autotrading", "autotrade start")
# try 바로 다음 if 바로 앞에 들어가는 거 -> list_[1]['closed']

balances = upbit.get_balances()
print(balances)
krw = get_balance("KRW")
print(krw)
