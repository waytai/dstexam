#########################################################################
#-*- coding:utf-8 -*-
# File Name: mycommand.py
# Author: wayne
# mail: @163.com
# Created Time: 2015年09月10日 星期四 11时03分38秒
#########################################################################
#!/bin/python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print "hello world"

