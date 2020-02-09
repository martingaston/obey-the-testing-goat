from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith returns to the home page and acidentally hits enter on an empty list input

        # The home page refreshes and an error is now displayed saying items cannot be blank

        # She tried again with text for the item, which works

        # She now tries to submit a second blank list item

        # A similar warning as before is displayed on the list page

        # And she corrects the error by submitting a todo with text

        self.fail('write the test!')
