from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


x = 0
driver = webdriver.Chrome(ChromeDriverManager().install())


def main():
    driver.get("https://yndx-test.ru/aci89e7kdo1g6q2v/")

    first_num = '27'
    num1 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[1]')
    num1.send_keys(first_num)

    second_num = '225'
    num2 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[2]')
    num2.send_keys(second_num)

    third_num = '988'
    num3 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[3]')
    num3.send_keys(third_num)

    fourth_num = '42'
    num4 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[4]')
    num4.send_keys(fourth_num)

    fifth_num = str(x)
    num5 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[5]')
    num5.send_keys(fifth_num)

    submit = driver.find_element("xpath", '//*[@id="action_form"]/form/button')
    submit.click()

    driver.back()


main()


def sm_try():
    fifth_num = str(x)
    num5 = driver.find_element("xpath", '//*[@id="action_form"]/form/input[5]')
    num5.clear()
    num5.send_keys(fifth_num)

    submit = driver.find_element("xpath", '//*[@id="action_form"]/form/button')
    submit.click()


while True:
    sm_try()
    if (driver.current_url != 'https://yndx-test.ru/aci89e7kdo1g6q2v/fail.php') and (driver.current_url != 'https://yndx-test.ru/aci89e7kdo1g6q2v/'):
        break
    else:
        x += 1
    print(x)
    driver.back()

print('The End')

time.sleep(1515)
