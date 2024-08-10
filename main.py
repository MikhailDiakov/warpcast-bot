import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from auth import useragent, profilepath, nameprofile


def setup_browser():
    options = Options()
    options.add_argument(f"user-agent={useragent}")
    options.add_argument("--start-maximized")
    options.add_argument(profilepath)
    options.add_argument(rf"profile-directory={nameprofile}")
    driver = webdriver.Chrome(options=options)
    return driver

def fast_pause(min_time=1.03, max_time=2.29):
    time.sleep(random.uniform(min_time, max_time))

def random_pause(min_time=2.77, max_time=5.23):
    time.sleep(random.uniform(min_time, max_time))

def mid_pause(min_time=149, max_time=238):
    time.sleep(random.uniform(min_time, max_time))

def big_pause(min_time=3226, max_time=4686):
    time.sleep(random.uniform(min_time, max_time))

def like_post(post):
    try:
        like_button = post.find_element(By.XPATH, './/div[@class="group flex flex-row items-center justify-center rounded-full p-2 transition-colors hover:bg-gray-200 group-hover:bg-gray-200 dark:hover:bg-overlay-medium dark:group-hover:bg-overlay-medium text-action-red text-faint"]')
        if like_button:
            actions.move_to_element(like_button).perform()
            fast_pause()
            like_button.click()
            fast_pause()
    except Exception as e:
        pass

def repost_post(driver, post):
    try:
        recast1 = post.find_element(By.XPATH, './/div[@class="group flex flex-row items-center justify-center rounded-full p-2 transition-colors hover:bg-gray-200 group-hover:bg-gray-200 dark:hover:bg-overlay-medium dark:group-hover:bg-overlay-medium text-action-green text-faint"]')
        if recast1:
            actions.move_to_element(recast1).perform()
            driver.execute_script(f"window.scrollBy(0, {random.randint(25, 55)});")
            fast_pause()
            recast1.click()
            fast_pause()
            recast2 = driver.find_element(By.XPATH, '//button[@class="flex w-full flex-row items-center justify-start p-2 align-middle text-sm outline-none hover:cursor-pointer hover:bg-overlay-faint text-default "]')
            fast_pause()
            recast2.click()
            fast_pause()
    except Exception as e:
        pass

def comment_on_post(driver, post):
    try:
        random_ans = ['LFG', 'DD', 'xD', 'lfg', 'LFG!', 'YAY', 'wow', 'Ate!', 'you ate...', 'ate', 'WOW','gm','GM!']
        random_text = random.choice(random_ans)
        comment1 = post.find_element(By.XPATH,'.//div[@class="group flex flex-row items-center justify-center rounded-full p-2 transition-colors hover:bg-gray-200 group-hover:bg-gray-200 dark:hover:bg-overlay-medium dark:group-hover:bg-overlay-medium text-action-purple  text-faint"]')
        if comment1:
            actions.move_to_element(comment1).perform()
            fast_pause()
            comment1.click()
            fast_pause()
            driver.switch_to.active_element.send_keys(random_text)
            random_pause()
            comment2 = driver.find_element(By.XPATH,'.//button[@class="rounded-lg font-semibold border border-transparent bg-action-primary text-light active:border-action-primary-active disabled:bg-action-primary-disabled disabled:text-action-primary-disabled disabled:active:border-transparent px-[0.9333rem] py-[0.4333rem] text-sm" and @title="Reply"]')
            actions.move_to_element(comment2).perform()
            fast_pause()
            comment2.click()
    except Exception as e:
        pass

def follow_post(post):
    try:
        follow = post.find_element(By.XPATH, './/div[@class="absolute bottom-0 right-0 mb-[-4px] mr-[-4px] flex h-[20px] w-[20px] items-center justify-center rounded-full border-[2px] bg-[#E2D8F4] border-app hover:bg-[#c1a9df]"]')
        if follow:
            fast_pause()
            actions.move_to_element(follow).perform()
            fast_pause()
            follow.click()
    except Exception as ex:
        pass

driver = setup_browser()
actions = ActionChains(driver)

def main():
    posts = []
    try:
        driver.get("https://warpcast.com/~/all-channels")
        time.sleep(random.uniform(8.23, 10.45))
        
        posts = driver.find_elements(By.XPATH, '//div[contains(@class, "relative cursor-pointer px-4 py-2 hover:bg-overlay-faint")]')

        for post in posts:
            fast_pause()
            actions.move_to_element(post).perform()
            random_pause()
            
            if random.random() < 0.8:
                like_post(post)
            if random.random() < 0.5:
                repost_post(driver, post)
            if random.random() < 0.3:
                comment_on_post(driver, post)
            if random.random() < 1:
                follow_post(post)
            
            mid_pause()
        big_pause()
        main()

    except Exception as ex:
        print(f"Общая ошибка: {ex}")
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()