#!/usr/bin/env python
# encoding: utf-8

import unittest
from .test import TestCase, Spy
from . import *


class TestSDK(TestCase):
    def test_instance(self):
        sdk = SDK('whatever', 'whatever', 'https://whatever')
        self.assertEqual(sdk.get_platform().api_url('/foo', add_server=True), 'https://whatever/restapi/v1.0/foo')


if __name__ == '__main__':
    unittest.main()