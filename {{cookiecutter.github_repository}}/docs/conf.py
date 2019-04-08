"""Sphinx configuration file."""

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
