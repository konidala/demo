import unittest
from selenium import webdriver
import time

class GoogleTestCase(unittest.TestCase):

    def testPageTitle(self):
        self.browser = webdriver.Chrome(r"C:/Users/konidapu/Downloads/chromedriver_win32/chromedriver.exe")
        self.browser.implicitly_wait(60)
        # self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://github.com/konidala/demo/commits/master')
        #self.browser.get('https://github.com/konidala/datascience/commits/master')
        total_commits_per_page = []
        for e in self.browser.find_elements_by_xpath("//div[@class='commit-links-group BtnGroup']/a"):
            total_commits_per_page.append(e.get_attribute('href'))

        older_button = self.browser.find_element_by_xpath("//*[contains(text(),'Older')]").get_attribute('href')

        for i in total_commits_per_page:
            #i.click()
            self.browser.get(i)
            time.sleep(1)
            total_files = self.browser.find_elements_by_xpath("//div[contains(@id, 'diff-')]")
            for file in total_files:
                commit_author = self.browser.find_element_by_xpath("//a[contains(@class, 'commit-author')]").text
                print(file.text)
                with open("result.txt", 'a') as file1:
                    file1.write(file.text)
                    file1.write("\n==========================================================\n")

                # committed_files = self.browser.find_elements_by_xpath("//div[contains(@id, 'diff-')]")
                # for change in committed_files:
                #     change.find_elements_by_xpath("//table[@class='datadisplaytable']")


if __name__ == '__main__':
    GoogleTestCase().testPageTitle()