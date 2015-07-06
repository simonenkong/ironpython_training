__author__ = 'Nataly'

from fixture.group import GroupHelper

import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *


class App:

    def __init__(self, base_path):
        self.application = Application.Launch(base_path)
        self.group = GroupHelper(self)
        self.main_window = self.application.GetWindow("Free Address Book")

    def is_valid(self):
        return self.main_window is None

    def destroy(self):
        self.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()

