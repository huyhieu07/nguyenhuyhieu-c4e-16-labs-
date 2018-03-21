from gmail import GMail, Message
import datetime
from random import choice

gmail = GMail('vihoabinhnhanloai@gmail.com','thisishuyhieu')
now = datetime.datetime.now()
# print("Current hour:", now.hour)

menu = ["vì em thích :))","vì hôm nay trời đẹp quá, em nghỉ","vì hôm nay là ngày tận thế","vì hôm nay e bị ẩy chỉa"]
reason = choice(menu)

don_xin_nghi_hoc = '''
<h1>em xin được nghỉ học v&igrave; l&iacute; do:&nbsp; {0}</h1>
'''.format(reason)
msg = Message('Đơn xin nghỉ học',
               to = 'huyhieu070109@gmail.',
               html = don_xin_nghi_hoc)

while now == 7:
    gmail.send(msg)
    break
