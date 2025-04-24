# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Smart Coking System Documentation'
copyright = '2024, Yuhang Qiu, Haodong Liu'
author = 'Haodong Liu'
release = 'v1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# os.path.dirname(__file__) 是当前 conf.py 文件的路径。
# '../..' 表示向上两级到项目的根目录。
project_path = os.path.join(os.path.dirname(__file__), '../..')
print(project_path)
sys.path.insert(0, project_path)
print("Current sys.path:", sys.path)  # 确认路径打印是否正确

# Sphinx 扩展
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgconverter',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'sphinx.ext.viewcode',
]

latex_engine = 'xelatex'  # 或 'pdflatex','xelatex', 'lualatex'
latex_documents = [
    ('index', 'output.tex', 'Your Project Title',
     'Author Name', 'manual'),
]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
        \usepackage{xeCJK}   % 加载 xeCJK 宏包
        \setCJKmainfont{SimSun}  % 设置中文字体
        \setCJKsansfont{SimHei}  % 设置无衬线字体
        \setCJKmonofont{KaiTi}   % 设置等宽字体

        \renewcommand{\contentsname}{User Documentation}  % 修改目录标题
        \renewcommand{\figurename}{Fig.}  % 修改图标题
        \renewcommand{\tablename}{Table}  % 修改表标题

        \usepackage{hyperref}    % 支持超链接
        \hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue}  % 超链接颜色
    ''',
    'babel': '',  # 禁用 Babel
}



# 文档源文件类型
source_suffix = '.rst'  # 使用 .rst 作为文档源文件

# 静态文件路径
html_static_path = ['_static']

# 添加自定义的 CSS 文件
html_css_files = [
    'css/modify.css',
]

# 模板路径
templates_path = ['_templates']
exclude_patterns = []
# 主文档
master_doc = 'index'  # 指定主文档为 index.rst

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  

# Logo
html_logo = './logos/logo.png'

# 自动生成文档的设置
autodoc_default_options = {
    'members': True,            # 仅生成显式定义的成员文档
    'undoc-members': False,     # 不生成未文档化成员的文档
    'private-members': False,   # 不生成私有成员的文档
    'special-members': False,   # 不生成特殊成员的文档（如 __init__）
    'inherited-members': False, # 不生成继承成员的文档
    'show-inheritance': False,  # 不显示继承信息
}


# Napoleon 设置（如果你使用 Google-style 或 Numpy-style 的 docstrings）
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True


