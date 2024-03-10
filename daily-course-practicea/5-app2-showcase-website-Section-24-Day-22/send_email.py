import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "rak.mdg94@gmail.com"
password = "zxxn xmbx vtnr mcal"

receiver = "rak.mdg94@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: My Email Subject!
Hi! 
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)



def sendemailViaWeb(emailid,message):
    host = "smtp.gmail.com"
    port = 465

    username = emailid
    password = "zxxn xmbx vtnr mcal"

    receiver = "rak.mdg94@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)