# BOT2WEB-Remastered
Remastered Edition of BOT2WEB with Antispam Bypass Techniques

Remastered Edition Requires at least three telegram accounts. If you don't have three accounts, use [BOT2WEB](https://github.com/Junaid433/BOT2WEB)

## Requirements:

Atleast three telegram accounts

Python3.11

## Configuration:

Install the dependencides > pip install -r requirements.txt

You need to collect all three accounts API_ID and API_HASH values from [Telegram](https://my.telegram.org)

Head to /api/client.py, edit Client object values with three seperate API_ID and API_HASH. Remember Which Phone numbers belongs to which API_ID and API_HASH, note them.

Run first_run.py it will launch three seperate terminals. Terminals will have different titles. You need to login with the same phone number you used in Client1 object in terminal with c1 title. Same goes for c2 and c3

## Usage

> python3.11 main.py

> head to localhost:5000 on browser and use the checker

## Limitations:

The BOT2WEB Remastered Edition comes with [Raven](https://t.me/SDBB_Bot) but the onwer has now put limitation of checking 20 cards per hour for non subscribers

## Bugs:

If the app crashed once you may need to restart it again to stop it from crashing

Sometimes cards aren't found and the checker throws error

## Development:

### Adding more accounts:

Add client objects in /api/client.py. For example:

```
client4 = Client(
api_id = 4444
api_hash = 'ww44'
)
```

### Add a class:

Import client4 object
Open cc_class.py and copy whole client1 class. Create new class named cc_methods_c4

```
from .client import client4
class cc_methods_c4:
    def __init__(self):
        self.client = client4
        self.loop = asyncio.get_event_loop()
 ...rest of the code
```
add the newly added class and client object in __init__.py

### Configuration of gates to rotate the accounts:

Lets take /api/auth.py for example:

```
from .cc_class import cc_methods_c1, cc_methods_c2, cc_methods_c3, cc_methods_c4
instance1 = cc_methods_c1()
instance2 = cc_methods_c2()
instance3 = cc_methods_c3()
instance4 = cc_methods_c4()
instance3 = cc_methods_c3()
loop = instance1.loop
loop2 = instance2.loop
loop3 = instance3.loop
loop4 = instance4.loop

last = 1

...more code...

if last ==  1:
  msg = loop.run_until_complete(instance1.send_message(chat_id, text))
  last = 2
  result = loop.run_until_complete(instance1.find_result_by_msg_id(msg.chat.id, msg.id))
elif last == 2:
  msg = loop2.run_until_complete(instance2.send_message(chat_id, text))
  last = 3
  result = loop2.run_until_complete(instance2.find_result_by_msg_id(msg.chat.id, msg.id))
elif last == 3:
  msg = loop3.run_until_complete(instance3.send_message(chat_id, text))
  last = 4
  result = loop3.run_until_complete(instance3.find_result_by_msg_id(msg.chat.id, msg.id))
elif last == 4:
  msg = loop3.run_until_complete(instance3.send_message(chat_id, text))
  last = 1
  result = loop3.run_until_complete(instance3.find_result_by_msg_id(msg.chat.id, msg.id))

```

# Adding new bots:

make a new file. Follow these example codes:

```
from flask import Blueprint, request
from .cc_class import cc_methods_c1, cc_methods_c2, cc_methods_c3
from .regex import *
import re
import time

instance1 = cc_methods_c1()
instance2 = cc_methods_c2()
instance3 = cc_methods_c3()
loop = instance1.loop
loop2 = instance2.loop
loop3 = instance3.loop
xd_bp = Blueprint('xd_bp', __name__)
last = 1

@xd_bp.route('/xd')
def chk_route():
    rt = 0
    while rt < 3:
        try:
            global last
            start = time.time()
            cc = request.args.get('cc')
            chat_id = 'spamx_bot'
            text = '/cc ' + str(cc)
            if last ==  1:
                msg = loop.run_until_complete(instance1.send_message(chat_id, text))
                last = 2
                result = loop.run_until_complete(instance1.find_result_by_msg_id(msg.chat.id, msg.id))
            elif last == 2:
                msg = loop2.run_until_complete(instance2.send_message(chat_id, text))
                last = 3
                result = loop2.run_until_complete(instance2.find_result_by_msg_id(msg.chat.id, msg.id))
            elif last == 3:
                msg = loop3.run_until_complete(instance3.send_message(chat_id, text))
                last = 1
                result = loop3.run_until_complete(instance3.find_result_by_msg_id(msg.chat.id, msg.id))
            if not result:
                if rt < 3:
                    rt += 1
                    continue
                else:
                    return 'No Result found'
            if 'ANTI_SPAM' in result:
                time.sleep(int(result))
                rt += 1
                continue
            match = re.search(glbl_regex, result)
            stop = time.time()
            total = str(stop - start)
            if match:
                otuput = f'<br>CC: {cc}<br>Result: {match.group(1)}<br>Gate: spamx BT Auth<br>Retries: {rt}<br>Time: {total}'
            elif not match:
                otuput = f'<br>CC: {cc}<br>Result: {result}<br>Gate: spamx BT Auth<br>Retries: {rt}<br>Time: {total}<br>'
            return otuput
        except Exception as e:
            if rt == 3:
                return 'Exception Catched: ' + str(e)
            else:
                rt += 1
                continue
```

chat_id is the bot's user name. and text is the command with the card which will be sent by bot


## Support:
[Telegram](https://t.me/fakehecker)
[Facebook](https://facebook.com/jnaid.rahman.im)
[Github](https://github.com/Junaid433/BOT2WEB-Remastered/issues)

## Donation:
BTC: `35s7bwSiLocbs2wYg7HdsHihNbRSgq4DFi`

LTC: `MM8f9Gz3LCMAgavxuuoUtNWRDazsKmycKu`

USDT [TRC20] : `TDW1piifbkZe2c3nTDTZHKuJe2LU1NgzQV`

TRX: `TChp9kpxSxFuMsytLzhj4FtG74Ad8ggNy3`







