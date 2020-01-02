from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_unittest_is_working(self):
        self.assertTrue(15 % 3 == 0)

    def test_can_start_a_list_and_retreive_it_later(self):
        # Edith has heard of a cool new online todo application. She visits the homepage.
        self.browser.get(self.live_server_url)
        header_text = self.browser.find_element_by_tag_name('h1').text

        # She can see the page title and header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.assertIn('To-Do', header_text)

        # She can enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types 'buy peacock feathers' into a text box
        inputbox.send_keys("Buy peacock feathers")

        # When she hits 'Enter' the page updates and now '#1: Buy peacock feathers' appears as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # There is still a text box where she can enter another item. She inputs 'use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and both items are in the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Edith wonders if the site will remember her list, and notices a unique URL has been generated for her. There is text that explains this.
        self.fail("Finish the test!")

        # She visits her unique URL - her list is still there.

