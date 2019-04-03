from setuptools import setup

with open( 'README.md', 'r' ) as f:
    long_description = f.read()

setup(
        name='SilverHeart',
        version=1.0,
        author='Pedro Vieira',
        author_email='pedrovieira3333@protonmail.com',
        license='GPLv3',
        description='Keylogger developed in python',
        long_description=long_description,
        url='https://github.com/PedrV/SilverHeart',
        packages=['Windows', 'macOS _ Linux'],
        python_requires='>=3.7',
        install_requires=[
            'pynput>=1.4.2',
            'Pywin32>=224',
        ],
        classifiers=[
            'Development Status :: 1 - Alpha',
            'Licence :: OSI Approved :: GPLv3+ license',
            'Operating System :: Windows',
        ]

)
