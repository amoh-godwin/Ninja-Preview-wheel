from setuptools import setup, find_packages

with open("README.md", 'r') as r_file:
    readme = r_file.read()

setup(
    name="Ninja-Preview",
    version="2.2",
    packages=find_packages(),
    install_requires=['Qmlview >= 1.1'],
    entry_points={
            'gui_scripts': ["Ninja-Preview=Ninja_Preview.Ninja_preview:dummy_run"],
    },

    author="Amoh - Gyebi Godwin Ampofo Michael",
    author_email="amohgyebigodwin@gmail.com",
    description="A preview for your Qml files",
    keywords="qmlview, qmlscene, qml, pyqt, pyqt5, pyside, pyside2",
    url="https://github.com/amoh-godwin/Ninja-Preview-wheel/",
    project_urls={
        "Bug Tracker": "https://github.com/amoh-godwin/Ninja-Preview-wheel/issues/",
        "Documentation": "https://github.com/amoh-godwin/Ninja-Preview-wheel/wiki/",
        "Source Code": "https://github.com/amoh-godwin/Ninja-Preview-wheel/",
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    long_description = readme,
    long_description_content_type = "text/markdown"
    
)
