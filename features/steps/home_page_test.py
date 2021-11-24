
from environment import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def environment():
    driver.maximize_window()
    driver.get(url_name)
    time.sleep(5)
    print(driver.title)


def page_load():
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    assert driver.current_url == url_name, "url does not match"


def post_page_load_pop_up():
    try:
        event_promo_pop_up = driver.find_element_by_xpath(
          "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
        driver.execute_script("arguments[0].click();", event_promo_pop_up)
    except NoSuchElementException:
        print("event promo pop-up does not exist")
    try:
        driver.switch_to.frame("sp_message_iframe_565136")
        pop_up_text = driver.find_element(By.XPATH, "//p[normalize-space()='We value your privacy']")
        if pop_up_text.is_displayed():
            accept_button = driver.find_element(By.XPATH, "//button[@title='Accept']")
            accept_button.click()
        driver.switch_to.parent_frame()
    except NoSuchElementException:
        print("blavity news privacy pop-up does not exist")
    footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
    driver.execute_script("arguments[0].click();", footer_xpath)
    assert driver.title == "The Community for Black Creativity and News - Blavity News", "title does not match"


def verify_presence_of_element_in_page():
    verify_blavity_news_at_top()
    right_arrow = driver.find_element(By.XPATH, "//button[@id='home-hero-slick-arrow-next']")
    assert right_arrow.is_displayed(), "right arrow element is not present"


def verify_if_ticker_exists():
    ticker = driver.find_element(By.XPATH, "//div[@class='story-ticker__wrapper d-flex align-items-center']")
    assert ticker.is_displayed(), "ticker is not present"
    assert (ticker.text != "") and (ticker.text is not None), "ticker text is not present"
    # print("text :", ticker.text)
    if (ticker.text != "") and (ticker.text is not None):
        print("Ticker Exists")
        # assert_equal(True, True, "ticker section is present")


def ticker_text_values(ticker_items):
    items = []
    count_test = 0
    while count_test < len(ticker_items):
        print("count test is: ", count_test)
        temp_test_temp = ticker_items[count_test].text
        items.append(temp_test_temp)
        print("txt test is : ", temp_test_temp)
        count_test += 1
        # time.sleep(1)
    print("test array", items)
    print("number of items in array", len(items))
    # element = ""
    # var1 = ""
    # if element in items:
    #   print("empty string position is : ", items.index(element))
    #   var1 = items.index(element)
    time.sleep(1)
    return items


def verify_ticker_count_and_links():
    ticker_items = driver.find_elements(By.CLASS_NAME, "story-ticker-item")
    deduced_array_items = ticker_text_values(ticker_items)
    element = ""
    # var1 = ""
    if element in deduced_array_items:
        print("after iteration array has empty string")
        while element in deduced_array_items:
            deduced_array_items = ticker_text_values(ticker_items)
            if "" not in deduced_array_items:
                break
            var1 = deduced_array_items.index(element)
            print("value is missing at position", var1)
            # time.sleep(2)
    else:
        print("array has no empty string")
    # ticker_text_values(ticker_items)
    print("finally array is, ", deduced_array_items)
    print("count :- ", len(ticker_items))
    assert len(ticker_items) > 0, "ticker items are not present in the ticker"
    # number = len(ticker_items)
    # ticker_text_values(ticker_items)
    time.sleep(1)
    count = 0
    while count < len(ticker_items):
        # time.sleep(1)
        print("count: ", count)
        time.sleep(1)
        temp_test_temp = deduced_array_items[count]
        time.sleep(1)
        print("txt is : ", temp_test_temp)
        print("required link : ", ticker_items[count].get_attribute('href'))
        new_url = ticker_items[count].get_attribute('href')
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url in new tab
        driver.get(new_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = str(temp_test_temp)
        print("deduced string is :", temp[0])
        print("text string is :", temp_test_temp)
        assert compare_1 == compare_2, "for ticker links, for one of the links , title text does not match"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        count += 1
        time.sleep(1)
    print("All the ticker links do work as expected")
    pass


def verify_if_all_carousel_entries_works():
    number_of_entries = driver.find_elements(By.CLASS_NAME, "home-hero-card__title-wrapper")
    assert len(number_of_entries) > 0, "no elements found in the carousel"
    print("number of entries in Carousel are :- ", len(number_of_entries))
    for y in range(len(number_of_entries)):
        # print("string value is :",str(y))
        temp_string = str(y+1)
        # print("tempString value is :", tempString)
        final_string = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["\
                       + temp_string + "]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]"
        # print("finalString value is :", finalString)
        b2 = driver.find_element(By.XPATH, final_string)
        assert (b2.get_attribute('href') is not None) and (b2.get_attribute('href') != ""), \
            "particular carousel link is not found"
        # print("carousel txt : ", b2.text)
        print("carousel required link : ", b2.get_attribute('href'))
        carousel_link_url = b2.get_attribute('href')
        if (carousel_link_url is None) or (carousel_link_url == ""):
            print("particular carousel link is not there")
        # driver.get(b[z].get_attribute('href'))
        # webbrowser.get("C:\exe installer\chrome driver\chromedriver_win32\chromedriver.exe")
        # .open(b[z].get_attribute('href'))
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url present in carousel link in a new tab
        driver.get(carousel_link_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current carousel window title: " + driver.title)
        # temp_str = driver.title
        # temp = temp_str.split(' -')
        # compare_1 = str(temp[0])
        # compare_2 = str(temp_test)
        # assert compare_1 == compare_2, "for ticker links, for one of the links , title text does not match"
        # print("deduced string is :", temp[0])
        # print("text string is :", temp_test)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    print("All the Carousel links do work as expected")
    pass


def verify_carousel_read_more_arrows():
    verify_presence_of_element_in_page()
    print("inside function carousel read more and arrows verification")
    number_of_entries = driver.find_elements(By.CLASS_NAME, "home-hero-card__title-wrapper")
    assert len(number_of_entries) > 0, "articles are not present in carousel"
    print("number of entries in Carousel are :- ", len(number_of_entries))
    left_click_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]"
                                                      "/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]")
    assert left_click_button.is_displayed(), "left click arrow button is not displayed in carousel"
    right_click_button = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[2]")
    assert right_click_button.is_displayed(), "right click arrow button is not displayed in carousel"
    if right_click_button.is_displayed() and right_click_button.is_displayed():
        print("both right and left click buttons are displayed on this page")
    count = 0
    while count < len(number_of_entries):
        time.sleep(2)
        temp_string = str(count+1)
        # print("count : ",count)
        # print("tempString : ", tempString)
        temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["\
                     + temp_string + "]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/a[1]"
        temp_xpath_article_heading = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[" \
                                     + temp_string + "]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]"
        # print("tempXPath : ", tempXPath)
        # actions = ActionChains(driver)
        article_heading = driver.find_element(By.XPATH, temp_xpath_article_heading)
        assert article_heading.is_displayed(), "article heading is not displayed in carousel"
        article = str(article_heading.text)
        print("article is :", article)
        read_more_button = driver.find_element(By.XPATH, temp_xpath)
        assert read_more_button.is_displayed(), "read more button for particular article is missing"
        if read_more_button.is_displayed():
            # actions.move_to_element(read_more_button).perform()
            driver.execute_script("arguments[0].click();", read_more_button)
            time.sleep(3)
            print("clicked on read more button")
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
            print("Current window title: " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = article
            print("deduced string is :", compare_1)
            print("text string is :", compare_2)
            assert compare_1 == compare_2, "for Carousel links, for one of the links , title text does not match"

            # driver.back()
            driver.execute_script("window.history.go(-1)")
            WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
            temp = 0
            while temp < (count + 1):
                # print("inside the while temp variable value is ", temp)
                # click on the left click button (temp) number of times
                time.sleep(3)
                right_arrow = driver.find_element(By.XPATH, "//button[@id='home-hero-slick-arrow-next']")
                right_arrow.click()
                # driver.execute_script("arguments[0].click();", right_click)
                time.sleep(1)
                temp += 1
                print("clicked the right icon number of times :- ", temp)
            count += 1
    print("All the Read More Links are working as expected along with left and right click arrow buttons in Carousel")
    pass


def verify_side_bar_top_stories():
    print("Within the function call top stories")
    b = driver.find_element(By.CSS_SELECTOR, ".home-top-stories.page-home__top-stories.flex-full")
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    inner_class = driver.find_elements(By.CLASS_NAME, "home-top-story-card__title-container")
    assert len(inner_class) > 0, "stories are not present for side bar top stories"
    print("number of instances under the top stories section are :", len(inner_class))
    # tempCountIs = driver.find_elements_by_css_selector
    # ("div[class='home-top-stories page-home__top-stories flex-full'] ul")
    for x in range(len(inner_class)):
        temp_string = str(x + 1)
        # count = int(tempCount)
        temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/aside[1]/div[2]/ul[1]/li["\
                     + str(temp_string) + "]/div[1]/div[2]/div[1]/a[1]"
        b = driver.find_element(By.XPATH, temp_xpath)
        compare_1 = str(b.text)
        assert b.is_displayed(), "particular side bar top story is not present"
        print("top story required link : ", b.get_attribute('href'))
        top_story_link_url = b.get_attribute('href')
        if (top_story_link_url is None) or (top_story_link_url == ""):
            print("particular top story link is not there")
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url present in carousel link in a new tab
        driver.get(top_story_link_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current top story window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_2 = str(temp[0])
        assert compare_1 == compare_2, "for side bar top stories, for this particular story, the text does not match"
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    print("All the Side bar Top Stories links do work as expected")
    pass


def verify_load_more_stories_home_page():
    print("inside function load more stories")
    # check on load more stories button
    b = driver.find_element(By.XPATH, "//button[normalize-space()='Load more stories']")
    assert b.is_displayed(), "load more stories button is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the Load More Stories button is there")
        # click on the button once
        driver.execute_script("arguments[0].click();", b)
        print("clicked on Load More Stories button once")
        # wait for the stories to be loaded and the button to appear
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
            By.XPATH, "//button[normalize-space()='Load more stories']")))
        # click on the button twice
        time.sleep(3)
        b = driver.find_element(By.XPATH, "//button[normalize-space()='Load more stories']")
        actions = ActionChains(driver)
        actions.move_to_element(b).perform()
        driver.execute_script("arguments[0].click();", b)
        print("clicked on Load More Stories button twice, now there are 6 stories")
        # again wait for stories to be loaded.
        WebDriverWait(driver, 40).until(
            ec.presence_of_element_located((By.XPATH, "//button[normalize-space()='Load more stories']")))
        time.sleep(2)  # this is added since seeing intermittent failures here
        count = 0
        print("now iterating stories")
        while count < 3:
            time.sleep(2)
            temp_string = str(count + 1)
            temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]" \
                         "/div[1]/div[1]/div[1]/div[" + temp_string + "]/div[2]/a[1]"
            # print('here is the tem xpath within the load more stories..'+temp_xpath)
            temp_element_story = driver.find_element(By.XPATH, temp_xpath)
            temp_test = temp_element_story.text
            print("temp_test :", temp_test)
            actions = ActionChains(driver)
            actions.move_to_element(temp_element_story).perform()
            print("loaded story required link : ", temp_element_story.get_attribute('href'))
            loaded_story_link_url = temp_element_story.get_attribute('href')
            assert loaded_story_link_url is not None and loaded_story_link_url != "", "" \
                "Under load more stories the story link is not present"
            if (loaded_story_link_url is None) or (loaded_story_link_url == ""):
                print("particular top story link is not there")
            # open a new tab
            # print("opening a new tab")
            # driver.find_element_by_xpath("body").send_keys(Keys.CONTROL + 't')
            # driver.execute_script("arguments[0].click();", loaded_story_link_url)
            # driver.execute_script("window.open('','_blank');", loaded_story_link_url)
            # print("opened a new tab")
            # switch command to the new tab being opened.
            # driver.switch_to.window(driver.window_handles[1])
            # open the url present in carousel link in a new tab
            driver.get(loaded_story_link_url)
            # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
            print("Current window title for loaded story: " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = str(temp_test)
            assert compare_1 == compare_2, "for ticker links, for one of the links , title text does not match"
            print("deduced string is :", temp[0])
            print("text string is :", temp_test)
            driver.back()
            WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
            # driver.close()
            driver.switch_to.window(driver.window_handles[0])
            count += 1
    print("All the Load More Stories links for 2 iterations do work as expected for 3 articles")
    pass


def verify_subscribe_banner_section():
    print("inside function subscribe_banner_section")
    b = driver.find_element(By.XPATH, "//h4[contains(text(),'Want a daily dose of Blavity News?')]")
    assert b.is_displayed(), "subscribe banner text is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the subscribe_banner_section is there")
        email_field = driver.find_element(By.XPATH, "//input[@class='bg-red border-0 text-white w-100']")
        assert email_field.is_displayed(), "email field is not displayed under subscribe banner section"
        email_field.send_keys("fortestpurposesonly5@gmail.com")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='submit']")
        assert submit_button.is_displayed(), "submit button is not displayed under subscribe banner section"
        # actions = ActionChains(driver)
        actions.move_to_element(submit_button).perform()
        driver.execute_script("arguments[0].click();", submit_button)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
            By.XPATH, "//p[contains(text(),'Welcome to the family!')]")))
        after_click = driver.find_element(By.XPATH, "//p[contains(text(),'Welcome to the family!')]")
        assert after_click.is_displayed(), \
            "after clicking submit, the text is not displayed under subscribe banner section"
        if ec.visibility_of_element_located(after_click):
            print("submit button works as expected")
            pass


