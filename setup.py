from setuptools import setup

setup(
    name="selenium_appium_alerts",
    version="0.1",
    description="Une bibliothèque pour les alertes de tests Selenium et Appium",
    url="https://github.com/EliteWise/selenium_appium_alerts",
    author="Elite",
    author_email="florent.mogenet@gmail.com",
    license="MIT",
    packages=["selenium_appium_alerts"],
    install_requires=[
        "selenium",
        "appium-python-client",
        "pymsteams"
    ],
    zip_safe=False
)