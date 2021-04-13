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
@pytest.mark.webtest
@pytest.mark.check
def test_send():
    pass  # perform some webtest test for your app




def test_something_quick():
    pass


def test_another():
    pass

class TestClass:
    def test_method(self):
        pass
