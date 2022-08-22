from logging import exception
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filterations import BookingFiltration
from booking.deals_reporting import DealsReporting
from prettytable import PrettyTable

import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        # adding the WebDriver to the Windows environment PATH variables.
        os.environ['PATH'] += driver_path

        # these options are to ignore the warnings showing up when executing the file from cmd.
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def select_currency(self, currency=None):
        currency_btn = self.find_element(
            By.CSS_SELECTOR, 'button[data-modal-aria-label="Select your currency"]')
        currency_btn.click()
        currency_type = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        currency_type.click()

    def select_destination(self, place=None):
        srch_place = self.find_element(By.ID, "ss")
        srch_place.clear()
        srch_place.send_keys(place)
        srch_list_select = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        srch_list_select.click()

    def select_dates(self, check_in_date, check_out_date):

        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def adults_select(self, count=1):
        guests_box = self.find_element(By.ID, "xp__guests__toggle")
        guests_box.click()

        while True:
            existing_adults_count = self.find_element(
                By.ID, "group_adults").get_attribute('value')

            if int(existing_adults_count) == 1:
                break

            decrease_adults_count = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_count.click()

        # the _ sign is replace to identifying a variable like 'i' when I won't use it
        for _ in range(count - 1):
            increase_adults_count = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Increase number of Adults"]'
            )
            increase_adults_count.click()

    def start_search(self):
        search_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_btn.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        # filtration.sort_for_lowest_price()  not reliable rightnow, the UI has chenged, I'm to lazy to edit the selector :D .
        filtration.select_star_rating(4, 5)

    def reporting_results(self):
        results_box = self.find_element(By.ID, "search_results_table")
        report = DealsReporting(results_box)

        result_table = PrettyTable(
            field_names=["Hottel_Name", "Price"]
        )
        result_table.add_rows(report.pull_deals_details())
        print(result_table)
