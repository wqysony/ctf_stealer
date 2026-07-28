from setuptools import setup
from setuptools.command.install import install

class InstallCommand(install):
    """Override the default Install class."""

    def run(self):
        install.run(self)

setup(
    name="ctf_stealer",
    version="0.1",
    description="hello world",
    author="Your Name",
    packages=["ctf_stealer"],
    cmdclass={
        "install": InstallCommand,
    },
)
