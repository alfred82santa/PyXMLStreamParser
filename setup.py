import ast

import os
from setuptools import setup

PACKAGE_NAME = 'xmlstreamparser'

path = os.path.join(os.path.dirname(__file__), PACKAGE_NAME, '__init__.py')

with open(path, 'r') as file:
    t = compile(file.read(), path, 'exec', ast.PyCF_ONLY_AST)
    for node in (n for n in t.body if isinstance(n, ast.Assign)):
        if len(node.targets) != 1:
            continue

        name = node.targets[0]
        if not isinstance(name, ast.Name) or \
                name.id not in ('__version__', '__version_info__', 'VERSION'):
            continue

        v = node.value
        if isinstance(v, ast.Str):
            version = v.s
            break
        if isinstance(v, ast.Tuple):
            r = []
            for e in v.elts:
                if isinstance(e, ast.Str):
                    r.append(e.s)
                elif isinstance(e, ast.Num):
                    r.append(str(e.n))
            version = '.'.join(r)
            break

# Get the long description from the README file
with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyXMLStreamParser',
    url='https://github.com/alfred82santa/PyXMLStreamParser',
    author='alfred82santa',
    version=version,
    author_email='alfred82santa@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Development Status :: 4 - Beta'],
    packages=['xmlstreamparser'],
    include_package_data=False,
    install_requires=[],
    description="Python library to parse XML streams easily ",
    long_description=long_description,
    test_suite="nose.collector",
    tests_require="nose",
    zip_safe=True,
)
