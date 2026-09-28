# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random
# import string
# import time
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
#
# try:
#     driver.maximize_window()
#
#     driver.get("https://testautomationpractice.blogspot.com/?m=1")
#
#     # Generate random data
#     name = "TestUser" + str(random.randint(1000, 9999))
#     email = "test" + str(random.randint(1000, 9999)) + "@example.com"
#     phone = "9" + "".join(random.choices(string.digits, k=9))
#     address = str(random.randint(1, 999)) + ", Test Street"
#
#     # Enter name
#     wait.until(
#         EC.visibility_of_element_located((By.ID, "name"))
#     ).send_keys(name)
#
#     # Enter email
#     driver.find_element(By.ID, "email").send_keys(email)
#
#     # Enter phone
#     driver.find_element(By.ID, "phone").send_keys(phone)
#
#     # Enter address
#     driver.find_element(By.ID, "textarea").send_keys(address)
#
#     # Select gender
#     driver.find_element(By.ID, "male").click()
#
#     # Select days
#     driver.find_element(By.ID, "monday").click()
#     driver.find_element(By.ID, "wednesday").click()
#     driver.find_element(By.ID, "friday").click()
#
#     print("Form filled successfully")
#     print("Name:", name)
#     print("Email:", email)
#     print("Phone:", phone)
#
# except Exception as e:
#     print("Test failed!")
#     print("Error:", e)
#
# finally:
#     time.sleep(3)
#     driver.quit()
#     print("Browser closed")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import string
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/?m=1")

    # -------------------------
    # Generate random data
    # -------------------------
    first_names = ["Vignesh", "Rahul", "Arun", "Kiran", "Rohit"]
    last_names = ["Kumar", "Sharma", "Reddy", "Patel", "Singh"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    email = (
        first_name.lower()
        + str(random.randint(1000, 9999))
        + "@example.com"
    )

    phone = "9" + "".join(
        random.choices(string.digits, k=9)
    )

    address = (
        str(random.randint(1, 999))
        + ", Test Automation Street, Bangalore"
    )

    # -------------------------
    # Text fields
    # -------------------------

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "name")
        )
    ).send_keys(first_name + " " + last_name)

    driver.find_element(
        By.ID, "email"
    ).send_keys(email)

    driver.find_element(
        By.ID, "phone"
    ).send_keys(phone)

    driver.find_element(
        By.ID, "textarea"
    ).send_keys(address)

    # -------------------------
    # Gender
    # -------------------------

    driver.find_element(
        By.ID, "male"
    ).click()

    # -------------------------
    # Days
    # -------------------------

    driver.find_element(
        By.ID, "monday"
    ).click()

    driver.find_element(
        By.ID, "wednesday"
    ).click()

    driver.find_element(
        By.ID, "friday"
    ).click()

    # -------------------------
    # Country dropdown
    # -------------------------

    country = Select(
        driver.find_element(By.ID, "country")
    )

    country.select_by_visible_text("India")

    # -------------------------
    # Colors
    # -------------------------

    colors = Select(
        driver.find_element(By.ID, "colors")
    )

    colors.select_by_visible_text("Red")

    # -------------------------
    # Date
    # -------------------------

    date_field = driver.find_element(
        By.ID, "datepicker"
    )

    date_field.send_keys("09/28/2026")

    # -------------------------
    # Print entered data
    # -------------------------

    print("\n========== TEST DATA ==========")
    print("Name    :", first_name, last_name)
    print("Email   :", email)
    print("Phone   :", phone)
    print("Address :", address)
    print("Gender  : Male")
    print("Days    : Monday, Wednesday, Friday")
    print("Country : India")
    print("Color   : Red")
    print("Date    : 09/28/2026")
    print("===============================\n")

    print("All fields entered successfully!")

except Exception as e:
    print("Test execution failed!")
    print("Error:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("Browser closed.")
