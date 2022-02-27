#coding: UTF8
"""
Design Patterns in Python
listing 1 for Chapter 3

"""

from mailer import Mailer
from mailer import Message
import urllib

msg1 = Message(From="translation@ginstrom.com",
                  To="marocsosinfo@gmail.com",
                  charset="utf-8")
msg1.Subject = "Vaccin"
msg1.Html = """Hello, <b>日本語</b>"""

mailer = Mailer('smtp01.odn.ne.jp')

mailer.send(msg1)
