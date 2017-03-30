import apiritif


class TestRequests(apiritif.APITestCase):
    def setUp(self):
        super(TestRequests, self).setUp()
        self.keep_alive = True
        
    def test_assert_regex(self):
        self.get('http://blazedemo.com/', timeout=30.0, allow_redirects=True)
        self.assertOk()
        self.assertStatusCode(200)
        self.assertRegexInBody('Welcome to the Simple Travel Agency!')
        
    def test_assert_xpath(self):
        self.get('http://blazedemo.com/', timeout=30.0, allow_redirects=True)
        self.assertOk()
        self.assertXPath('//head/title', parser_type='html', validate=False)
        
    def test_assert_jsonpath(self):
        self.get('https://api.github.com/users/linus',
                 headers={'user-agent': 'biggie/smalls'}, timeout=30.0, allow_redirects=True)
        self.assertOk()
        self.assertJSONPath('$.name', expected_value='Linus Gustav Larsson Thiel')
