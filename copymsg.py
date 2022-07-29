from telethon import TelegramClient, events
from binance.client import Client
from ticker_rules import rules
import time

Pkey = 'kmovXgZCvCBBtpClUTIfPzpyRHxHdoRUlygKeydYVB3v66N4SOB2qVggk5LXJ9Gz'
Skey = 'OQu6WNZkaYP2IbYlGKDJWoOOKyCCCLVxw9Dnqk0oCQzVzH0qeafUZ8U2Zc4dDnNc'
api_id = '3686067'
api_hash = '98d331dfb25569d1e362a95f63f40c44'
client = TelegramClient('reda', api_id, api_hash)

@client.on(events.NewMessage)
async def handlmsg(event):
    # try:
        chat_id = event.chat_id
        msg = event.raw_text
        msg1 = msg.upper()
        res = msg.split()
        chat = 5102702091

        # if chat_id == -1001260725140:
        if chat_id == -1001516609917:
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
                balance1 = round(balance, rules[symbol][0])
                balance1 = float(balance1) - balance
                balance = balance - balance1
                balance = round(balance, rules[symbol][0])
                if balance >= rules[symbol][4]:
                    avg_price = client1.get_avg_price(symbol = symbol)
                    avg_price = float(avg_price["price"])
                    if avg_price <= float(target1):
                        await client.send_message(chat, "/buy")
                        time.sleep(2)
                        await client.send_message(chat, coin)
                        time.sleep(2)
                        await client.send_message(chat, "USDT")
                        time.sleep(2)
                        await client.send_message(chat, str(balance))
                        time.sleep(2)
                        await client.send_message(chat, "yes")
                        balance = client1.get_asset_balance(asset = coin)
                        balance = float(balance["free"])
                        balance1 = round(balance, rules[symbol][0])
                        balance1 = float(balance1) - balance
                        balance = balance - balance1
                        balance = round(balance, rules[symbol][0])
                        if balance > 0:
                            time.sleep(2)
                            await client.send_message(chat, "/sale_limit_stop_lose")
                            time.sleep(2)
                            await client.send_message(chat, coin)
                            time.sleep(2)
                            await client.send_message(chat, "USDT")
                            time.sleep(2)
                            await client.send_message(chat, str(balance))
                            time.sleep(2)
                            await client.send_message(chat, str(target1))
                            time.sleep(2)
                            await client.send_message(chat, str(stop))
                            time.sleep(2)
                            await client.send_message(chat, "yes")
    # except:
    #     pass

client.start()
client.run_until_disconnected()