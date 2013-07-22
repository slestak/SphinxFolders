#!/usr/bin/env python
#coding=utf-8
import codecs
import datetime
from distutils import log
from distutils.core import setup
import getpass
import glob
import imp
import os
import os.path
import re
import sys

module_name = 'sphinxfolders'
if module_name == '{' + '{ package_name }' + '}':
    module_name = 'starterpyth'

command = len(sys.argv) > 1 and sys.argv[1] or None
build_path = os.path.join(os.path.dirname(__file__), 'build')

(file_, pathname, description) = imp.find_module(module_name)
main_module = imp.load_module(module_name, file_, pathname, description)

__version__ = getattr(main_module, '__version__',  u'1.0')
__author__ = getattr(main_module, '__author__',  getpass.getuser())
__maintainer__ = getattr(main_module, '__maintainer__',  getpass.getuser())
__email__ = getattr(main_module, '__email__',  u'%s@example.com' % getpass.getuser())
__maintainer_email__ = getattr(main_module, '__email__',  u'%s@example.com' % __maintainer__)
__copyright__ = getattr(main_module, '__copyright__',  u'Copyright %d' % datetime.date.today().year)
__credits__ = getattr(main_module, '__credits__',  [])
__licence__ = getattr(main_module, '__licence__',  u'Cecill-B')
__description__ = getattr(main_module, '__description__',  u'Sample Python application')
__url__ = getattr(main_module, '__url__',  u'http://www.example.com/%s/' % module_name)
__include_paths__ = getattr(main_module, '__include_paths__', [])


def find_packages(name, main_module):
    source = os.path.abspath(os.path.dirname(main_module.__file__))
    l = len(source)
    result = [str(name), ]
    for root, dirs, files in os.walk(source):
        for mod_name in dirs:
            s = '%s.%s' % (name, os.path.join(root, mod_name)[l+1:].replace(os.path.sep, '.'))
            file_ = None
            try:
                (file_, pathname, description) = imp.find_module(mod_name, [root, ])
                imp.load_module(s, file_, pathname, description)
                file_ = None
                result.append(s)
            except:
                file_.close() if file_ else 0
    return result

def find_data_files(sources, exclude_regexp):
    u'''Helper function to generate list of extra files for py2exe'''
    lis = []
    ret = {}
    r = re.compile(exclude_regexp)
    for source in sources:
        source = os.path.join(os.path.abspath(os.path.dirname(main_module.__file__)), source)
        target = os.path.basename(source)
        for root, dirs, files in os.walk(source):
            for k in files:
                pathname = os.path.join(root, k)
                if r.match(pathname):
                    continue
                targetpath = os.path.join(target, os.path.relpath(pathname, source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(pathname)
                lis.append(os.path.join(target, os.path.relpath(pathname, source)))
    return (lis, sorted(ret.items()))

data_files, exe_data_files = find_data_files(__include_paths__, '.*(.svn).*')


# try to include some extra commands
try: import py2app
except: pass
try: import py2exe
except: pass
cmdclass = {}
try:
    import starterpyth.command.gen_doc
    import starterpyth.command.gen_doc_api
    import starterpyth.command.dependencies
    import starterpyth.command.lint
    import starterpyth.command.dmg
    import starterpyth.command.test_doc
    import starterpyth.command.compilemessages
    import starterpyth.command.makemessages
    cmdclass.update({
        'gen_doc': starterpyth.command.gen_doc.gen_doc,
        'gen_doc_api': starterpyth.command.gen_doc_api.gen_doc_api, 
        'dependencies': starterpyth.command.dependencies.dependencies, 
        'lint': starterpyth.command.lint.lint, 
        'dmg': starterpyth.command.dmg.dmg, 
        'test_doc': starterpyth.command.test_doc.test_doc, 
        'makemessages': starterpyth.command.makemessages.makemessages, 
        'compilemessages': starterpyth.command.compilemessages.compilemessages, 
        })
except:
    pass


packages = find_packages(module_name, main_module)
extra_options = {
        'name': module_name,
        'version': __version__,
        'author': __author__,
        'author_email': __email__,
        'maintainer': __maintainer__,
        'maintainer_email': __maintainer_email__,
        'description': __description__,
        'license': __licence__,
        'long_description': codecs.open(os.path.join(os.path.dirname(__file__), 'README.txt'), 'r', encoding='utf-8').read(),
        'url': __url__,
        'packages': packages,
        'platforms': ['all'],
        'package_data': {module_name: data_files, },
        'cmdclass': cmdclass,
        'provides': packages,
        'test_suite': '%s.load_tests' % module_name,
        }
if command == 'py2exe':
    extra_options['setup_requires'] = ['py2exe', ]

for k, v in extra_options.items():
    if isinstance(v, unicode):
        extra_options[k] = v.encode('utf-8')

extra_options['install_requires'] = [] # please add here a list of required Python modules
setup(requires=['sphinx', 'docutils'], **extra_options)
