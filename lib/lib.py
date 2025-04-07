from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def _wait(fun):
    def _wrapper(*args, **kwargs):
        instance = args[0]
        _locators = args[1]
        print(f"waiting for locator {_locators}")
        w = WebDriverWait(instance.driver, 20)
        w.until(EC.visibility_of_element_located(_locators))
        return fun(*args, **kwargs)

    return _wrapper


class Wrapper:
    def __init__(self, driver):
        self.driver = driver

    @_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @_wait
    def enter_text(self,locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait
    def mouse_hover(self, locator):
        action = ActionChains(self.driver)
        mouse = self.driver.find_element(*locator)
        action.move_to_element(mouse).perform()

    # @_wait
    def browser_back(self):
        self.driver.back()


    def is_displayed(self, locator):
        self.driver.find_element(*locator).is_displayed()

    @_wait
    def select_element(self, locator, *, value):
        element = self.driver.find_element(*locator)
        dropdown = Select(element)
        dropdown.select_by_visible_text(value)


