from selene.support.conditions import be, have
from selene.support.shared import browser


class ProfilePage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/pages/personal_cabinet_notifications/")
