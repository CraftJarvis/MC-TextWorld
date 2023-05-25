from setuptools import setup, find_packages
from codecs import open
from os import path
setup(
    name='mc-textworld',
    version='1.0',
    description='A text world based on Minecraft rules.',
    long_description='',
    # The project's main homepage.
    url='craftjarvis.org',
    # Author details
    author='wangzihao',
    author_email='zhwang@stu.pku.edu.cn',
    # Choose your license
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=["mc-textworld"],
    install_requires=['gym']
)