import pytest
import allure

@allure.feature("All Login Users")
@allure.title('All user login')
@allure.description('Checking all the user are login successfully or not')
@allure.suite("LOGIN")
@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


@allure.feature("check")
@allure.title('check')
@allure.description('check successfully or not')
@allure.suite("check")
@pytest.mark.check
def test_send():
    with allure.step(allure_Step):
                allure.attach(self.driver.get_screenshot_as_png(), name=allure_screenshot_name,
                              attachment_type=AttachmentType.PNG)
    pass  # perform some webtest test for your app




def test_something_quick():
    pass


def test_another():
    pass

class TestClass:
    def test_method(self):
        pass
