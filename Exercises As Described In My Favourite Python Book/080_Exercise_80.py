# Question :-
"""Using the functions from Extra_file_for_Exercise_80.py in a Write an import statement at the top of your program , and modify it to use the imported functions."""

import Extra_file_for_Exercise_80 as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)