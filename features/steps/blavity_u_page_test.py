

from Navigation_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys

import time
# import os


def verify_write_a_story():
    print("inside function write a story")
    actions = ActionChains(driver)
    write_a_story_want = driver.find_element(By.XPATH, "//h2[contains(text(),'Want to')]")
    actions.move_to_element(write_a_story_want).perform()
    assert write_a_story_want.is_displayed(), "write a story 'want' title is not displayed"
    if write_a_story_want.is_displayed():
        print("write a story section is present under news")
    write_a_story_link = driver.find_element(By.XPATH, "//span[normalize-space()='write a story']")
    assert write_a_story_link.is_displayed(), "write a story link is not displayed"
    write_a_story_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    time.sleep(2)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    time.sleep(2)


def verify_traversing_dots_and_next_button_news():
    print("function called traversing dots and next button")
    actions = ActionChains(driver)
    traverse_dots = driver.find_element(By.XPATH, "//div[@id='news']//li[2]")
    actions.move_to_element(traverse_dots).perform()
    time.sleep(2)
    assert traverse_dots.is_displayed(), "traverse dots are not displayed"
    traverse_dots.click()
    time.sleep(5)
    print("clicked on dots , working appropriately")
    write_a_story_want = driver.find_element(By.XPATH, "//h2[contains(text(),'Want to')]")
    next_button = driver.find_element(
        By.CSS_SELECTOR, "div[id='news'] button[aria-label='Next']")
    actions.move_to_element(write_a_story_want).perform()
    next_button.click()
    assert next_button.is_displayed(), "next button is not displayed"
    print("clicked on right next button , working appropriately")
    time.sleep(5)


def verify_sample_and_read_more_stories_news():
    actions = ActionChains(driver)
    sample_story = driver.find_element(By.XPATH, "(//a[@class='article-link u-category-card__title'])[1]")
    actions.move_to_element(sample_story).perform()
    sample_story.click()
    assert sample_story.is_displayed(), "initial article is not displayed"
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(3)
    print("news sample article link is active")
    driver.back()
    print("back clicked 1")
    time.sleep(3)
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "//a[@href='/tags/Blavity-U-News'][normalize-space()='Load more stories']")))
    time.sleep(3)
    actions = ActionChains(driver)
    read_more_stories = driver.find_element(
        By.XPATH, "//a[@href='/tags/Blavity-U-News'][normalize-space()='Load more stories']")
    actions.move_to_element(read_more_stories).perform()
    assert read_more_stories.is_displayed(), "read more stories is not displayed"
    read_more_stories.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(2)
    print("news page is loaded with read more stories link being active")
    driver.back()
    time.sleep(2)
    print("back clicked 2")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "//a[@href='/tags/Blavity-U-News'][normalize-space()='Load more stories']")))
    time.sleep(3)


def verify_latest_news_story():
    time.sleep(3)
    actions = ActionChains(driver)
    latest_news = driver.find_element(By.XPATH, "//h2[normalize-space()='Latest News']")
    actions.move_to_element(latest_news).perform()
    assert latest_news.is_displayed(), "latest news header is not displayed"
    if latest_news.is_displayed():
        print("latest news header is present")
    number_of_stories = driver.find_elements(By.CLASS_NAME, "u-latest-section__card-container")
    assert len(number_of_stories) > 0, "stories/articles under latest news section are not displayed"
    print("number of stories in latest news section are :", len(number_of_stories))
    read_more_stories = driver.find_element(
        By.XPATH, "//button[@class='border-white btn--rounded d-none d-desktop-block mx-auto text-white']")
    assert read_more_stories.is_displayed(), "read more stories button under latest news section is not displayed"
    read_more_stories.click()
    time.sleep(2)
    print("read more stories button under latest news working as expected")
    latest_news_sample_story = driver.find_element(
        By.XPATH, "//div[@class='u-latest-section u__latest']//div[1]//div[1]//a[1]")
    latest_news_sample_story.click()
    time.sleep(2)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.back()
    print("sample story link is working as expected")
    time.sleep(2)


