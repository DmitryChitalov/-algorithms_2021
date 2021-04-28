from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('task_2_cython.pyx'))
