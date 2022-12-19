import unittest
from appium import webdriver
from notepad import NotepadPage
from selenium.webdriver.common.keys import Keys


class NotepadTest(unittest.TestCase):
    appSession = None
    calcResult = None

    def setUp(self):
        capabilities = {"app": "C:\\Windows\\System32\\notepad.exe"}
        self.appSession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=capabilities
        )

    def tearDown(self):
        self.appSession.quit()

    def test_notepad(self):
        np = NotepadPage.NotepadPage(self.appSession)
        np.text_area().send_keys("Hello World!")
        np.text_area().send_keys(Keys.ALT, Keys.F4)
        np.dialog_cancel().click()
        np.text_area().send_keys(Keys.ALT, Keys.F4)
        np.dialog_dont_save().click()
