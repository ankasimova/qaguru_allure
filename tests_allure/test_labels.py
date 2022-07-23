import allure
from allure_commons.types import Severity

def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Создание задачи в репозитории')
    allure.dynamic.story('Авторизованный пользователь может создать задачу в репо')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kasimovaan')
@allure.feature('Создание задачи в репозитории')
@allure.story('Неавторизованный пользователь не может создать задачу в репо')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass