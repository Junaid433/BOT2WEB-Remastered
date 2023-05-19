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
vbv_bp = Blueprint('vbv_bp', __name__)
last = 1

@vbv_bp.route('/vbv')
def vbv_route():
    rt = 0
    while rt < 3:
        try:
            global last
            start = time.time()
            cc = request.args.get('cc')
            chat_id = 'SDBB_Bot'
            text = '/vbv ' + str(cc)
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
            match = re.search(raven_chk_regex, result)
            stop = time.time()
            total = str(stop - start)
            if match:
                otuput = f'<br>CC: {cc}<br>Result: {match.group(1)}<br>Gate: Raven VBV<br>Retries: {rt}<br>Time: {total}'
            elif not match:
                otuput = f'<br>CC: {cc}<br>Result: {result}<br>Gate: Raven VBV<br>Retries: {rt}<br>Time: {total}<br>'
            return otuput
        except Exception as e:
            if rt == 3:
                return 'Exception Catched: ' + str(e)
            else:
                rt += 1
                continue