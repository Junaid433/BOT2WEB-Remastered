from .client import client1, client2, client3
import asyncio

class cc_methods_c1:
    def __init__(self):
        self.client = client1
        self.loop = asyncio.get_event_loop()

    def name(self):
        return 'instance1'
        
    async def send_message(self, chat_id, text):
        await self.client.start()
        data = await self.client.send_message(chat_id, text)
        await asyncio.sleep(1)
        await self.client.stop()
        return data

    async def find_result_by_card(self, chat_id, card, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(5)
            history = self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if card in message.text:
                    await self.client.stop()
                    return message

    async def find_result_by_msg_id(self, chat_id, msg_id, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(1)
            history = self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if str(message.reply_to_message_id) == str(msg_id):
                    while True:
                        mx = await self.client.get_messages(chat_id=chat_id, message_ids=message.id)
                        if 'Please wait...' in mx.text or 'Waiting for result...' in mx.text or 'Checking your card...' in mx.text or 'Checking...' in mx.text or 'Mass Checking...' in mx.text:
                            await asyncio.sleep(5)
                            continue
                        else:
                            await self.client.stop()
                            return str(mx.text)
                        
class cc_methods_c2:
    def __init__(self):
        self.client = client2
        self.loop = asyncio.get_event_loop()

    def name(self):
        return 'instance2'

    async def send_message(self, chat_id, text):
        await self.client.start()
        data = await self.client.send_message(chat_id, text)
        await asyncio.sleep(1)
        await self.client.stop()
        return data

    async def find_result_by_card(self, chat_id, card, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(5)
            history = self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if message.text and str(card) in str(message.text):
                    await self.client.stop()
                    return message

    async def find_result_by_msg_id(self, chat_id, msg_id, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(1)
            history = self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if str(message.reply_to_message_id) == str(msg_id):
                    while True:
                        mx = await self.client.get_messages(chat_id=chat_id, message_ids=message.id)
                        if 'Please wait...' in mx.text or 'Waiting for result...' in mx.text or 'Checking your card...' in mx.text or 'Checking...' in mx.text:
                            await asyncio.sleep(5)
                            continue
                        else:
                            await self.client.stop()
                            return str(mx.text)

class cc_methods_c3:
    def __init__(self):
        self.client = client3
        self.loop = asyncio.get_event_loop()

    def name(self):
        return 'instance3'
        
    async def send_message(self, chat_id, text):
        await self.client.start()
        data = await self.client.send_message(chat_id, text)
        await asyncio.sleep(1)
        await self.client.stop()
        return data

    async def find_result_by_card(self, chat_id, card, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(5)
            history = await self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if message.text and str(card) in str(message.text):
                    await self.client.stop()
                    return message

    async def find_result_by_msg_id(self, chat_id, msg_id, retry = 1):
        await self.client.start()
        for i in range(retry):
            await asyncio.sleep(1)
            history = self.client.get_chat_history(chat_id, limit=10)
            async for message in history:
                if str(message.reply_to_message_id) == str(msg_id):
                    while True:
                        mx = await self.client.get_messages(chat_id=chat_id, message_ids=message.id)
                        if 'Please wait...' in mx.text or 'Waiting for result...' in mx.text or 'Checking your card...' in mx.text or 'Checking...' in mx.text:
                            await asyncio.sleep(5)
                            continue
                        else:
                            await self.client.stop()
                            return str(mx.text)