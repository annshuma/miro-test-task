from typing import Tuple, Union

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def __element(self, selector: Tuple[By, str]) -> WebElement:
        return self.driver.find_element(*selector)

    def _click(self, selector: Tuple[By, str]) -> None:
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector: Tuple[By, str], value: Union[int, str]) -> None:
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector: Tuple[By, str], timeout: int = 10) -> Union[WebElement, bool]:
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of(self.__element(selector)))
        except(NoSuchElementException, TimeoutException):
            return False

    def _get_element_text(self, selector: Tuple[By, str]) -> str:
        element = self._wait_for_visible(selector)
        if isinstance(element, WebElement):
            return element.text
        else:
            raise TypeError()

    def _get_attribute(self, selector: Tuple[By, str], attribute: str) -> str:
        return self.__element(selector).get_attribute(attribute)

    def _get_css_attribute_(self, selector: Tuple[By, str], prop: str) -> str:
        return self.__element(selector).value_of_css_property(prop)
