from setuptools import setup
setup(
    name='pymill',
    version='0.1.1',
    description='Python API for Paymill credit card processing service',
    packages=['pymill'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['pycurl2']
)
