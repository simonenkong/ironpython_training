__author__ = 'Nataly'

from model.group import Group

import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys

sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *
import time

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_editor(self):
        main_window = self.app.main_window
        main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = main_window.ModalWindow("Group editor")
        return modal

    def close_group_editor(self):
        main_window = self.app.main_window
        modal = main_window.ModalWindow("Group editor")
        modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    def add_new_group(self, group):
        modal = self.open_group_editor()
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(group.name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor()

    def delete_group(self, group):
        modal = self.open_group_editor()
        modal.Get(SearchCriteria.ByText(group.name)).Click()
        modal.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
        deletemodal = modal.ModalWindow("Delete group")
        deletemodal.Get(SearchCriteria.ByAutomationId("uxDeleteAllRadioButton")).Click()
        time.sleep(2)
        deletemodal.Get(SearchCriteria.ByText("OK")).Click()
        time.sleep(2)
        self.close_group_editor()

    def get_group_list(self):
        modal = self.open_group_editor()
        tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        l = [Group(node.Text) for node in root.Nodes]
        self.close_group_editor()
        return l