def verify_news_link():
    time.sleep(3)
    print("inside function verify news link of BlavityU Page")
    news_link = driver.find_element(
        By.XPATH, "//a[@class='u-navbar__link--news']")
    news_link.click()
    news_header = driver.find_element(By.XPATH, "//h2[normalize-space()='News']")
    assert news_header.is_displayed(), "news header is not displayed"
    if news_header.is_displayed():
        print("news header is present")
    temp = driver.find_element(
        By.XPATH, "//div[@id='news']//div[@class='slick-list draggable']//div[@class='slick-track']")
    number_of_articles = temp.find_elements(
        By.XPATH, "//div[@class='slick-slide slick-current slick-active']")
    # //div[@id='entertainment']//div[@class='slick-track']//div[@class='slick-slide slick-current slick-active']
    assert len(number_of_articles) > 0, "news section is not having any articles"
    print("number of articles seen in news track are :", len(number_of_articles))
    verify_sample_and_read_more_stories_news()
    verify_traversing_dots_and_next_button_news()
    time.sleep(2)
    verify_write_a_story()
    # code for sample story
    time.sleep(3)


def verify_traversing_dots_and_next_button_entertainment():
    print("function called traversing dots and next button")
    actions = ActionChains(driver)
    traverse_dots = driver.find_element(By.XPATH, "//div[@id='entertainment']//li[2]")
    actions.move_to_element(traverse_dots).perform()
    time.sleep(2)
    assert traverse_dots.is_displayed(), "traverse dots are not displayed for entertainment section"
    traverse_dots.click()
    time.sleep(5)
    print("clicked on dots , working appropriately")
    next_button = driver.find_element(
        By.XPATH, "//div[@id='entertainment']//button[@aria-label='Next'][normalize-space()='Next']")
    assert next_button.is_displayed(), "next button is not displayed for entertainment section"
    next_button.click()
    print("next button is working appropriately")
    time.sleep(2)


def verify_sample_and_read_more_stories_entertainment():
    actions = ActionChains(driver)
    sample_story = driver.find_element(
        By.XPATH,
        "(//a[@class='article-link u-category-card__title'])[10]")
    actions.move_to_element(sample_story).perform()
    assert sample_story.is_displayed(), "initial article is not displayed for entertainment"
    sample_story.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(10)
    print("entertainment sample article link is active")
    driver.back()
    print("back clicked 1")
    time.sleep(6)
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "//a[@href='/tags/Blavity-U-Entertainment']")))
    time.sleep(3)
    actions = ActionChains(driver)
    read_more_stories = driver.find_element(
        By.XPATH, "//a[@href='/tags/Blavity-U-Entertainment']")
    actions.move_to_element(read_more_stories).perform()
    assert read_more_stories.is_displayed(), "read more stories is not displayed for entertainment section"
    read_more_stories.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(2)
    print("news page is loaded with read more stories link being active")
    driver.back()
    print("back clicked 2")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "//a[@href='/tags/Blavity-U-News'][normalize-space()='Load more stories']")))
    time.sleep(3)


def verify_entertainment_link():
    time.sleep(3)
    print("inside function verify entertainment link of BlavityU Page")
    entertainment_link = driver.find_element(
        By.XPATH, "//a[normalize-space()='Entertainment']")
    actions = ActionChains(driver)
    assert entertainment_link.is_displayed(), "entertainment link is not displayed in the navBar"
    actions.move_to_element(entertainment_link).perform()
    entertainment_link.click()
    time.sleep(5)
    entertainment_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Entertainment')]")
    assert entertainment_header.is_displayed(), "entertainment header is not displayed"
    if entertainment_header.is_displayed():
        print("entertainment header is present")
    # number_of_articles = driver.find_elements(
    #     By.XPATH, "//div[@class='slick-slide slick-current slick-active']")
    temp = driver.find_element(
        By.XPATH, "//div[@id='entertainment']//div[@class='slick-list draggable']//div[@class='slick-track']")
    number_of_articles = temp.find_elements(
        By.XPATH, "//div[@class='slick-slide slick-current slick-active']")
    # //div[@id='entertainment']//div[@class='slick-track']//div[@class='slick-slide slick-current slick-active']
    assert len(number_of_articles) > 0, "entertainment section is not having any articles"
    print("number_of_articles :", len(number_of_articles))
    verify_sample_and_read_more_stories_entertainment()
    verify_traversing_dots_and_next_button_entertainment()


