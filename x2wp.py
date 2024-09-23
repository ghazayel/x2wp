from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time
import os

# Define the path to your Chrome user data directory and the profile name
user_data_dir = '/path/to/your/chrome/user/data'
profile_dir = 'Profile 2'

# Define Chrome options with the user data directory and profile directory
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_dir}")

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

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

# remove specific word from sentence # updated by Roham in 2024-09-19
def remove_word(sentence, word_to_remove):
    # Replace the small sentence (phrase) with an empty string
    updated_sentence = sentence.replace(word_to_remove, '')

    # Remove extra spaces that might result from the removal
    return ' '.join(updated_sentence.split())
    return updated_sentence


while True:
    try:
        # Open the X.com (formerly Twitter) profile page of 20fourMedia
        driver.get('https://x.com/ghazayel')

        # Wait for the page to load completely (adjust sleep time as needed)
        time.sleep(7)

        # Find the newest tweet on the page (XPath may need to be adjusted depending on the structure of the page)
        newest_tweet = driver.find_element(By.XPATH, '//article[1]//div[@lang]')

        # Extract the text content of the tweet
        tweet_content = newest_tweet.text
        print(f"Latest Tweet: {tweet_content}")

        # Check if the tweet content is the same as the last sent tweet
        last_sent_tweet = read_last_sent_tweet()
        if tweet_content == last_sent_tweet:
            print("Tweet already sent. Waiting for the next check...")
        else:
            # updated by Roham in 2024-09-19
            sentence  = tweet_content
            word_to_remove = ['عاجل |','عاجل|']

            if (word_to_remove[0]) in sentence:
                new_tweet_content = remove_word(sentence, word_to_remove[0])

            elif (word_to_remove[1]) in sentence:
                new_tweet_content = remove_word(sentence, word_to_remove[1])

            else:
                new_tweet_content = sentence
            new_tweet_content = new_tweet_content.replace('_',' ').replace('#','')
            #tweet_content = new_tweet_content
            print(new_tweet_content)
            # end of updatesa

            # Open the WhatsApp channel
            whatsapp_channel_url = ' https://web.whatsapp.com/accept?channel_invite_code=XXXdummyaccount'
            driver.get(whatsapp_channel_url)
            # dummy account is used to divert pressing "x" of close before publishing content
            
            # Wait for the WhatsApp Web channel to load
            time.sleep(10)
            whatsapp_channel_url = 'https://web.whatsapp.com/accept?channel_invite_code=XXXXXintendedchannel'
            driver.get(whatsapp_channel_url)

            # Wait for the WhatsApp Web channel to load
            time.sleep(15)

            # Find the message input box and send the tweet content
            input_box = driver.find_element(By.XPATH, '//div[@aria-placeholder="Type an update" and @role="textbox"]')
            input_box.send_keys(new_tweet_content)

            # Simulate pressing Enter to send the message
            input_box.send_keys(Keys.RETURN)

            # Update the last sent tweet content in the file
            write_last_sent_tweet(tweet_content)

            print("Tweet sent successfully!")
            print("Original tweet :", tweet_content)
            print("Updated tweet sent :", new_tweet_content)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for 2 minutes before running the script again
    time.sleep(120)
