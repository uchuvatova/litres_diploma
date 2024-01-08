from selene import browser


class ProfilePage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/pages/personal_cabinet_notifications/")
