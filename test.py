import pyupbit

access = "bIQ17TlUSVILX0s5tOowdiAoxSWuJosT1DxYVQNd"          # 본인 값으로 변경
secret = "x31ywPx6LtJueY2yP2ZIcG3ypB9a34erWnPAn7Ow"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회