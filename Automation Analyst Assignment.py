import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the Fitpeo website
driver.get("https://www.fitpeo.com/")
driver.maximize_window()

try:
    # Navigate to the Revenue Calculator page by waiting for the link and clicking it
    webpage = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/revenue-calculator']"))
    )
    webpage.click()  # Click the link to navigate to the page
    print("Navigated to the Revenue Calculator page.")

    # Wait for the slider element to be present and scroll to it
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", target_element)  # Scroll to the slider element
    print("Scrolled to the target slider element.")

    # Use JavaScript to set the slider's value to 820
    slider_input = driver.find_element(By.XPATH, "//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']")
    target_value = 820
    driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", slider_input, target_value)  # Set the slider value to 820

    # Optionally, verify the slider value (this step can be adjusted to your specific needs)
    text = driver.find_element(By.XPATH, "//input[@type='number' and @min='0' and @max='2000']")
    input=560
    text.send_keys("560")  # Set a custom value (can be adjusted)
    slider_input = driver.find_element(By.XPATH, "//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']")
    slider_value = slider_input.get_attribute("aria-valuenow")  # Get the current value of the slider
    print(f"Slider value: {input}")

    # Scroll down further and select the checkboxes for CPT-99091, CPT-99453, CPT-99454, and CPT-99474.
    driver.find_element(By.XPATH, "//span[normalize-space()='57']").click()  # Selecting CPT-99091
    driver.find_element(By.XPATH, "//span[normalize-space()='19.19']").click()  # Selecting CPT-99453
    driver.find_element(By.XPATH, "//span[normalize-space()='63']").click()  # Selecting CPT-99454
    driver.find_element(By.XPATH, "//span[normalize-space()='15']").click()  # Selecting CPT-99474

    # Pause for observation (optional)
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Close the browser
