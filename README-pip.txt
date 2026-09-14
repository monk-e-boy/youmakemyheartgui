# this will create a .whl in a dist folder
python -m build

# this sends it to PyPl
twine upload dist/*