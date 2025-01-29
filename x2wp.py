# working as intended, but the error is from Whatsapp Web page, not loading Channels correctly

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time
import os

# Chrome options to avoid detection as automation tool
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:\Users\ghazayel\AppData\Local\Google\Chrome\User Data")  
chrome_options.add_argument("--profile-directory=Profile 1")  
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Optional: Fix decryption issue
chrome_options.add_argument("--password-store=basic")  

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
except Exception as e:
    print(f"🚨 WebDriver failed to start: {e}")
    exit()

# File to store the last sent tweet content
last_sent_file = 'last_sent_tweet.txt'

# Function to read the last sent tweet content from a file
def read_last_sent_tweet():
    if os.path.exists(last_sent_file):
        with open(last_sent_file, 'r', encoding='utf-8') as file:
            return file.read().strip()
    return None

# Function to write the latest tweet content to a file
def write_last_sent_tweet(content):
    with open(last_sent_file, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to remove specific words or characters from a tweet
def remove_word(sentence, word_to_remove):
    updated_sentence = sentence.replace(word_to_remove, '')  # Replace word with empty string
    return ' '.join(updated_sentence.split())  # Remove extra spaces

# Function to fetch the latest tweet from the X (formerly Twitter) profile
def get_latest_tweet():
    driver.get("https://x.com/ghazayel")
    try:
        tweet = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article div[lang]"))
        ).text
        return tweet
    except Exception as e:
        print(f"❌ Error fetching tweet: {e}")
        driver.save_screenshot("get_latest_tweet_error.png")  # Take screenshot on failure
        return None

import time

def send_via_whatsapp(message):
    driver.get("https://web.whatsapp.com/")

    try:
        # Wait for the "Channels" tab to be clickable and click it
        channels_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Channels" or @data-icon="newsletter-outline"]'))
        )
        channels_button.click()

        # Wait for the search box to appear and type the channel name
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
        )
        print("Search box found.")
        search_box.click()
        search_box.send_keys("soubasouba" + Keys.ENTER)

        # Wait for the result containing 'soubasouba' to appear and click it
        # Ensure that the result containing the 'soubasouba' channel is clickable
        channel_result = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='soubasouba']//ancestor::div[@role='button']"))
        )
        print("Channel result found.")
        
        # Scroll the element into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", channel_result)
        channel_result.click()

        # Wait for the message input box (Type an update) and send the message
        message_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']"))
        )
        print("Message box found.")
        
        # Directly interact with the message box
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)

        print('✅ Message sent successfully!')

        # Wait for 5 seconds before closing the tab/browser
        time.sleep(5)

    except Exception as e:
        print(f"❌ Failed to send message: {e}")
        driver.save_screenshot("send_via_whatsapp_error.png")  # Take screenshot on failure

#Function to READ TWEET
def main():
    previous_tweet = read_last_sent_tweet()

    # Get latest tweet
    latest_tweet = get_latest_tweet()

    if latest_tweet and latest_tweet != previous_tweet:
        # Process tweet to remove specific words and characters
        sentence = latest_tweet
        word_to_remove = ['عاجل |','عاجل|']

        if word_to_remove[0] in sentence:
            new_tweet_content = remove_word(sentence, word_to_remove[0])
        elif word_to_remove[1] in sentence:
            new_tweet_content = remove_word(sentence, word_to_remove[1])
        else:
            new_tweet_content = sentence

        new_tweet_content = new_tweet_content.replace('_',' ').replace('#','')  # Remove underscores and hashtags
        
        # Logging the tweet content
        print(f"Original tweet: {latest_tweet}")
        print(f"Processed tweet: {new_tweet_content}")

        # Send the tweet via WhatsApp
        send_via_whatsapp(new_tweet_content)

        # Update the last sent tweet in the file
        write_last_sent_tweet(latest_tweet)

    else:
        print("🔄 No new tweet found or tweet already sent.")

    driver.quit()

if __name__ == "__main__":
    main()
