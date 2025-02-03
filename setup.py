from setuptools import find_packages, setup
setup(
    name='aly',
    packages=find_packages(include=["aly","aly.management","aly.management.structure"]),
    version='0.0.2',
    description='Python library helps you to create Telegram bots more easily',
    author='Omar Elkhadragy',
    license='MIT',
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    entry_points={
        "console_scripts": [
            "aly = aly.cli:main",
        ]
    },
    url="https://github.com/okhadragy/aly",
    project_urls={
        "Source Code": "https://github.com/okhadragy/aly",
    }
)
