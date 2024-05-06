from django.shortcuts import make_toast
from django.test import simpleTestCase

class MakeToastTests(SimpleTestCase):
  def test_make_toast(self):

    self.assertEqual(make_toast(),"toast")
