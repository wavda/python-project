class CalcPage():
    def __init__(self, driver):
        self.driver = driver

    def app_name(self):
        return self.driver.find_element_by_accessibility_id("AppName")

    def two(self):
        return self.driver.find_element_by_name("Two")

    def six(self):
        return self.driver.find_element_by_name("Six")

    def equals(self):
        return self.driver.find_element_by_name("Equals")

    def minus(self):
        return self.driver.find_element_by_name("Minus")

    def plus(self):
        return self.driver.find_element_by_name("Plus")

    def divide_by(self):
        return self.driver.find_element_by_name("Divide by")

    def multiply_by(self):
        return self.driver.find_element_by_name("Multiply by")

    def get_display_result(self):
        text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        text = text.strip("Display is ").rstrip(' ').lstrip(' ')
        return int(text)

    def choose_calculator(self, locator):
        self.driver.find_element_by_accessibility_id("TogglePaneButton").click()
        list_element = self.driver.find_elements_by_xpath("//ListItem")
        for element in list_element:
            if element.get_attribute("AutomationId") == locator:
                element.click()
                break