def verify_load_more_count_sample_story_hbc():
    load_more_stories = driver.find_element(
        By.XPATH, "//button[@class='border-white btn--rounded d-block mx-auto text-white']")
    assert load_more_stories.is_displayed(), "in hbc section load more stories button is displayed"
    count = driver.find_elements(
        By.XPATH,
        "//div[@class='u-card u-section__card']")
    assert len(count) > 0, "in hbc section stories are not present"
    print("number of stories are ", len(count) + 1)
    load_more_stories.click()
    print("clicked on load more stories once")
    time.sleep(2)
    count1 = driver.find_elements(
        By.XPATH,
        "//div[@class='u-card u-section__card']")
    print("number of stories are ", len(count1) + 1)
    assert len(count1) > len(count), "read more button is not functioning correctly"
    sample_article = driver.find_element(By.CSS_SELECTOR, "div[class='u-card u-section__card u-card--first'] span")
    actions = ActionChains(driver)
    actions.move_to_element(sample_article).perform()
    sample_article.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    time.sleep(2)
    driver.back()
    time.sleep(2)
    print("sample link of hbc section is active")


def verify_hbc_link():
    time.sleep(3)
    print("inside function verify hbc-you link of BlavityU Page")
    hbc_link = driver.find_element(
        By.XPATH, "//a[normalize-space()='HBC-YOU']")
    actions = ActionChains(driver)
    actions.move_to_element(hbc_link).perform()
    assert hbc_link.is_displayed(), "hbc link is not displayed in the navBar"
    hbc_link.click()
    time.sleep(5)
    hbc_header = driver.find_element(By.XPATH, "//h2[normalize-space()='HBC-You']")
    assert hbc_header.is_displayed(), "hbc header is not displayed"
    if hbc_header.is_displayed():
        print("hbc header is present")
    alt_img = driver.find_element(By.XPATH, "//img[@alt='HBC-You']")
    assert alt_img.is_displayed(), "hbc section having left side image is not displayed"
    verify_load_more_count_sample_story_hbc()


def verify_blavity_image_link():
    print("inside function verify blavity website link")
    blavity_link = driver.find_element(By.XPATH, "//a[@class='navbar-brand d-inline-block nuxt-link-active']")
    actions = ActionChains(driver)
    actions.move_to_element(blavity_link).perform()
    assert blavity_link.is_displayed(), "blavity news link is not present"
    if blavity_link.is_displayed():

        print("blavity news link is present")
    blavity_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    if ec.title_contains("Blavity"):
        print("blavity website link is active")
        time.sleep(3)
    driver.back()
    time.sleep(3)


def verify_instagram_link():
    actions = ActionChains(driver)
    print("inside function verify instagram link of BlavityU Page")
    instagram_link = driver.find_element(
        By.XPATH, "//li[@class='u-navbar__item--social d-grid align-items-center']//a[1]")
    actions.move_to_element(instagram_link).perform()
    assert instagram_link.is_displayed(), "instagram link is not displayed"
    instagram_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("BlavityU"))
    if driver.current_url == 'https://www.instagram.com/blavityu/':
        print("instagram link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_twitter_link():
    actions = ActionChains(driver)
    print("inside function verify twitter link of BlavityU Page")
    twitter_link = driver.find_element(
        By.XPATH, "//div[@class='u__hero']//a[2]")
    actions.move_to_element(twitter_link).perform()
    assert twitter_link.is_displayed(), "twitter link is not displayed"
    twitter_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("BlavityU"))
    if driver.current_url == 'https://twitter.com/blavityu/':
        print("twitter link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_tiktok_link():
    actions = ActionChains(driver)
    print("inside function verify tiktok link of BlavityU Page")
    tiktok_link = driver.find_element(
        By.XPATH, "//div[@class='u__hero']//a[3]")
    actions.move_to_element(tiktok_link).perform()
    assert tiktok_link.is_displayed(), "tik talk link is not displayed"
    tiktok_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("BlavityU"))
    # if driver.current_url == 'https://www.facebook.com/Blavity':
    #     print("face book link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_right_image():
    time.sleep(5)
    print("in the function to verify image section")
    right_image_section = driver.find_element(
        By.XPATH, "//div[@class='u-navbar__logo-container flex-full d-desktop-flex align-items-center text-center']")
    temp = right_image_section.is_displayed()
    assert temp, "Nav Bar Right image of Blavity U and Promo Image are missing"
    if right_image_section.is_displayed():
        print("right image section is displayed with Blabity U and promo at&t images")


