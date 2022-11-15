# -*- coding: utf-8 -*-
import distutils.core
from setuptools import setup

# Until pbr fixes the packages_root support, there will be some extra
# boilerplate in this setup.py file, and a hack in setup.cfg file. Bug in
# question:
#     https://bugs.launchpad.net/pbr/+bug/1686111
# The workaround is to trick pbr into finding the nested package by monkey
# patching pbr smart_find_packages and changing files.packages-root and
# files.packages to src in the setup.cfg. The monkey patch is done indirectly
# via a distutils monkey patch to make sure the patch is only applied once pbr
# has been installed in the .eggs directory.

distutils_core_setup_orig = distutils.core.setup


def distutils_core_setup(**attrs):
    def dumb_find_packages(top):
        from setuptools import find_packages

        return "\n".join(find_packages(where=top))

    import pbr.find_package

    pbr.find_package.smart_find_packages = dumb_find_packages
    distutils_core_setup_orig(**attrs)


distutils.core.setup = distutils_core_setup
setup(setup_requires=["pbr"], pbr=True)
