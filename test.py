from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Twitter credentials (for demo purposes)
username = "tinnicumBucks"
password = "wijnyq-1pyXso-gawrun"

# Set up WebDriver
driver = webdriver.Chrome()

# Open X (Twitter) login page
driver.get("https://twitter.com/login")
time.sleep(3)  # Allow the page to fully load

# Locate the username field and input the username
username_input = driver.find_element(By.NAME, "text")
username_input.send_keys(username)
time.sleep(1)

# Click 'Next' button
next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
next_button.click()
time.sleep(2)

# Now, locate the password field after username is submitted
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Allow time for login to process

# Go to the tweet compose page
driver.get("https://twitter.com/compose/tweet")
time.sleep(3)

# Find the tweet text box and simulate typing out the tweet message
tweet_box = driver.find_element(By.XPATH, "//div[@data-offset-key]")
tweet_message = "Don't miss the upcoming township meeting! Details here: https://tinicumtownship.org/events/"

for char in tweet_message:
    tweet_box.send_keys(char)  # Simulate typing each character one by one
    time.sleep(0.05)  # Adjust typing speed if necessary

# Find the "Post" button using the data-testid attribute
post_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='tweetButton']")

# Click the "Post" button to send the tweet
post_button.click()

print("Township meeting tweet posted successfully!")
time.sleep(5)

# Close the browser
driver.quit()

