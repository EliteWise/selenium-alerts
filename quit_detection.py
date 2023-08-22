from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from teams_request import ConnectorCard


class MyEventListener(AbstractEventListener):
    def __init__(self, active=False):
        self.active = active

    # Listen to `driver.quit()` event
    def before_quit(self, driver):
        if self.active:
            myTeamsMessage = ConnectorCard("MSTEAMS_WEBHOOK")
            myTeamsMessage.text("msg")
            myTeamsMessage.send()


# Init Decorator
def activate_listener(driver):
    def decorator(func):
        def wrapper(*args, **kwargs):
            event_driver = EventFiringWebDriver(driver, MyEventListener(active=True))
            result = func(event_driver, *args, **kwargs)
            return result
        return wrapper
    return decorator