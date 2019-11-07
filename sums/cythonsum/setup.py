from distutils.core import setup
from Cython.Build import cythonize

setup(name='cythonsum app',
      ext_modules=cythonize("cythonsums.pyx"))
