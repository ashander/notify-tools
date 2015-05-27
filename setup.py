from setuptools import setup

setup(
    name='notify-tools',
    version='0.1',
    py_modules=['notify_tools'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'timer = notify_tools:timer',
            'todo = notify_tools:todo'
        ]
    },
)
