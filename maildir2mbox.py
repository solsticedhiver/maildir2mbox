#!/usr/bin/python3

import os
import re
import datetime
import sys

email_regex = re.compile(r'^[^<]*<(.+@.+)>')

emails = os.listdir('.')
total = len(emails)
print('Processing', total, 'emails', file=sys.stderr)

count = 0
for email in emails:
    # print progress
    print('{:2}% done\r'.format(int((count/total)*100)), file=sys.stderr, end='')
    count += 1
    # TODO: more sophisticated encoding handling needed here
    # i.e. use chardet2 ? http://pypi.python.org/pypi/chardet2/2.0.1
    try:
        f = open(email, 'r')
        content = f.read()
    except UnicodeDecodeError:
        g = open(email, mode='r', encoding='latin1')
        content = g.read()
        g.close()
    finally:
        f.close()
    # join each split header line into one single line
    content = re.sub(r'\n[\t ]+', ' ', content)
    # quote From_ line (gives a mboxrd output file)
    content = re.sub(r'\n(\>*From )', r'\n>\1', content)
    lines = content.split('\n')

    email_addr, mbox_date = None, None
    for line in lines:
        if line.startswith('From: '):
            try:
                email_addr = re.findall(email_regex, line)[0]
            except IndexError:
                email_addr = re.sub('^From: ', '', line)
        if line.startswith('Date: '):
            date = re.sub('^Date: ', '', line)
            # remove timezone name
            date = re.sub(r' \(.*\)$', '', date)
            try:
                d = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
            except ValueError:
                try:
                    d = datetime.datetime.strptime(date, '%d %b %Y %H:%M:%S %z')
                except ValueError:
                    print("Error: Can't parse date.", email, "has been dropped", file=sys.stderr)
                    continue
            mbox_date = d.strftime('%a %b %e %H:%M:%S %Y')
        if email_addr and mbox_date:
            print('From {}  {}'.format(email_addr, mbox_date))
            # email headers have been changed from original email (joined in one line)
            print(content)
            break
