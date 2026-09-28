Selenium Web Automation Testing with Python

This project demonstrates web automation testing using Python and Selenium WebDriver on the Test Automation Practice website. The main objective of this project is to automate user interactions with different web elements and validate the basic functionality of a web form.

The automation script launches the Chrome browser, navigates to the practice website, and enters dynamically generated test data into multiple input fields. Random data is generated for fields such as name, email, phone number, and address, which helps simulate different test scenarios during every execution.

The project covers automation of various types of web elements, including text boxes, radio buttons, checkboxes, dropdown menus, color selection, and date fields. Selenium's "Select" class is used to interact with dropdown elements, while "WebDriverWait" and Expected Conditions are used to wait for elements before performing actions.

Exception handling is implemented using Python's try-except-finally structure. This helps handle unexpected errors during test execution and ensures that the browser is closed properly after the test, whether the execution passes or fails.

Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- Python Random Module

Key Concepts Practiced

- WebDriver initialization
- Locating elements using ID and XPath
- Explicit waits
- Sending data using "send_keys()"
- Clicking radio buttons and checkboxes
- Handling dropdowns using "Select"
- Generating random test data
- Exception handling
- Browser automation
- Proper cleanup using "finally"

This project is part of my QA Automation Testing learning journey and helped me gain practical experience with Selenium WebDriver and Python. It demonstrates how repetitive manual form-filling activities can be automated and provides a foundation for developing more advanced automation frameworks using PyTest, Page Object Model (POM), test reports, screenshots, and data-driven testing.
