#!/usr/bin/python3
import nls_util as nut
from selenium import webdriver
import time as t

opts = webdriver.FirefoxOptions()
#opts.headless = True

wd = webdriver.Firefox(options=opts)
'''
wd.get("https://duckduckgo.com")
t.sleep(2)
wd.quit()
'''