def verify_nav_bar_blavity_u():
    print("inside function nav bar of BlavityU page")
    time.sleep(2)
    nav_bar = driver.find_element(
        By.CSS_SELECTOR, ".u-navbar__nav.d-none.d-desktop-flex.align-items-center.m-0.p-0.position-relative")
    temp = nav_bar.find_elements(By.TAG_NAME, "li")
    print(len(temp))
    # print(len(nav_bar))
    nav_bar_length = len(temp)
    assert nav_bar_length > 0, "nav bar left side links section is missing"
    if nav_bar_length > 0:
        print("nav bar left section link is there")
    verify_blavity_image_link()
    verify_right_image()


def verify_communication_links_hero_card_details():
    print("within function verify_communication_links_hero_card_details")
    facebook_link = driver.find_element(
      By.XPATH,
      "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/button[1]"
      "/*[name()='svg'][1]/*[name()='path'][1]")
    assert facebook_link.is_displayed(), "facebook link is not present"
    facebook_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Facebook"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    twitter_link = driver.find_element(
      By.XPATH,
      "//button[@class='btn border-circle border-0 bg-twitter text-white d-flex align-items-center "
      "justify-content-center "
      "p-0 social-sharing-link social-sharing-link--twitter']//*[name()='svg']")
    assert twitter_link.is_displayed(), "twitter link is not present"
    twitter_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Twitter"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # copied_link_button = driver.find_element(
    #   By.XPATH,
    #   "//button[@class='btn btn--click-copy border-circle border-0 bg-green text-white "
    #   "d-flex align-items-center justify-content-center p-0 has-tooltip']//*[name()='svg']//*[name()='path'][1]")
    # actions = ActionChains(driver)
    # temp_image = driver.find_element(By.XPATH, "//img[@class='u-sidebar__logo img-fluid']")
    # actions.move_to_element(temp_image).perform()
    # copied_link_button.click()
    # # open a new tab
    # print("opening a new tab")
    # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
    # driver.execute_script("window.open('','_blank');")
    # print("opened a new tab")
    # driver.switch_to.window(driver.window_handles[1])
    # # driver.get(.send_keys(Keys.ENTER))
    # text = os.environ['CLIPBOARD']
    # print("copied link is :",text)


def verify_hero_card_details():
    time.sleep(3)
    verify_communication_links_hero_card_details()
    actions = ActionChains(driver)
    print("inside function verify hero card(article below nav-bar)")
    image_wrapper = driver.find_element(By.XPATH, "//div[@class='u-hero-card__image-wrapper image-wrapper']")
    actions.move_to_element(image_wrapper).perform()
    assert image_wrapper.is_displayed(), "image wrapper section is not displayed"
    if image_wrapper.is_displayed():
        print("image of the article story is present for the hero card")
    title = driver.find_element(By.XPATH, "//a[@class='article-link u-hero-card__title']")
    assert title.is_displayed(), "title under hero card details under nav bar is not displayed"
    print("title ", title.text)
    # if title.is_displayed():
    #     assert title.is_displayed(), "title under hero card details under nav bar is not displayed"
    #     print("title ", title.text)
    """""
    # uncomment while submitting the code
    sub_title = driver.find_element(By.XPATH, "//p[@class='u-hero-card__sub-title']")
    assert sub_title.is_displayed(), "sub title under hero card details under nav bar is not displayed"
    print("sub title", sub_title.text)
    """""
    # if sub_title.is_displayed():
    #     assert title.is_displayed(), "sub title under hero card details under nav bar is not displayed"
    #     print("sub title", sub_title.text)
    """""
    uncomment while submitting the code
    story_by = driver.find_element(By.XPATH, "//div[@class='u-hero-card__info d-inline-block']")
    assert story_by.is_displayed(), "by under hero card details under nav bar is not displayed"
    print("by ", story_by.text)
    """""
    # if story_by.is_displayed():

    read_more_button = driver.find_element(By.XPATH, "//a[normalize-space()='Read More']")
    assert read_more_button.is_displayed(), "read more button for hero card details is not displayed"
    if read_more_button.is_displayed():
        print("read more button")
        read_more_button.click()
        print(driver.current_url)
        WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
        time.sleep(2)
        driver.back()
        time.sleep(3)
    # tags = driver.find_element(By.XPATH, "//div[@class='u-hero-card__tags']")
    # if tags.is_displayed():
    #     print("tag/tags is/are displayed for this article story", tags.text)


