__author__ = 'Nataly'

from model.group import Group
import pytest
from fixture.application import App
import os.path
import json

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def app(request):
    global fixture
    config = load_config(request.config.getoption("--target"))["app"]
    if fixture is None or not fixture.is_valid():
        fixture = App(base_path=config['basePath'])
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")



