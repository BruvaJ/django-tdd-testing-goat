from django.test import TestCase

# Create your tests here.

# to check this is getting run
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