def verify_promo_image_is_present():
    print("inside function promo image is present")
    promo_image = driver.find_element(By.XPATH, "//img[@class='u-sidebar__logo img-fluid']")
    assert promo_image.is_displayed(), "promo image under nav bar left side is not displayed"
    if promo_image.is_displayed():
        print("promo image is displayed")


def verify_trending_section():
    print("inside function trending section")
    actions = ActionChains(driver)
    trending_section = driver.find_element(By.XPATH, "//div[@class='u-sidebar__trending position-sticky']")
    actions.move_to_element(trending_section).perform()
    assert trending_section.is_displayed(), "trending section is not displayed"
    if trending_section.is_displayed():
        print("trending section is displayed", trending_section.text)
    temp_ele = driver.find_element(By.XPATH, "//ol[@class='m-0 p-0']")
    number_of_trending_stories = temp_ele.find_elements(
        By.TAG_NAME, "li")
    print("number of stories in trending section are :- ", len(number_of_trending_stories))
    sample_trending_story_view = driver.find_element(
        By.XPATH, "//h4[normalize-space()='Trending']")
    sample_trending_story = driver.find_element(
        By.XPATH, "//div[@class='u-second d-flex flex-column u__second']//li[1]//a[1]")
    actions.move_to_element(sample_trending_story_view).perform()
    sample_trending_story.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    time.sleep(2)
    driver.back()
    time.sleep(5)


def verify_spotted_on_the_yard_section():
    print("inside function spotted on the yard section")
    image_spotted_section = driver.find_element(By.XPATH, "//h2[normalize-space()='Spotted on the yard']")
    actions = ActionChains(driver)
    actions.move_to_element(image_spotted_section).perform()
    assert image_spotted_section.is_displayed(), "image spotted section in yard section is not displayed"
    if image_spotted_section.is_displayed():
        print("spotted logo image is present")
    story_class_name = driver.find_elements(By.CLASS_NAME, "slick-track")
    print(len(story_class_name), "story board slick track is present")
    assert len(story_class_name) > 0, "stories in yard section are not displayed"
    slick_dots = driver.find_element(By.XPATH, "(//ul[@role='tablist'])[1]")
    assert slick_dots.is_displayed(), "slick dots in yard section is not displayed"
    if slick_dots.is_displayed():
        print("slick dots are displayed")


def verify_instagram_img():
    instagram_img_link = driver.find_element(
        By.XPATH,
        "//div[@class='u-footer__social d-flex align-items-center justify-content-center "
        "justify-content-desktop-start']//a[1]")
    assert instagram_img_link.is_displayed(), "instagram link is not displayed"
    instagram_img_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from instagram")


def verify_tik_tok_img():
    time.sleep(2)
    tik_talk = driver.find_element(By.XPATH, "//footer[@class='u-footer bg-black text-white']//a[2]")
    assert tik_talk.is_displayed(), "tik-talk link is not displayed"
    tik_talk.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from tik-talk")
    time.sleep(2)


def verify_twitter_img():
    time.sleep(2)
    twitter = driver.find_element(By.XPATH, "//footer[@class='u-footer bg-black text-white']//a[3]")
    assert twitter.is_displayed(), "twitter link is not displayed"
    twitter.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from twitter")
    time.sleep(2)


def verify_mail_img():
    time.sleep(2)
    mail = driver.find_element(By.XPATH, "//a[@href='mailto:BlavityU@blavity.com']")
    assert mail.is_displayed(), "twitter link is not displayed"
    mail.click()
    driver.switch_to.window(driver.window_handles[1])
    # WebDriverWait(driver, 40).until(ec.url_contains("mailto:BlavityU@blavity.com"))
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from mail")
    time.sleep(2)


