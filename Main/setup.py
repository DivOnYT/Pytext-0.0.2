from setuptools import setup

APP = ['Original_code.py']
DATA_FILES = ['PyText.png','PyText1.png', 'About.txt', 'logo.icns']
OPTIONS = {
 'iconfile':'logo.icns',
 'argv_emulation': True,
 }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
