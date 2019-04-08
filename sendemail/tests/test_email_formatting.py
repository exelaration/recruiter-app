from django.test import TestCase

from sendemail.views import format_list_string


class FormatListStringTest(TestCase):
    def setUp(self):
        pass

    # Test default settings
    def test_format_list_string_no_item(self):
        items = []
        output = format_list_string(items)
        self.assertEquals(output, '')

    def test_format_list_string_one_item(self):
        items = ['one']
        output = format_list_string(items)
        self.assertEquals(output, 'one')

    def test_format_list_string_two_items(self):
        items = ['one', 'two']
        output = format_list_string(items)
        self.assertEquals(output, 'one, two')

    def test_format_list_string_three_items(self):
        items = ['one', 'two', 'three']
        output = format_list_string(items)
        self.assertEquals(output, 'one, two, three')

    # Test separator
    def test_format_list_string_many_items(self):
        items = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        output = format_list_string(items, separator='-')
        self.assertEquals(output, 'one-two-three-four-five-six-seven')

    # Test correct separator is used
    def test_format_list_string_two_items_uses_correct_separator(self):
        items = ['one', 'two']
        output = format_list_string(items, separator=' ... ', separator_2_items=' and ', last_separator=', and ')
        self.assertEquals(output, 'one and two')

    def test_format_list_string_three_items_uses_correct_separators(self):
        items = ['one', 'two', 'three']
        output = format_list_string(items, separator=' ... ', separator_2_items=' and ', last_separator=', and ')
        self.assertEquals(output, 'one ... two, and three')

    def test_format_list_string_many_items_uses_correct_separators(self):
        items = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        output = format_list_string(items, separator='-', last_separator=' and ')
        self.assertEquals(output, 'one-two-three-four-five-six and seven')

    # Test prefix is used
    def test_format_list_string_no_items_uses_prefix(self):
        items = []
        output = format_list_string(items, prefix='<', separator='-')
        self.assertEquals(output, '<')

    def test_format_list_string_one_item_uses_prefix(self):
        items = ['one']
        output = format_list_string(items, prefix='<', separator='-')
        self.assertEquals(output, '<one')

    def test_format_list_string_two_items_uses_prefix(self):
        items = ['one', 'two']
        output = format_list_string(items, prefix='<', separator='-')
        self.assertEquals(output, '<one-two')

    def test_format_list_string_three_items_uses_prefix(self):
        items = ['one', 'two', 'three']
        output = format_list_string(items, prefix='<', separator='-')
        self.assertEquals(output, '<one-two-three')

    def test_format_list_string_many_items_uses_prefix(self):
        items = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        output = format_list_string(items, prefix='<', separator='-')
        self.assertEquals(output, '<one-two-three-four-five-six-seven')

    # Test postfix is used
    def test_format_list_string_no_items_uses_postfix(self):
        items = []
        output = format_list_string(items, separator='-', postfix='/>')
        self.assertEquals(output, '/>')

    def test_format_list_string_one_item_uses_postfix(self):
        items = ['one']
        output = format_list_string(items, separator='-', postfix='/>')
        self.assertEquals(output, 'one/>')

    def test_format_list_string_two_items_uses_postfix(self):
        items = ['one', 'two']
        output = format_list_string(items, separator='-', postfix='/>')
        self.assertEquals(output, 'one-two/>')

    def test_format_list_string_three_items_uses_postfix(self):
        items = ['one', 'two', 'three']
        output = format_list_string(items, separator='-', postfix='/>')
        self.assertEquals(output, 'one-two-three/>')

    def test_format_list_string_many_items_uses_postfix(self):
        items = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        output = format_list_string(items, separator='-', postfix='/>')
        self.assertEquals(output, 'one-two-three-four-five-six-seven/>')

    # Test prefix-postfix order
    def test_format_list_string_no_items_uses_pre_and_postfix(self):
        items = []
        output = format_list_string(items, prefix='<', separator='-', postfix='/>')
        self.assertEquals(output, '</>')