def verify_home_footer():
    print("in the function called home")
    home_link = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
    assert home_link.is_displayed(), "home link is not displayed"
    home_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.back()
    time.sleep(2)
    print("finally back to main window from blavity.com")


def verify_about_footer():
    print("in the function called about")
    about_link = driver.find_element(By.XPATH, "//a[normalize-space()='About']")
    assert about_link.is_displayed(), "about link is not displayed"
    about_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from about")
    time.sleep(2)


def verify_portfolio_footer():
    print("in the function called portfolio")
    portfolio_link = driver.find_element(By.XPATH, "//a[normalize-space()='Brand Portfolio']")
    assert portfolio_link.is_displayed(), "brand portfolio link is not displayed"
    portfolio_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from brand portfolio")
    time.sleep(2)


def verify_case_studies_footer():
    print("in the function called case studies")
    case_studies_link = driver.find_element(By.XPATH, "//a[normalize-space()='Case Studies']")
    assert case_studies_link.is_displayed(), "case studies link is not displayed"
    case_studies_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from case studies")
    time.sleep(2)


def verify_latest_news_footer():
    print("in the function called latest news")
    latest_news_link = driver.find_element(By.XPATH, "//a[normalize-space()='Latest News']")
    assert latest_news_link.is_displayed(), "latest news link is not displayed"
    latest_news_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from latest news")
    time.sleep(2)


def verify_footer_social_media_links():
    footer_img = driver.find_element(By.XPATH, "//img[@class='u-footer__logo img-fluid']")
    assert footer_img.is_displayed(), "footer blavity U image is not displayed"
    footer_text = driver.find_element(
        By.XPATH, "//h1[contains(text(),'Connects the world to Black culture through experi')]")
    assert footer_text.is_displayed(), "footer text like 'Connects the world to' is not displayed"
    verify_instagram_img()
    # tik_tok_img()
    verify_twitter_img()
    # mail_img()


def verify_blavity_news():
    print("in the function called blavity news")
    blavity_news_link = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity : News']")
    assert blavity_news_link.is_displayed(), "blavity news link is not displayed"
    blavity_news_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from blavity news")
    time.sleep(2)


def verify_blavity_politics():
    print("in the function called blavity politics")
    blavity_politics_link = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity : Politics']")
    assert blavity_politics_link.is_displayed(), "blavity politics link is not displayed"
    blavity_politics_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from blavity politics")
    time.sleep(2)


def verify_shadow_and_act_link():
    print("in the function called shadow and act")
    shadow_and_act = driver.find_element(By.XPATH, "//a[normalize-space()='Shadow And Act']")
    assert shadow_and_act.is_displayed(), "shadow and act link is not displayed"
    shadow_and_act.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from shadow and act")
    time.sleep(2)


def verify_travel_noire_link():
    print("in the function called shadow and act")
    travel_noire = driver.find_element(By.XPATH, "//a[normalize-space()='Travel Noire']")
    assert travel_noire.is_displayed(), "travel noire link is not displayed"
    travel_noire.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from travel noire")
    time.sleep(2)


def verify_twenty_one_ninety_link():
    print("in the function called twenty one ninety")
    twenty_one_ninety = driver.find_element(By.XPATH, "//a[normalize-space()='21 Ninety']")
    assert twenty_one_ninety.is_displayed(), "21ninety link is not displayed"
    twenty_one_ninety.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from twenty one ninety")
    time.sleep(2)


def verify_afro_tech_link():
    print("in the function called afro tech")
    afro_tech = driver.find_element(By.XPATH, "//a[@href='https://blavityinc.com/afrotech']")
    assert afro_tech.is_displayed(), "Afro tech link is not displayed"
    afro_tech.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from Afro tech")
    time.sleep(2)


def verify_our_brands_footer():
    afro_tech_link_footer = driver.find_element(By.XPATH, "//a[@href='https://blavityinc.com/afrotech']")
    our_brands_img = driver.find_element(By.XPATH, "//p[normalize-space()='Our Brands']")
    assert our_brands_img.is_displayed(), "footer text 'OUR BRANDS' is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(afro_tech_link_footer).perform()
    verify_blavity_news()
    verify_blavity_politics()
    verify_shadow_and_act_link()
    verify_travel_noire_link()
    verify_twenty_one_ninety_link()
    verify_afro_tech_link()


