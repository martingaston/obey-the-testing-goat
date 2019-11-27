from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_unittest_is_working(self):
        self.assertTrue(15 % 3 == 0)

    def test_can_start_a_list_and_retreive_it_later(self):
        # Edith has heard of a cool new online todo application. She visits the homepage.
        self.browser.get('http://localhost:8000')

        # She can see the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # She can enter a to-do item straight away

        # She types 'buy peacock feathers' into a text box

        # When she hits 'Enter' the page updates and now '#1: Buy peacock feathers' appears as an item in the to-do list

        # There is still a text box where she can enter another item. She inputs 'use peacock feathers to make a fly'

        # The page updates again and both items are in the list

        # Edith wonders if the site will remember her list, and notices a unique URL has been generated for her. There is text that explains this.

        # She visits her unique URL - her list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
