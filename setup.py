# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 19:26
from os.path import abspath, join, dirname
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()
version = {}
with open(join(this_dir, "hanlp", "version.py")) as fp:
    exec(fp.read(), version)

FASTTEXT = 'fasttext-wheel==0.9.2'
extras_require = {
    'amr': [
        'penman==1.2.1',
        'networkx>=2.5.1',
        'perin-parser>=0.0.12',
    ],
    'fasttext': [FASTTEXT],
    'tf': [
        FASTTEXT,
        'tensorflow>=2.6.0',
        'keras==2.6.0',
    ]
}
extras_require['full'] = list(set(sum(extras_require.values(), [])))

setup(
    name='hanlp',
    version=version['__version__'],
    description='HanLP: Han Language Processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hankcs/HanLP',
    author='hankcs',
    author_email='hankcshe@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        "Development Status :: 4 - Beta",
        'Operating System :: OS Independent',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        "Topic :: Text Processing :: Linguistic"
    ],
    keywords='corpus,machine-learning,NLU,NLP',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=[
        'termcolor',
        'pynvml',
        'toposort==1.5',
        'transformers>=4.1.1',
        'tokenizers==0.11.6',  # The latest tokenizers==0.12.1 failed to compile on macOS Python3.6
        'torch>=1.6.0',
        'hanlp-common>=0.0.13',
        'hanlp-trie>=0.0.4',
        'hanlp-downloader',
    ],
    extras_require=extras_require,
    python_requires='>=3.6',
    # entry_points={
    #     'console_scripts': [
    #         'hanlp=pyhanlp.main:main',
    #     ],
    # },
)
