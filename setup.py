from setuptools import setup, find_packages
setup(
    name="Ninja_Preview",
    version="2.1-beta",
    packages=find_packages(),
    install_requires=['Qmlview >= 1.1'],
    entry_points={
            'gui_scripts': ['Ninja_Preview = Ninja_Preview.Ninja_preview:dummy_run'],
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
    long_description = """\
    Ninja_Preview is a Graphical User Interface that aims at letting you 
    use qmlview, which is just like qmlscene in a more flexible way, since 
    both do not provide with Graphical User Interfaces.
    """
    
)
