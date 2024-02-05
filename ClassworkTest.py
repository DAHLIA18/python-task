import unittest








def test_list_length(list):
    expectedlength = len(list)
    actuallength = list_length(list)
    assert actuallength == expectedlength




class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