def verify_lunchtable_section():
    # this function verifies if the lunchtable logo exists, checkout more link works and the video exists
    print("inside function call lunchtable section")
    b = driver.find_element(By.XPATH, "//div[@class='home-lunchtable position-relative text-center text-desktop-left']")
    assert b.is_displayed(), "lunchtable section is not displayed"
    if b.is_displayed():
        print("lunchtable section is there")
        link_lunchtable_webelement = driver.find_element(
            By.XPATH, "//a[@class='btn btn-outline-primary d-none d-desktop-inline-block text-bold text-uppercase']")
        # actions = ActionChains(driver)
        actions.move_to_element(link_lunchtable_webelement).perform()
        print("lunchtable link : ", link_lunchtable_webelement.get_attribute('href'))
        link_lunchtable = link_lunchtable_webelement.get_attribute('href')
        assert link_lunchtable is not None and link_lunchtable != "", "lunchtable link is not present"
        if (link_lunchtable is None) or (link_lunchtable == ""):
            print("lunchtable link is not there")
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url present in carousel link in a new tab
        driver.get(link_lunchtable)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title for lunchtable is: " + driver.title)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # check for the video section
        video_path = driver.find_element(By.XPATH, "//video[@class='jw-video jw-reset']")
        assert video_path.is_displayed(), "video is not present for lunchtable section"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ".jwplayer.image-wrapper.image-wrapper--16x9.home-lunchtable__player")))
        print("video is present")
        pass


