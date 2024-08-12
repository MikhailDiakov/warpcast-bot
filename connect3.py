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

def fast_pause(min_time=0.83, max_time=1.49):
    time.sleep(random.uniform(min_time, max_time))

def random_pause(min_time=2.77, max_time=5.23):
    time.sleep(random.uniform(min_time, max_time))


def like_post(driver,actions):
    try:
        like = driver.find_element(By.XPATH,'.//button[@class="f16hrol c3ds-font-interactive-default-regular"]')
        if like:
            fast_pause()
            actions.move_to_element(like).perform()
            fast_pause()
            like.click()
            fast_pause()
            like2 = driver.find_element(By.XPATH, './/button[@class="f17x42hi c3ds-font-interactive-default-regular f18fbjxn"]')
            fast_pause()
            like2.click()
            fast_pause()
    except Exception as e:
        pass

def comment_post(driver,actions):
        random_ans = ['LFG', 'DD', 'xD', 'lfg', 'LFG!', 'YAY', 'wow', 'Ate!', 'you ate...', 'ate', 'WOW','gm','GM!']
        random_text = random.choice(random_ans)
        try:
            comment1 = driver.find_element(By.XPATH,'.//textarea[@class="c3ds-font-interactive-default-regular fprfxgt"]')
            if comment1:
                fast_pause()
                actions.move_to_element(comment1).perform()
                fast_pause()
                comment1.click()
                fast_pause()
                driver.switch_to.active_element.send_keys(random_text)
                fast_pause()
                comment2 = driver.find_element(By.XPATH,'.//button[@class="fs3q9v c3ds-font-interactive-default-regular fyepy8g"]')
                actions.move_to_element(comment2).perform()          
                fast_pause()
                comment2.click()
        except Exception as e:
            pass

driver = setup_browser()
actions = ActionChains(driver)

def main():
    driver.get("https://connect3.world/discover/posts")
    time.sleep(random.uniform(8.23, 10.45))
     

    processed_posts = 0  

    while True:
        posts = driver.find_elements(By.XPATH, './/li[@class="fvibj0b"]')
        for post in posts[processed_posts:]:
            fast_pause()
            actions.move_to_element(post).perform()
            come = post.find_element(By.XPATH,'.//div[@class="f8qn65z"]')
            fast_pause()
            come.click()
            random_pause()
            like_post(driver,actions)
            fast_pause()
            comment_post(driver,actions)
            exit = driver.find_element(By.XPATH,'.//div[@class="f1xrdn9y"]')
            exit2 = exit.find_elements(By.XPATH,'.//button[@class="f17x42hi c3ds-font-interactive-default-regular"]')
            fast_pause()
            exit2[1].click()
            fast_pause()

        processed_posts = len(posts)
        driver.execute_script(f"window.scrollBy(0, 1000);")
        random_pause()

        new_posts = driver.find_elements(By.XPATH, './/li[@class="fvibj0b"]')

        if len(new_posts) == processed_posts:
            break


if __name__ == "__main__":
    main()