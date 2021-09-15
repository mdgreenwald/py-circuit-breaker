from setuptools import find_packages, setup

setup(
    name='py-circuit-breaker',
    packages=find_packages(include=['py_circuit_breaker']),
    version='0.1.0',
    description='Circuit Breaker Pattern Library',
    author='Matthew Greenwald',
    license='Apache-2.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.5'],
    test_suite='tests'
)