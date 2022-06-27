def assert_page_title(test_self, page_url, expected_title):
    title = get_page_title(test_self, page_url)
    test_self.assertEqual(expected_title, title, f'Expected title differ then actual for page {test_self.driver.current_url}')


def get_page_title(test_self, page_url: str):
    driver = test_self.driver
    driver.get(page_url)
    return driver.title
