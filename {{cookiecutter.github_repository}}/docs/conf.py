"""Sphinx configuration file."""

from pkg_resources import get_distribution

release = get_distribution('{{ cookiecutter.pypi_name }}').version
version = '.'.join(release.split('.')[:2])

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
