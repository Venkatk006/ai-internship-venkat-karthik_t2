This Python script automates interaction with websites using Selenium WebDriver. It accepts text-based commands like "click", "go to", "search", and "exit", performs the actions in a Chrome browser, captures screenshots, and logs all activities.

Features

- Open any URL in Chrome.
- Interact using simple commands:
    - click <link or button text>
    - go to <menu item>
    - search <keywords>
    - exit (to close the session)
- Logs actions to task2_log.txt.
- Saves screenshots for each action.

How to Run

1. Install Selenium:
   pip install selenium

2. Download ChromeDriver:
   - Match your Chrome version from https://chromedriver.chromium.org/downloads
   - Place chromedriver.exe in the script folder or system PATH

3. Run the script:
   python task2_script.py

4. Enter commands like:
   Enter website URL: (https://www.nueverainfotech.com/)
   Enter command: click About
   Enter command: search AI
   Enter command: exit

Outputs

Files are saved in the same directory as the script:

- task2_log.txt
- homepage.png
- click_about.png
- search_ai.png
- final.png
