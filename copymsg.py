from telethon import TelegramClient, events
from binance.client import Client
from ticker_rules import rules


Pkey = 'kmovXgZCvCBBtpClUTIfPzpyRHxHdoRUlygKeydYVB3v66N4SOB2qVggk5LXJ9Gz'
Skey = 'OQu6WNZkaYP2IbYlGKDJWoOOKyCCCLVxw9Dnqk0oCQzVzH0qeafUZ8U2Zc4dDnNc'
api_id = '3686067'
api_hash = '98d331dfb25569d1e362a95f63f40c44'
client2 = TelegramClient('reda', api_id, api_hash)

@client2.on(events.NewMessage)
async def handlmsg(event):
    try:
        chat_id = event.chat_id
        msg = event.raw_text
        msg1 = msg.upper()
        res = msg.split()

        if chat_id == -1001260725140:
            print("Start")
            if 'TARGETS' in msg1 and '⛔️' in msg and 'BUY' in msg1:
                a = 0
                coin = res[1]
                coin = coin.split("/", 1)
                coin = coin[0]
                target1 = 0
                for (index, item) in enumerate(res):
                    if item == "1️⃣":
                        a = index
                target1 = res[a+1]
                for (index, item) in enumerate(res):
                    if item == "LOSS":
                        a = index
                stop = res[a+2]

                symbol = coin+"USDT"
                client1 = Client(api_key=Pkey, api_secret=Skey)
                balance = client1.get_asset_balance(asset = "USDT")
                balance = float(balance["free"])
                balance = str(balance).split(".", 1)
                balance1 = balance[0] + "."
                for i in range(int(rules[symbol][0])):
                    try:
                        balance1 = balance1 + balance[1][i]
                    except:
                        pass
                balance = float(balance1)
                if balance >= rules[symbol][4]:
                    avg_price = client1.get_avg_price(symbol = symbol)
                    avg_price = float(avg_price["price"])
                    avg_price = str(avg_price).split(".", 1)
                    avg_price1 = avg_price[0] + "."
                    for i in range(int(rules[symbol][0])):
                        try:
                            avg_price1 = avg_price1 + avg_price[1][i]
                        except:
                            pass
                    avg_price = float(avg_price1)
                    if avg_price <= float(target1):
                        quantity = float(balance) / avg_price
                        quantity = str(quantity).split(".", 1)
                        quantity1 = quantity[0] + "."
                        for i in range(int(rules[symbol][3])):
                            try:
                                quantity1 = quantity1 + quantity[1][i]
                            except:
                                pass
                        quantity = float(quantity1)
                        client1.order_market_buy(symbol=symbol, quantity=quantity)

                        balance = client1.get_asset_balance(asset = str(coin))
                        balance = float(balance["free"])
                        balance = str(balance).split(".", 1)
                        balance1 = balance[0] + "."
                        for i in range(int(rules[symbol][0])):
                            try:
                                balance1 = balance1 + balance[1][i]
                            except:
                                pass
                        quantity = float(balance1)
                        commission = (float(quantity) / 100)
                        quantity = float(quantity) - commission 
                        quantity = str(quantity).split(".", 1)
                        quantity1 = quantity[0] + "."
                        for i in range(int(rules[symbol][3])):
                            try:
                                quantity1 = quantity1 + quantity[1][i]
                            except:
                                pass
                        quantity = float(quantity1)
                        price1 = float(target1)
                        price1 = str(price1).split(".", 1)
                        price2 = price1[0] + "."
                        for i in range(int(rules[symbol][0])):
                            try:
                                price2 = price2 + price1[1][i]
                            except:
                                pass
                        price1 = float(price2)
                        stop_lose = float(stop)
                        stop_lose = str(stop_lose).split(".", 1)
                        stop_lose1 = stop_lose[0] + "."
                        for i in range(int(rules[symbol][0])):
                            try:
                                stop_lose1 = stop_lose1 + stop_lose[1][i]
                            except:
                                pass
                        stop_lose = float(stop_lose1)
                        trigger = float(stop_lose) + (float(stop_lose) * 0.001)
                        float_format = "%."+str(rules[symbol][0])+"f"
                        trigger = float_format % trigger
                        client1.create_oco_order(symbol = symbol, side = "SELL", stopLimitTimeInForce = "GTC", quantity = quantity, stopPrice = trigger, stopLimitPrice  = stop_lose, price = price1 )
                        print("Done")














                        # await client2.send_message("AutoCopy_TradeBot", "/buy")
                        # time.sleep(2)
                        # await client2.send_message("AutoCopy_TradeBot", coin)
                        # time.sleep(2)
                        # await client2.send_message("AutoCopy_TradeBot", "USDT")
                        # time.sleep(2)
                        # await client2.send_message("AutoCopy_TradeBot", str(balance))
                        # time.sleep(2)
                        # await client2.send_message("AutoCopy_TradeBot", "yes")
                        # balance = client1.get_asset_balance(asset = coin)
                        # balance = float(balance["free"])
                        # balance1 = round(balance, rules[symbol][0])
                        # balance1 = float(balance1) - balance
                        # balance = balance - balance1
                        # balance = round(balance, rules[symbol][0])
                        # if balance > 0:
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", "/sale_limit_stop_lose")
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", coin)
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", "USDT")
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", str(balance))
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", str(target1))
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", str(stop))
                        #     time.sleep(2)
                        #     await client2.send_message("AutoCopy_TradeBot", "yes")
    except:
        pass

client2.start()
client2.run_until_disconnected()