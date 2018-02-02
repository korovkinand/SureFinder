import subprocess

from pyvirtualdisplay import Display
from selenium import webdriver


class Selenium:
    def __init__(self, implicit_wait=60) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(implicit_wait)

    def quit(self):
        self.browser.quit()


class SeleniumService:
    _pool = []
    _display = Display(visible=0, size=(1920, 1080))

    def __init__(self):
        if not SeleniumService._pool:
            # kill Chrome at program launch
            subprocess.run(['killall', '-s', '9', 'Xvfb'])
            subprocess.run(['killall', '-s', '9', 'chromedriver'])

            # TODO: remove old files

            SeleniumService._display.start()

    @staticmethod
    def new_instance():
        SeleniumService._pool.append(Selenium())
        return SeleniumService._pool[-1]

    @staticmethod
    def quit():
        for instance in SeleniumService._pool:
            instance.quit()
        SeleniumService._pool.clear()
        SeleniumService._display.stop()
