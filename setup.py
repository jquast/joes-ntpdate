#!/usr/bin/env python
""" Distribution file for joes-ntpdate. """
# std imports
import sys
import os

# 3rd-party
import setuptools

HERE = os.path.dirname(__file__)

setuptools.setup(
    name='joes-ntpdate',
    version='1.9.76',
    description=("Joe's own ntpdate: set the date and time via NTP"),
    long_description=open(os.path.join(HERE, 'README.rst')).read(),
    author='Jeff Quast',
    author_email='contact@jeffquast.com',
    license='MIT',
    packages=['joes_ntpdate'],
    install_requires=['ntplib>=0.3.2'],
    url='https://github.com/jquast/joes_ntpdate',
    include_package_data=True,
    zip_safe=True,
    keywords=['ntpdate', 'hwclock', 'time', 'clock', 'synchronize'],
    entry_points={
        'console_scripts': ['joes-ntpdate=joes_ntpdate.joes_ntpdate:main'],
    },
    classifiers=[
        'Topic :: System :: Networking :: Time Synchronization'
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: Linux',
        # not tested, please report or pull request
        #
        # 'Operating System :: POSIX :: BSD :: FreeBSD',
        # 'Operating System :: POSIX :: BSD :: NetBSD',
        # 'Operating System :: POSIX :: BSD',
        # 'Operating System :: POSIX :: SunOS/Solaris',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals'
    ],
)
