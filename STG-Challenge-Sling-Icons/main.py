import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class testChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_getallicons(self):
        driverwait = WebDriverWait(self.driver, 10)

        self.driver.get("https://www.sling.com")
        driverwait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@id='planOne']")))
        self.driver.find_element(By.XPATH, "//a[@id='planOne']").click()
        sling_channel_logos = self.driver.find_elements(By.XPATH, "//img[@class='all-channels-image all-channels--image active']")
        for logo in sling_channel_logos:
            print(str(logo.get_attribute("alt")) + " - " + str(logo.get_attribute("src")))

if __name__ == '__main__':
    unittest.main()