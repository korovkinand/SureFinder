import time

from surebet import *
from surebet.loading import Selenium
from surebet.loading.fonbet import load, load_events, name
from surebet.tests.loading import *


def test_loading():
    selenium = Selenium()

    for j in range(2):
        print("load: ({})".format(j))

        load(selenium.browser)
        for i in range(4):
            print("load events: ({})".format(i))

            result = try_load_events(load_events, name, browser=selenium.browser)
            check_result(result)

            time.sleep(1)

        time.sleep(5)

    selenium.quit()
    logging.info("PASS: loading")
