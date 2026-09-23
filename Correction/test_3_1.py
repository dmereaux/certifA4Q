import os,logging
import time

def test_3_1():

    logging.debug("running test_3_1")
    assert time.localtime().tm_hour  >  7
