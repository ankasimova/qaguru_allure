import allure
from allure import attachment_type
import json

def test_attachments():
    allure.attach('Text content', name='Text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>Hello, World!</h1>', name='Html', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="JSON", attachment_type=attachment_type.JSON)