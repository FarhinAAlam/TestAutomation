import  unittest

def add(a, b):
    return a + b
class DemoTest(unittest.TestCase):
    def test_add_positive(self):

     self.assertEqual(add(10, 5),15)


     if   __name__ == '__main__':

         var = unittest.main

