from setuptools import find_packages, setup
setup(
    name='socialpybot',
    packages=find_packages(include=["pybot","pybot.management","pybot.management.structure"]),
    version='0.0.1',
    description='Python library helps you to create Telegram bots more easily',
    author='Omar Elkhadragy',
    license='MIT',
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    entry_points={
        "console_scripts": [
            "pybot = pybot.cli:main",
        ]
    }
)
