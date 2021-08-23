from base_page.base_page import BasePage
from pages.locators import SignInLocators


class SignInPage(BasePage):

    def sign_in(self, email: str, password: str) -> None:
        self._set_email(email)
        self._set_password(password)
        self._click_on_sign_in_button()

    def _set_email(self, email: str) -> None:
        self._input(SignInLocators.Inputs.EMAIL, email)

    def _set_password(self, password: str) -> None:
        self._input(SignInLocators.Inputs.PASSWORD, password)

    def _click_on_sign_in_button(self) -> None:
        self._click(SignInLocators.Buttons.SIGN_IN)
