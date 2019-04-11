"""Sphinx configuration file."""

from pkg_resources import get_distribution

project = "{{ cookiecutter.name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.author }}"
release = get_distribution('{{ cookiecutter.pypi_name }}').version
version = '.'.join(release.split('.')[:2])

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
