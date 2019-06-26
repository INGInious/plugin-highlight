# INGInious-highlight-plugin
A plugin that allows highlighting lines in "code" problems

Installation
------------

Install the plugin via pip:
```
pip install git+https://github.com/UCL-INGI/INGInious-highlight-plugin.git
```

Then add the plugin in your configuration.yaml
```
plugins:
- plugin_module: inginious_highlight
```

Usage
-----

Inside your `run` file, in python:
```
from inginious import feedback
feedback.set_custom_value("highlight", 56)

# Colors the line 3 of subproblem "subproblem_id" with the default color
feedback.set_custom_value("highlight", {"subproblem_id": 3})
# Colors the lines 2 and 4 of subproblem "subproblem_id" with the default color
feedback.set_custom_value("highlight", {"subproblem_id": [2, 4]})
# Colors the lines 1,2,3 of subproblem "subproblem_id1" with a pale red,
# and lines 5 of subproblem "subproblem_id2" with a darker green
feedback.set_custom_value("highlight", {
    "subproblem_id1": [{"lines": [1, 2, 3], "color": "red"}, {"lines": [4], "color": "darkred"}],
    "subproblem_id2": {"lines": [5], "color": "darkgreen"},
})
```


Inside your `run` file, in bash:
```
# Colors the line 3 of subproblem "subproblem_id" with the default color
feedback-custom --json highlight '{"subproblem_id": 3}'
# Colors the line 2 and 4 of subproblem "subproblem_id" with the default color
feedback-custom --json highlight '{"subproblem_id": [2, 4]}'
# Colors the lines 1,2,3 of subproblem "subproblem_id1" with a pale red,
# and lines 5 of subproblem "subproblem_id2" with a darker green
feedback-custom --json highlight '{"subproblem_id1": [{"lines": [1, 2, 3], "color": "red"}, {"lines": [4], "color": "darkred"}], "subproblem_id2": {"lines": [5], "color": "darkgreen"}}'
```


Supported colors
----------------

default, yellow, orange, red, green, blue, darkred, darkgreen, darkblue