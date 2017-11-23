from setuptools import setup, find_packages

# Basics ---------------------------------------------------------------------

NAME = 'hanabi'
VERSION = '0.1'
DESCRIPTION = 'Hanabi, the co-operative card game.'
LONG_DESCRIPTION = DESCRIPTION
AUTHOR = 'lekha'

# Dependencies ---------------------------------------------------------------

INSTALL_DEPS = ()
TESTS_DEPS = ()

if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        install_requires=INSTALL_DEPS,
        tests_require=TESTS_DEPS,
        packages=find_packages(exclude=['test', 'test.*']),
        include_package_data=True,
    )
