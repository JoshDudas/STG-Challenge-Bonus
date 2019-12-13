import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAutomatedChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_searchSlingHelpPage(self):
        self.driver.get("https://sling.com")
        driverwait = WebDriverWait(self.driver, 5)

        # Wait until the Help Center element in the footer is visbile to continue
        driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//footer[@id='footer']//a[@href='https://help.sling.com']")))

        # Get the Help Center element and click (for some reason the link requires 2 clicks to actually work)
        helpcenter_link = self.driver.find_element_by_link_text("Help Center")
        helpcenter_link.click()
        helpcenter_link.click()

        # Wait to proceed until the Help Center search field is visible
        driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='support-search-input']")))

        # Get the search field and enter Roku
        helpsearch_field = self.driver.find_element(By.XPATH, "//input[@id='support-search-input']")
        helpsearch_field.send_keys("ROKU")

        # Get the search button and click
        helpsearch_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        helpsearch_btn.click()

        # Wait to continue
        driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Search Results')]")))

        helpsearch_results = self.driver.find_elements(By.XPATH, "//ul[@class='search-results-list']//a[contains(@href, '/support/solutions/articles/')]")

        # for search_result in helpsearch_results:
        #     print(search_result.text)

        self.assertTrue((len(helpsearch_results) > 0), "No Results Found")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

