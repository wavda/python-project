import unittest
from appium import webdriver
from calc import CalcPage
from selenium.webdriver.common.action_chains import ActionChains


class CalcTest(unittest.TestCase):
    appSession = None
    calcResult = None
    c = None
    move = None

    def setUp(self):
        capabilities = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
        self.appSession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=capabilities
        )
        self.c = CalcPage.CalcPage(self.appSession)
        self.move = ActionChains(self.appSession)

    def tearDown(self):
        self.appSession.quit()

    def test_add(self):
        self.c.six().click()
        self.c.plus().click()
        self.c.two().click()
        self.c.equals().click()
        self.assertEqual(self.c.get_display_result(), 6 + 2)

    def test_subtraction(self):
        self.c.six().click()
        self.c.minus().click()
        self.c.two().click()
        self.c.equals().click()
        self.assertEqual(self.c.get_display_result(), 6 - 2)

    def test_division(self):
        self.c.six().click()
        self.c.divide_by().click()
        self.c.two().click()
        self.c.equals().click()
        self.assertEqual(self.c.get_display_result(), 6 / 2)

    def test_multiplication(self):
        self.c.six().click()
        self.c.multiply_by().click()
        self.c.two().click()
        self.c.equals().click()
        self.assertEqual(self.c.get_display_result(), 6 * 2)

    def test_chooseCalculator(self):
        self.c.choose_calculator("Scientific")

    def test_move_calculator(self):
        self.move.click_and_hold(self.c.app_name).move_by_offset(50, 50).perform()
        self.move.click_and_hold(self.c.app_name).move_by_offset(-50, -50).perform()
        self.move.context_click(self.c.app_name)
