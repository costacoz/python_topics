"""
    Example of internet access modules: urllib.request and smtplib
"""

from urllib.request import urlopen

article = 'https://apod.nasa.gov/apod/ap050521.html'

with urlopen(article) as response:
    for line in response:
        line = line.decode('utf-8')
        if 'snake' in line.lower() and not '<' in line:
            print(line)


def send_mail():
    """
        Need to have functional mailserver on localhost to be able to use this
    """
    import smtplib, sys

    server = smtplib.SMTP('localhost')
    server.send('real_email_here@gmail.com', 'real_email_here@gmail.com',
                """To: real_email_here@gmail.com
                From: real_email_here@gmail.com
                
                Hello, this is test.
                """)
    server.quit()


send_mail()
