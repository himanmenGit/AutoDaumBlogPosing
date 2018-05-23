import os

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, inspect


class DaumPosting:

    def __init__(self, ui, **kwargs):
        # for window
        current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
        driver_path = os.path.join(current_folder, 'chromedriver.exe')

        # for linux
        # current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
        # driver_path = os.path.join(current_folder, 'chromedriver.exe')

        self.browser = webdriver.Chrome(driver_path)

        self.ui = ui

        self.id = kwargs['id']
        self.pw = kwargs['pw']
        self.title = kwargs['title']
        self.content = kwargs['content']
        self.repeat = int(kwargs['repeat'])

    def setBrowser(self, **kwargs):
        self.browser.get('https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fblog.daum.net%2F')

        self.browser.find_element_by_name('id').send_keys(self.id)
        self.browser.find_element_by_name('pw').send_keys(self.pw)
        self.browser.find_element_by_xpath('//*[@id="loginBtn"]').click()

        logo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#daumServiceLogo")))

        if self.repeat > 100:
            self.repeat = 100
        elif self.repeat <= 0:
            self.repeat = 1

        for i in range(self.repeat):
            self.browser.get(
                'http://m.blog.daum.net/_blog/_m/articleRegisterForm.do?blogid=0uPSK&categoryId=&returnURL=http%3A%2F%2Fm.blog.daum.net%2F' + self.id)
            self.browser.implicitly_wait(3)

            title = self.browser.find_element_by_css_selector('#articleTitle')
            title.click()
            title.send_keys(self.title)

            content = self.browser.find_element_by_css_selector('#me_editor > textarea')
            content.click()
            content.send_keys(self.content)

            show = self.browser.find_element_by_xpath('//*[@id="articleOpen"]/option[text()="전체공개"]')
            show.click()

            btn = self.browser.find_element_by_css_selector(
                '#form > div.mblog_btn_bg > a.mblog_btn.mblog_btn_highlight')
            btn.click()

        self.ui.logUpdate(f'총 {self.repeat}회 포스팅 완료')

        self.browser.quit()
