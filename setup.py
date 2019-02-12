#!/usr/bin/env python3
from setuptools import setup, find_packages
from setuptools.command.install import install
import os
from shutil import copyfile

class PostInstallCommand(install):
  def run(self):

    try:
      prefix = os.environ['PREFIX']
    except:
      raise OSError('PREFIX is not set')

    share = os.path.join(prefix, 'share/pkgtool/templates')

    if not os.path.exists(share):
      os.makedirs(share)

    templates = [
      'PKGBUILD.standard',
    ]

    for template in templates:
      copyfile('share/templates/%s' % template, os.path.join(share, template))


    install.run(self)

setup(
  name='pkgtool',
  version='1.0',
  scripts=['pkgtool.py', 'pkgtool'],
  cmdclass={
    'install': PostInstallCommand,
  }
)

