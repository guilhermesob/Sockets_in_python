#!/usr/bin/env python3

import poplib

mailbox = poplib.POP3_SSL("pop.gmail.com", 995)
mailbox.user("pyyanev")
mailbox.pass_("")

print(mailbox.getwelcome())

message = len(mailbox.list()[1])

for index in range(message):
    for message in mailbox.retr(index+1)[1]:
        print(message)

mailbox.quit()