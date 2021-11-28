import unittest 
import vimlinks as vl

class TestStringMethods(unittest.TestCase):
  def test_get_url1(self):
    self.assertEqual(vl.get_url(["abc","def"]), "https://duckduckgo.com/?q=abc+def")

  def test_get_url2(self):
    self.assertEqual(vl.get_url(["what", "is grass"]), "https://duckduckgo.com/?q=what+is+grass")

  def test_get_url3(self):
    self.assertEqual(vl.get_url(["ftps://", "abc","def"]), "ftps://")

if __name__ == '__main__':
  unittest.main()

