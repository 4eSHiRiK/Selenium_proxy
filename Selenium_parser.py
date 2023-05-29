import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)


def proxy_parser():

    ''' Parsing information about your active proxy servers'''

    driver.get('https://proxy6.net/user/proxy')
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/ul[2]/li[2]/a')
    login_button.click()
    time.sleep(5)

    login_enter = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/div/input')
    login_enter.send_keys("YOUR_LOGIN")

    password_enter = driver.find_element(By.ID, 'login-password')
    password_enter.send_keys('YOUR_PASSWORD')
    time.sleep(60)

    confirm_button = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[7]/button')
    confirm_button.click()
    time.sleep(5)

    proxy_table = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/table').text
    proxy_table = proxy_table.split('\n')

    for index in range(len(proxy_table[3::15])):
        print(f'{proxy_table[3::15][index]} - {proxy_table[13::15][index]}')


if __name__ == '__main__':
    proxy_parser()

