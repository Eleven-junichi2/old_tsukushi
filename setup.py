from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

requires = ["cython", "kivy"]

setup(
    name="tsukushi",
    description='A code editor created by kivy.',
    long_description=readme,
    author="Junichi Suetsugu",
    install_requires=requires,
    test_suite="tests",
    license=license,
    entry_points={
        "gui_scripts": [
            "tsukushi = tsukushi.main:main"
        ]
    }
)
