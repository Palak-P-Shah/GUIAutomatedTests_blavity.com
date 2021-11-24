from home_page_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def verify_op_eds_exhaust():
    print("in the function verify_op_eds_exhaust")
    b = driver.find_element(
      By.XPATH, "//a[@class='text-bold text-uppercase d-flex align-items-center justify-content-center']")
    assert b.is_displayed(), "Page Opinion Section is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    count = 0
    while count < 578:
        number_of_stories_for_opeds = driver.find_elements(By.CLASS_NAME, "home-op-ed-card.d-flex.flex-column")
        print("before clicking more button", len(number_of_stories_for_opeds))
        more_op_ed_button = driver.find_element(By.XPATH, "//button[contains(text(),'Read more op-eds')]")
        more_op_ed_button.click()
        WebDriverWait(driver, 40).until(
          ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Read more op-eds')]")))
        # print("after clicking more button "+str(count)+" times",len(number_of_stories_for_opeds))
        number_after_click = driver.find_elements(By.CLASS_NAME, "home-op-ed-card.d-flex.flex-column")
        temp = int(len(number_after_click))/2
        print("after clicking more button "+str(count+1) +
              " times, number of articles on the screen are :- ", str(int(temp)))
        count += 1


# environment()
# page_load()
# post_page_load_pop_up()
# verify_op_eds_exhaust()
