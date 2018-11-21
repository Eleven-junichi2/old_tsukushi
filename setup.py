from setuptools import setup, find_packages

setup(
    name="tsukushi",
    author="Junichi Suetsugu",
    version="1.0.19",
    python_requires="==3.5.3",
    setup_requires=[
        "cython==0.29",
    ],
    install_requires=[
        "certifi==2018.10.15",
        "chardet==3.0.4",
        "docutils==0.14",
        "idna==2.7",
        "kivy==1.10.1",
        "kivy-garden==0.1.4",
        "pygments==2.2.0",
        "requests==2.20.1",
        "urllib3==1.23; python_version != '3.3.*'",
    ],
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/Eleven-junichi2/tsukushi",
    entry_points={
        "console_scripts": [
            "tsukushi = tsukushi.main:main",
        ],
    },
)
