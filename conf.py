import sys, os
extensions = ['sphinx.ext.graphviz']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'HiPFiSH API docs'
copyright = u'2016, Chris Gough'
version = '0.0'
release = '0.0'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'HiPFiSHAPIdocsdoc'
latex_elements = {
}
latex_documents = [
  ('index', 'HiPFiSHAPIdocs.tex', u'HiPFiSH API docs Documentation',
   u'Chris Gough', 'manual'),
]
man_pages = [
    ('index', 'hipfishapidocs', u'HiPFiSH API docs Documentation',
     [u'Chris Gough'], 1)
]
texinfo_documents = [
  ('index', 'HiPFiSHAPIdocs', u'HiPFiSH API docs Documentation',
   u'Chris Gough', 'HiPFiSHAPIdocs', 'One line description of project.',
   'Miscellaneous'),
]
