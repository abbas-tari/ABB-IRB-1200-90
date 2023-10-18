import setuptools
from distutils.core import setup, Extension

def main():
    setup(
        name='pyikfast_abb_irb_1200_90',
        version='0.0.1',
        description='ikfast wrapper',
        author='Abbas Tariverdi',
        author_email='abbasta@abbasta.com',
        ext_modules=[Extension('pyikfast_abb_irb_1200_90', ['ikfast_robot.cpp', 'pyikfast.cpp'])],
        setup_requires=['wheel'],
        install_requires=['numpy'] 
    )

if __name__ == '__main__':
    main()
