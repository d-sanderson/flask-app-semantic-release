from setuptools import setup

with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:

  setup(
   name='flask-semantic-release',
   version=version_file.read().strip(),
   description='A useful module',
   author='Meow Wolf DE',
  )
