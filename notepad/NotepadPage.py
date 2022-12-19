class NotepadPage():
    def __init__(self, driver):
        self.driver = driver

    def text_area(self):
        return self.driver.find_element_by_class_name("RichEditD2DPT")

    def dialog_dont_save(self):
        return self.driver.find_element_by_name("Don't save")

    def dialog_cancel(self):
        return self.driver.find_element_by_name("Cancel")
