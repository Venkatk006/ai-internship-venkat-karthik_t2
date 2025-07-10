from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

print("Will write logs to:", os.path.join(os.getcwd(), "task2_log.txt"))

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def log_action(message):
    print(message)
    with open("task2_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

def take_screenshot(driver, name):
    filename = f"{name.replace(' ', '_')}.png"
    driver.save_screenshot(filename)
    log_action(f"Screenshot saved: {filename}")

def handle_command(driver, command):
    command = command.strip().lower()
    success = False

    if command.startswith("click") or command.startswith("go to"):
        keyword = command.replace("click", "").replace("go to", "").strip().lower()

        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            text = link.text.strip().lower()
            if keyword in text:
                link.click()
                time.sleep(2)
                log_action(f"Clicked on link: {text}")
                take_screenshot(driver, f"click_{text}")
                success = True
                break

        if not success:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                text = btn.text.strip().lower()
                if keyword in text:
                    btn.click()
                    time.sleep(2)
                    log_action(f"Clicked on button: {text}")
                    take_screenshot(driver, f"click_{text}")
                    success = True
                    break

        if not success:
            log_action(f"Could not find clickable element for: {keyword}")

    elif command.startswith("search"):
        query = command.replace("search", "").strip()
        try:
            search_box = driver.find_element(By.XPATH, "//input[@type='search' or @name='q' or @type='text']")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            log_action(f"Searched for: {query}")
            take_screenshot(driver, f"search_{query}")
        except:
            log_action("Search box not found.")

    elif command == "exit":
        return False

    else:
        log_action("Unrecognized command. Use: click, go to, search, or exit.")

    return True

def main():
    if os.path.exists("task2_log.txt"):
        os.remove("task2_log.txt")

    url = input("Enter website URL: ").strip()
    if not url.startswith("http"):
        url = "https://" + url

    driver = setup_driver()
    driver.get(url)
    log_action(f"Opened URL: {url}")
    take_screenshot(driver, "homepage")

    while True:
        command = input("Enter command (click/go to/search/exit): ").strip()
        if command.lower() == "exit":
            log_action("Browser closed by user.")
            take_screenshot(driver, "final")
            driver.quit()
            break
        else:
            try:
                keep_running = handle_command(driver, command)
                if not keep_running:
                    break
            except Exception as e:
                log_action(f"Error during command: {e}")

if __name__ == "__main__":
    main()