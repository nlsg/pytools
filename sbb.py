#!/usr/bin/python3
import nls_util as nut
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
import os
from os import system as s

opts = webdriver.FirefoxOptions()
#opts.headless = True

wd = webdriver.Firefox(options=opts)
def submit_query(from_field, to_field):
  wd.get("https://sbb.ch")
  wd.find_element_by_id("fromField").send_keys(from_field)
  wd.find_element_by_id("toField").send_keys(to_field)
  #wd.find_element_by_id("timepicker").send_keys("07:33")

  element = wd.find_element_by_class_name("mod_fieldset_controls")
  element.find_elements_by_xpath("//button[@class='text__primarybutton button' and @type='submit']")[0].click()

submit_query("Zürich, Probstei", "Wald ZH, Bahnhof\n")

# wd.find_elements_by_xpath("//button[@class='mod_accordion_item_link var_timetable' and @type='button']")[0].click()
ele = wd.find_elements_by_xpath("//svg[@id='SBB_03_plus']")
ele = wd.find_elements(By.XPATH, "//button[@class='mod_accordion_item_link var_timetable']")
nut.listing(ele)


# s("clear")
wd.quit()
#fill a form with curl
