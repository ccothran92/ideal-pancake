from setuptools import setup

setup(
   name='ideal-pancake',
   version='1.0',
   description='MSA: Moist Soil Automation',
   author='Chris Cothran',
   author_email='foomail@foo.com',
   packages=['ideal-pancake'],  #same as name
   install_requires=['RPi'], #external packages as dependencies
)