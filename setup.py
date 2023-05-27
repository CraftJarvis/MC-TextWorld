from setuptools import setup, find_packages

setup(
    name='mctextworld',
    version='1.0.3',
    description='A text world based on Minecraft rules.',
    long_description='',
    # The project's main homepage.
    url='https://zhwang4ai.github.io/',
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
    py_modules=["mctextworld"],
    install_requires=['gym']
)