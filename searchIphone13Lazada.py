# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    # driver.find_element(By.CLASS_NAME,"radius").click()
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(self.base_url + "chrome://newtab/")
        driver.get("https://www.google.com/search?q=lazada&oq=lazada&aqs=chrome.0.0i271j46i131i199i433i465i512j69i59j0i131i433i512l4j0i433i512j0i512j0i271.2734j0j15&sourceid=chrome&ie=UTF-8")
        driver.find_element(By.XPATH,"//div[@id='tads']/div/div/div/div/div/a/div/span").click()
        driver.get("https://www.lazada.co.id/?exlaz=d_1:mm_150050845_51350203_2010350203::11:12493663656!118894776677!lazada!e!kwd-19342147066!c!!!!503957112711!&gclid=Cj0KCQiApKagBhC1ARIsAFc7Mc5UmUO-pYV7FfFxP1nFhvuAwhCDOfuRRQKiq_YZII8Wg0E5DCRyuqYaAmYAEALw_wcB")
        driver.find_element(By.ID,"q").click()
        driver.find_element(By.ID,"q").clear()
        driver.find_element(By.ID,"q").send_keys("iphone 13")
        driver.find_element(By.XPATH,"//div[@id='topActionHeader']/div/div[2]/div/div[2]/div/form/div/div[2]/button").click()
        driver.get("https://www.lazada.co.id/catalog/?q=iphone+13&_keyori=ss&from=input&spm=a2o4j.home.search.go.6fe053e0uX6uhD")
        driver.find_element(By.XPATH,"//div[@id='root']/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/span[2]/div").click()
        driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Terkait'])[2]/following::div[3]").click()
        driver.get("https://www.lazada.co.id/catalog/?_keyori=ss&from=input&page=1&q=iphone%2013&sort=priceasc&spm=a2o4j.home.search.go.6fe053e0uX6uhD")
        driver.find_element(By.XPATH,"//img[@alt='IPHONE 13 Mini Ultimate FS HDC']").click()
        driver.get("https://www.lazada.co.id/products/iphone-13-mini-ultimate-fs-hdc-i6862364264-s13005878793.html?clickTrackInfo=query%253Aiphone%252B13%253Bnid%253A6862364264%253Bsrc%253ALazadaMainSrp%253Brn%253Aa651276ed6b12bc4367f3b6083a3aac5%253Bregion%253Aid%253Bsku%253A6862364264_ID%253Bprice%253A2450000%253Bclient%253Adesktop%253Bsupplier_id%253A400621188431%253Basc_category_id%253A42006401%253Bitem_id%253A6862364264%253Bsku_id%253A13005878793%253Bshop_id%253A4111924&fastshipping=0&freeshipping=0&fs_ab=1&fuse_fs=0&lang=id&location=Kota%20Pekanbaru&price=2.45E%206&priceCompare=&ratingscore=0&request_id=a651276ed6b12bc4367f3b6083a3aac5&review=&sale=0&search=1&source=search&spm=a2o4j.searchlist.list.i80.14a89f32Z0ES8u&stock=1")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
