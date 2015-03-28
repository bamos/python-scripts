#!/usr/bin/env python3

__author__ = ['[Brandon Amos](https://github.com/bamos)']
__date__ = '2014.02.06'

"""
Script to be run by crontab to report broken links.

Builds upon linkchecker (Ubuntu: sudo apt-get install linkchecker)
to hide warnings and to send a concise email if bad links are found.

![Link checker screenshot](https://raw.githubusercontent.com/bamos/python-scripts/master/link-checker-screenshot.png?raw=true)
"""

from subprocess import Popen, PIPE

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Settings to send emails with SMTP with gmail.
server = "smtp.gmail.com"
port = 587
user = ENTER_USER
pw = ENTER_PW  # Please use an application-specific password for security!
email_to = ENTER_TO_EMAIL
email_from = ENTER_FROM_EMAIL
root_url = ENTER_URL

cmd = ["linkchecker", "--no-warnings", "--no-status", root_url]
output = Popen(cmd, stdout=PIPE).communicate()[0].decode("UTF-8")

bad_urls = []
for line in output.splitlines():
    if line.startswith("URL"):
        current_url = line
    if line.startswith("Parent URL"):
        parent_url = line
    elif line.startswith("Result"):
        current_result = line
        toks = line.split()
        if toks[1] != "Valid:":
            bad_urls.append((current_url, parent_url, current_result))

if bad_urls:
    message_contents = "Error checking links for " + root_url + "\n\n"
    for url in bad_urls:
        message_contents += "\n".join(url) + "\n\n"

    server = smtplib.SMTP(server, port)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.login(user, pw)

    multi_msg = MIMEMultipart()
    multi_msg['From'] = email_to
    multi_msg['To'] = email_from
    multi_msg['Subject'] = "Bad links on " + root_url + "."
    multi_msg.attach(MIMEText(message_contents))
    server.sendmail(email_to, email_from, multi_msg.as_string())

    server.close()
