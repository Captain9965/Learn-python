"""while using the import syntax, remember that the last attribute should be a package or module, not a class or function:
"""

# import test_package.package_module
# test_package.package_module.call_package_module()

"""
    The from....import syntax is more convenient if we want not to call the whole function tree
"""
from test_package import call_package_module
call_package_module()