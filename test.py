import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


list_courses = ['ENGM+spring_2020',
                'ENGM+spring_2020_net']


# Подготовка и запуск драйвера
login_url = 'https://sso.openedu.ru/login/'

profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 'dir_location') # Установка директории для скачивания
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

driver = webdriver.Firefox(profile)

# Авторизация на сайте openedu.ru

driver.get(login_url)
driver.set_window_size(1920, 1015)
WebDriverWait(driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, 'id_password')))
driver.find_element_by_id('id_username').send_keys('openedu_urfu')
driver.find_element_by_id('id_password').send_keys('15Ch3Ent!@#')
driver.find_element_by_id('id_password').send_keys(Keys.ENTER)
WebDriverWait(driver, 30000).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,
                                                                                    'dropdown-login__text')))

# Цикл загрузки результатов обучения
for course in list_courses:
    course_url = 'https://courses.openedu.ru/courses/course-v1:urfu+{}/instructor#view-data_download'.format(course)
    driver.get(course_url)
    driver.execute_script("window.scrollTo(0,1200)")
    WebDriverWait(driver, 30000).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".ui-widget-content:nth-child(1) > .slick-cell")))
    WebDriverWait(driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ui-widget-content:nth-child(1) > .slick-cell")))
    driver.find_element(By.CSS_SELECTOR, ".ui-widget-content:nth-child(1) a").click()
    driver.get('https://openedu.ru/')

driver.close()
