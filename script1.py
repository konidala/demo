import unittest
from selenium import webdriver
import time

class GoogleTestCase(unittest.TestCase):

    def testPageTitle(self):
        self.browser = webdriver.Chrome(r"C:/Users/konidapu/Downloads/chromedriver_win32/chromedriver.exe")
        self.browser.implicitly_wait(60)
        self.addCleanup(self.browser.quit)
        self.browser.get('https://github.com/konidala/demo/commits/master')
        #self.browser.get('https://github.com/konidala/datascience/commits/master')
        total_commits_per_page = []
        for e in self.browser.find_elements_by_xpath("//div[@class='commit-links-group BtnGroup']/a"):
            total_commits_per_page.append(e.get_attribute('href'))

        older_button = self.browser.find_element_by_xpath("//*[contains(text(),'Older')]").get_attribute('href')

        for i in total_commits_per_page:
            self.browser.get(i)
            time.sleep(1)
            total_files = self.browser.find_elements_by_xpath("//div[contains(@id, 'diff-')]")
            for file in total_files:
                commit_author = self.browser.find_element_by_xpath("//*[contains(@class, 'commit-author')]").text
                with open("result.txt", 'a') as file1:
                    table = file.find_elements_by_xpath("//tbody")

                    for tbody in table:
                        all_rows = tbody.find_elements_by_xpath(".//tr")
                        file1.write("Author: -->" + commit_author + "\n")
                        file1.write("File Name: --> " + self.browser.find_element_by_xpath("//div[contains(@class, 'file-info')]//a").text  + "\n")
                        for td in all_rows[1:]:
                            file1.write(td.find_element_by_xpath(".//td[3]").get_attribute("data-code-marker") + td.find_element_by_xpath(".//td[4]").text  + "\n")
                        file1.write("=============================================================\n")

        element = self.browser.find_element_by_xpath("//div[contains(@class, 'pagination')]//a")
        if element.is_displayed() and (element.text == 'Older'):
            pass


if __name__ == '__main__':
    GoogleTestCase().testPageTitle()