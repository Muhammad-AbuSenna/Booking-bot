from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DealsReporting:
    def __init__(self, deals_box: WebElement):
        self.deals_box = deals_box
        self.deals = self.pull_deals()

    def pull_deals(self):
        return self.deals_box.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_deals_details(self):

        collection = []
        for deal in self.deals:
            hottel_name = deal.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()

            # hottel_score = deal.find_element(
            #    By.CSS_SELECTOR,
            #    'a[data-testid="review-score-link"]'
            # ).find_element(
            #    By.CSS_SELECTOR,
            #    'div[data-testid="review-score"]'
            # ).find_element(
            #    By.CLASS_NAME,
            #    "d10a6220b4"
            # ).get_attribute('innerHTML').strip()

            hottel_price = deal.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="price-and-discounted-price"]'
            ).find_element(
                By.CSS_SELECTOR,
                'span:last-child'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hottel_name, hottel_price]
            )
        return collection
