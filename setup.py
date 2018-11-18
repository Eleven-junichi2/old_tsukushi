from setuptools import setup

setup(
    name="tsukushi",
    version="1.0",
    install_requires=["cython", "kivy"],
    # extras_require={
    #     "develop": ["dev-packageA", "dev-packageB"]
    # },
    entry_points={
        "console_scripts": [
            "foo = package_name.module_name:func_name",
            "foo_dev = package_name.module_name:func_name [develop]"
        ],
        "gui_scripts": [
            "bar = gui_package_name.gui_module_name:gui_func_name"
        ]
    }
)