def verify_blavity_originals_section():
    # this function verifies if all the 8 links in the section works fine
    print("in the function blavity originals section ")
    # temp_element = driver.find_elements(By.CLASS_NAME, "article-link home-original-card__title text-bold")
    # print(len(temp_element))
    b = driver.find_element(By.XPATH, "//h3[normalize-space()='Blavity Originals']")
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    assert b.is_displayed(), "text heading is present for blavity originals"
    if b.is_displayed():
        print("blavity originals section is there")
        count = 0
        while count < 8:
            temp_str = str(count + 1)
            temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[6]" \
                         "/div[1]/div[2]/div[1]/div[1]/div["+temp_str+"]/div[1]/div[1]/div[2]/div[2]/div[1]/a[1]"
            b = driver.find_element(By.XPATH, temp_xpath)
            # actions = ActionChains(driver)
            actions.move_to_element(b).perform()
            print("loaded link of blavity originals : ", b.get_attribute('href'))
            blavity_original_link_url = b.get_attribute('href')
            temp_var = b.text
            print("sample text :", temp_var)
            assert blavity_original_link_url is not None and blavity_original_link_url != "", \
                "particular blavity originals article link is present"
            if (blavity_original_link_url is None) or (blavity_original_link_url == ""):
                print("particular blavity original link is not there")
            # open a new tab
            print("opening a new tab")
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
            driver.execute_script("window.open('','_blank');")
            print("opened a new tab")
            # switch command to the new tab being opened.
            driver.switch_to.window(driver.window_handles[1])
            # open the url present in carousel link in a new tab
            driver.get(blavity_original_link_url)
            # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
            print("Current window title for blavity original: " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = str(temp_var)
            assert compare_1 == compare_2, "for a particular story of blavity originals, title text does not match"
            print("deduced string is :", temp[0])
            print("text string is :", temp_var)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            count += 1
        print("all the links of blavity originals section are working correctly")
        pass


def verify_page_op_ed_section():
    # this function verified if the Op_ed section is visible on the page,
    # and verified if all the 6 links within this section works
    print("in the function page op ed section")
    b = driver.find_element(
        By.XPATH, "//a[@class='text-bold text-uppercase d-flex align-items-center justify-content-center']")
    assert b.is_displayed(), "Page Opinion Section is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the op ed section is displayed")
        print("link to blavity's op ed section : ", b.get_attribute('href'))
        driver.execute_script("arguments[0].click();", b)
        print("Current Page title: " + driver.title)
        # see whether login page is presented or not.
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Login']")))
        # back to previous page with back()
        driver.back()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((
            By.XPATH, "//button[normalize-space()='Read more op-eds']")))
        time.sleep(2)
        # tempElementtest = driver.find_elements_by_css_selector
        # ("div[class='page-home__op-ed__articles d-grid'] div:nth-child(1) div:nth-child(2)
        # div:nth-child(2) a:nth-child(1)")
        # print(len(tempElementtest))
        print("Current Page title after back: " + driver.title)
        time.sleep(3)
        more_op_ed_button = driver.find_element(By.XPATH, "//button[contains(text(),'Read more op-eds')]")
        from_other_sites = driver.find_element(By.XPATH, "//h2[normalize-space()='From Our Other Sites']")
        count = 0
        while count < 6:
            temp_string = str(count + 1)
            time.sleep(2)
            temp_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[2]/" \
                         "div[1]/div[" + temp_string + "]/div[2]/div[2]/a[1]"
            # print(tempXpath)
            b = driver.find_element(By.XPATH, temp_xpath)
            temp_var = str(b.text)
            actions = ActionChains(driver)
            actions.move_to_element(b).perform()
            print("loaded link of op ed : ", b.get_attribute('href'))
            op_ed_original_link_url = b.get_attribute('href')
            assert (op_ed_original_link_url is not None) and (op_ed_original_link_url != ""),\
                "opinon ed article url is not present"
            if (op_ed_original_link_url is None) or (op_ed_original_link_url == ""):
                print("particular op ed link is not there")
            # open a new tab
            print("opening a new tab")
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
            driver.execute_script("window.open('','_blank');")
            print("opened a new tab")
            # switch command to the new tab being opened.
            driver.switch_to.window(driver.window_handles[1])
            # open the url present in carousel link in a new tab
            driver.get(op_ed_original_link_url)
            # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
            print("Current window title for opinion ed is : " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = temp_var
            assert compare_1 == compare_2, "for a particular story of opinon ed's sections, title text does not match"
            print("deduced string is :", compare_1)
            print("text string is :", compare_2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            count += 1
        print("all the links in op ed are working as expected")
        actions.move_to_element(from_other_sites).perform()
        driver.execute_script("arguments[0].click();", more_op_ed_button)
        print("Read more op-eds button is working as expected")
        pass


def verify_from_our_other_sites():
    print("in function from our other sites")
    from_other_sites = driver.find_element(By.XPATH, "//h2[normalize-space()='From Our Other Sites']")
    assert from_other_sites.is_displayed(), "from our other sites section is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(from_other_sites).perform()
    number_of_ele = driver.find_elements(By.CLASS_NAME, "home-oo-card__site-name")
    assert len(number_of_ele) > 0, "articles are not there in from our other sites section."
    count = 0
    while count < len(number_of_ele):
        temp_string = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[2]/div[1]/div[1]" \
                      "/div[1]/div["+str(count+1) + "]/div[1]/div[1]/div[2]/div[2]/a[1]"
        temp_ele = driver.find_element(By.XPATH, temp_string)
        actions = ActionChains(driver)
        actions.move_to_element(temp_ele).perform()
        assert temp_ele.is_displayed(), "particular article is not displayed of from our other sites section"
        compare_var = str(temp_ele.text)
        print("loaded link of other sites : ", temp_ele.get_attribute('href'))
        blavity_other_link_url = temp_ele.get_attribute('href')
        assert blavity_other_link_url is not None and blavity_other_link_url != "", \
            "article link is not there for particular blavity other link url"
        if (blavity_other_link_url is None) or (blavity_other_link_url == ""):
            print("particular other site link is not there")
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url present in carousel link in a new tab
        driver.get(blavity_other_link_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title for from our other links: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = compare_var
        assert compare_1 == compare_2, "for a particular story from our other sites, title text does not match"
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        count += 1
    pass


def verify_blavity_news_at_top():
    print("function called to verify_blavity_news_at_top")
    blavity_logo = driver.find_element(By.XPATH, "//header//nav[1]//div[1]//div[1]//a[1]//img[1]")
    assert blavity_logo.is_displayed(), "Blavity:News image is not present"
    blavity_logo.click()
    WebDriverWait(driver, 40).until(
        ec.presence_of_element_located((By.XPATH, "//header//nav[1]//div[1]//div[1]//a[1]//img[1]")))


def verify_blavity_footer():
    print("function called to check blavity footer")

    # driver.get("https://staging.blavity.com")
    # page_load()
    # post_page_load_pop_up()
    # driver.switch_to.frame("ad_is_1634275213042_ifr")
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='side-tile']")))
    # pop_up = driver.find_element(By.XPATH, "//div[@id='side-tile']")
    # if pop_up.is_displayed():
    #     print(pop_up.text)
    #     close = driver.find_element(By.XPATH, "//img[@data-pin-nopin='true']")
    #     close.click()
    all_rights_reserved = driver.find_element(
        By.XPATH, "//p[contains(text(),'© 2021 Blavity, Inc. All rights reserved.')]")
    assert all_rights_reserved.is_displayed(), "under footer all rights reserved text is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(all_rights_reserved).perform()
    # image = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/footer[1]/div[1]/img[1]")
    if all_rights_reserved.is_displayed():
        print("footer blavity image is present")
        fb_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/Blavity']")
        assert fb_blavity.is_displayed(), "facebook link is not displayed under footer"
        actions.move_to_element(all_rights_reserved).perform()
        if fb_blavity.is_displayed():
            print("footer facebook image is present")
            fb_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/Blavity']")
            fb_blavity.location_once_scrolled_into_view
            time.sleep(2)
            fb_blavity.click()
            verify_blavity_footer_facebook()
        twitter_blavity = driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[1]/div[1]/footer[1]/div[2]/ul[2]/li[2]/a[1]")
        assert twitter_blavity.is_displayed(), "twitter link is not displayed under footer"
        if twitter_blavity.is_displayed():
            print("footer tweeter image is present")
            twitter_blavity.click()
            verify_blavity_footer_twitter()
        instag_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.instagram.com/blavity']")
        assert instag_blavity.is_displayed(), "instagram link is not displayed under footer"
        if instag_blavity.is_displayed():
            print("footer instagram image is present")
            instag_blavity.click()
            verify_blavity_footer_instagram()
        if all_rights_reserved.is_displayed():
            print("All rights reserved condition is there")
        link_careers = driver.find_element(By.XPATH, "//a[@class='text-bold'][normalize-space()='Careers']")
        assert link_careers.is_displayed(), "careers link is not displayed under footer"
        if link_careers.is_displayed():
            print("Careers link is displayed")
            link_careers.click()
            open_new_tab_and_verify()
            print("footer career's link is active")
        link_terms = driver.find_element(By.XPATH, "//a[normalize-space()='Terms']")
        assert link_terms.is_displayed(), "terms link is not displayed under footer"
        if link_terms.is_displayed():
            print("terms link is displayed")
            link_terms.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer terms link is active")
        link_privacy = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy']")
        assert link_privacy.is_displayed(), "privacy link is not displayed under footer"
        if link_privacy.is_displayed():
            print("privacy link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_privacy.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer privacy link is active")
        link_adv = driver.find_element(By.XPATH, "//a[normalize-space()='Advertise']")
        assert link_adv.is_displayed(), "Advertise link is not displayed under footer"
        if link_adv.is_displayed():
            print("Advertise link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_adv.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer advertise link is active")
        link_media = driver.find_element(By.XPATH, "//a[contains(text(),'Media Passes')]")
        assert link_media.is_displayed(), "Media link is not displayed under footer"
        if link_media.is_displayed():
            print("Media Passes link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_media.click()
            # switch to the new tab being opened.
            verify_blavity_footer_link_media()
        #   as "privacy preferences" link is removed , from footer, thus this code is commented.
        # link_prefer = driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Preferences')]")
        # assert link_prefer.is_displayed(), "Preferences link is not displayed under footer"
        # if link_prefer.is_displayed():
        #     print("Privacy Preferences link is displayed")
        #     actions.move_to_element(all_rights_reserved).perform()
        #     link_prefer.click()
        #     # switch to the new tab being opened.
        #     verify_blavity_footer_preferences()
    pass


def verify_blavity_footer_facebook():
    print("inside function footer facebook link")
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert driver.current_url == 'https://www.facebook.com/Blavity', "facebook link in footer is not active"
    if driver.current_url == 'https://www.facebook.com/Blavity':
        print("face book link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_twitter():
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert driver.current_url == 'https://twitter.com/blavity', "twitter link in footer is not active"
    if driver.current_url == 'https://twitter.com/blavity':
        print("twitter link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_instagram():
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("blavity"))
    assert driver.current_url == 'https://www.instagram.com/blavity/', "instagram link in footer is not active"
    if driver.current_url == 'https://www.instagram.com/blavity/':
        print("instagram link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def open_new_tab_and_verify():
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    # assert ec.title_contains("Blavity") == 'https://www.instagram.com/blavity/', "instagram link in footer is active"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_preferences():
    time.sleep(5)
    driver.switch_to.frame("sp_message_iframe_410351")
    # manage_pre = driver.find_element_by_xpath("//p[normalize-space()='Manage your preferences']")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located(
        (By.XPATH, "//p[normalize-space()='Manage your preferences']")))
    close_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
    actions = ActionChains(driver)
    actions.move_to_element(close_btn).perform()
    assert close_btn.is_displayed(), "close button is not displayed for preferences under footer"
    close_btn.click()
    print("footer privacy preferences link is active")


def verify_blavity_footer_link_media():
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_is("Media Credentials Request Form"))
    assert "Media Credentials Request Form" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("footer media passes link is active")


# environment()
# page_load()
# post_page_load_pop_up()
# verify_presence_of_element_in_page()
# verify_if_ticker_exists()
# verify_ticker_count_and_links()
# # verify_if_all_carousel_entries_works() is this required verify_carousel_read_more_arrows is doing what is required
# verify_carousel_read_more_arrows()
# verify_side_bar_top_stories()
# verify_load_more_stories_home_page()
# verify_subscribe_banner_section()
# verify_lunchtable_section()
# verify_blavity_originals_section()
# verify_page_op_ed_section()
# verify_from_our_other_sites()
# verify_blavity_footer()
