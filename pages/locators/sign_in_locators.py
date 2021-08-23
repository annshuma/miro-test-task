from selenium.webdriver.common.by import By

class SignInLocators:
    class Buttons:
        SIGN_IN = [By.CSS_SELECTOR, "button[type='submit']"]

    class Inputs:
        EMAIL = (By.CSS_SELECTOR, "#email ")
        PASSWORD = (By.CSS_SELECTOR, "#password")