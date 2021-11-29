#!/usr/bin/python3
import nls_util as nut
from selenium import webdriver
import time as t

opts = webdriver.FirefoxOptions()
#opts.headless = True

wd = webdriver.Firefox(options=opts)
wd.get("https://sbb.ch")
wd.find_element_by_id("fromField").send_keys("Zürich, Probstei")
wd.find_element_by_id("toField").send_keys("Wald ZH, Bahnhof\n")
#wd.find_element_by_id("timepicker").send_keys("07:33")
element = wd.find_element_by_tag_name("button")

import os
os.system("clear")
#wd.quit()
#fill a form with curl
