# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

""" Allow to highlight code lines """
import os

from flask import send_from_directory
from inginious.frontend.pages.utils import INGIniousPage
from inginious.frontend.task_problems import DisplayableCodeProblem

__version__ = "0.1.dev0"
PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))
AUTHORIZED_COLORS = ["default", "blue", "darkblue", "red", "darkred", "green", "darkgreen", "yellow", "orange"]


class StaticMockPage(INGIniousPage):
    def GET(self, path):
        return send_from_directory(os.path.join(PATH_TO_PLUGIN, "static"), path)

    def POST(self, path):
        return self.GET(path)


def parse_highlight_entry(sidx, entry):
    if isinstance(entry, list):
        lines = entry
        color = "default"
    elif isinstance(entry, int):
        lines = [entry]
        color = "default"
    elif isinstance(entry, dict):
        lines = entry["lines"]
        color = entry["color"]
    else:
        raise Exception("Invalid")

    if color not in AUTHORIZED_COLORS:
        color = "default"

    return [(sidx, l, color) for l in lines]


def add_feedback_script(task, submission):
    if "custom" not in submission or "highlight" not in submission["custom"]:
        return
    todo = []
    error = False

    subproblems = set(x.get_id() for x in task.get_problems() if isinstance(x, DisplayableCodeProblem))

    for sidx, d in submission["custom"]["highlight"].items():
        if sidx in subproblems:
            try:
                if isinstance(d, int):
                    todo.append((sidx, d, "default"))
                elif isinstance(d, list):
                    for entry in d:
                        todo += parse_highlight_entry(sidx, entry)
                else:
                    todo += parse_highlight_entry(sidx, d)
            except:
                # badly formatted input, ignore
                error = True

    out =  "\n".join(["codeEditors['{}'].addLineClass({}, 'background', 'ph-{}');".format(sidx, line, color) for sidx, line, color in todo])
    return "clear_highlight();\n" + out + (";\n console.log(\"Invalid format for the highlight plugin.\");" if error else "")


def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    plugin_manager.add_page('/plugins/highlight/static/<path:path>', StaticMockPage.as_view("highlightstaticpage"))
    plugin_manager.add_hook("feedback_script", add_feedback_script)
    plugin_manager.add_hook("css", lambda: "/plugins/highlight/static/highlight.css")
    plugin_manager.add_hook("javascript_header", lambda: "/plugins/highlight/static/highlight.js")
