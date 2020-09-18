import time
from LIBS.openexchange import OpenExchangeClient

APP_ID = "c5c2881fe25f45d3aab4de7cec781d8f"
client = OpenExchangeClient(APP_ID)
usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(gbp_amount)
print(end-start)


start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(gbp_amount)
print(end-start)


start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(gbp_amount)
print(end-start)


start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(gbp_amount)
print(end-start)

