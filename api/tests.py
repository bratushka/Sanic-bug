#!/usr/bin/env python
import socket
import time
import unittest

import main


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Wait for the DB to start accepting connections"""
        while True:
            try:
                soc = socket.create_connection(('sanic-bug-db', 5432))
                soc.close()
                break
            except ConnectionRefusedError:
                time.sleep(.1)

    def test_1(self):
        """This runs fine"""
        main.app.test_client.get('/')

    def test_2(self):
        """This fails"""
        main.app.test_client.get('/')


if __name__ == '__main__':
    unittest.main()
