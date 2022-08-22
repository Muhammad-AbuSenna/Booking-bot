# this file will start a new class that will be responsible for holding filtration methods.
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# identifying the parameter (driver) type as a WebDriver in the class below is not necessary for the program execution
# instead it can help the IDE to know the type of the parameter which in turn will help us in auto completing,
# that's why we have imported the above lib (selenium.webdriver.remote.webdriver).

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')

        for star_value in star_values:
            star_option = star_filtration_box.find_element(
                By.CSS_SELECTOR,
                f'div[data-filters-item="class:class={star_value}"]'
            )
            star_option.click()

    def sort_for_lowest_price(self):
        lowest_price = self.driver.find_element(
            By.CSS_SELECTOR,
            'li[data-id="price"]'
        )
        lowest_price.click()
