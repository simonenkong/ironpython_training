__author__ = 'Nataly'
from model.group import Group
import random


def test_del_group(app):
    if len(app.group.get_group_list()) == 1:
        app.group.add_new_group(Group("not enough groups"))
    old_list = app.group.get_group_list()
    group = random.choice(old_list)
    app.group.delete_group(group)
    new_list = app.group.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)