def verify_partnerships():
    print("in the function called partnerships")
    partnership = driver.find_element(By.XPATH, "//a[normalize-space()='Partnerships']")
    assert partnership.is_displayed(), "Partnerships link is not displayed"
    partnership.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from Partnerships")
    time.sleep(2)


def verify_careers():
    print("in the function called careers")
    careers = driver.find_element(By.XPATH, "//a[@href='https://www.blavityinc.company/careers']")
    assert careers.is_displayed(), "Careers link is not displayed"
    careers.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from Careers")
    time.sleep(2)


def verify_contacts():
    print("in the function called contacts")
    careers = driver.find_element(By.XPATH, "//a[normalize-space()='Contact']")
    assert careers.is_displayed(), "Contact link is not displayed"
    careers.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from Contacts")
    time.sleep(2)


def verify_join_the_team():
    join_link_footer = driver.find_element(By.XPATH, "//p[normalize-space()='Join The Team']")
    actions.move_to_element(join_link_footer).perform()
    assert join_link_footer.is_displayed(), "footer text 'JOIN THE TEAM' is not displayed"
    verify_partnerships()
    verify_contacts()
    verify_careers()


def verify_afro_tech():
    print("in the function called verify afrotech")
    afro_tech = driver.find_element(By.XPATH, "//a[@href='https://experience.afrotech.com/']")
    assert afro_tech.is_displayed(), "Afrotech link is not displayed"
    afro_tech.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.url_contains("https://www.experience.afrotech.com/"))
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from Afrotech Experiences")
    time.sleep(2)


def verify_conferences():
    conferences_footer = driver.find_element(By.XPATH, "//p[normalize-space()='Conferences']")
    actions.move_to_element(conferences_footer).perform()
    assert conferences_footer.is_displayed(), "footer text 'CONFERENCES' is not displayed"
    verify_afro_tech()


def verify_tag_disclosure():
    tag_disclosure = driver.find_element(By.XPATH, "//a[normalize-space()='TAG Disclosure']")
    assert tag_disclosure.is_displayed(), "Afrotech link is not displayed"
    tag_disclosure.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from TAG Disclosure")
    time.sleep(2)


def common_function_test_footer(xpath, ec_param, link_name):
    print("common function used to verify footer links")
    temp_var = driver.find_element(By.XPATH, xpath)
    assert temp_var.is_displayed(), link_name+" link is not displayed"
    temp_var.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains(ec_param))
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("finally back to main window from "+link_name)
    time.sleep(2)


def verify_blavity_u_footer():
    time.sleep(2)
    actions = ActionChains(driver)
    # actions.move_to_element(image_spotted_section).perform()
    print("inside function to test blavity u footer")
    footer = driver.find_element(
        By.XPATH, "//div[@class='u-footer__header d-flex flex-column flex-desktop-row align-items-center']")
    actions.move_to_element(footer).perform()
    assert footer.is_displayed(), "footer section is not displayed"
    if footer.is_displayed():
        print("footer is present")
    verify_footer_social_media_links()
    verify_home_footer()
    verify_about_footer()
    verify_portfolio_footer()
    verify_case_studies_footer()
    verify_latest_news_footer()
    verify_our_brands_footer()
    verify_join_the_team()
    verify_conferences()
    verify_tag_disclosure()


def verify_blavity_u_page():
    page_value = "BlavityU"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[normalize-space()='BlavityU']")
    assert page.is_displayed(), "the text BlavityU is present"
    page.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//img[@title='Blavity News']")))
    verify_nav_bar_blavity_u()
    verify_news_link()
    verify_entertainment_link()
    verify_hbc_link()
    verify_hero_card_details()
    verify_latest_news_story()
    verify_instagram_link()
    verify_twitter_link()
    # verify_tiktok_link()
    verify_spotted_on_the_yard_section()
    verify_trending_section()
    verify_blavity_u_footer()


# environment()
# page_load()
# post_page_load_pop_up()
# # verify_opinion_page()
# verify_blavity_u_page()
# # verify_life_style_page()
# # verify_politics_page()
# # verify_culture_page()
# # verify_footer_presence()
# driver.quit()
