import codecs
import fnmatch
import re

__author__ = 'flanker'
import os


def render_directory_html(self, node, directory, root, options):
    filenames = os.listdir(directory)
    cls = ''
    if node['options'].get('class'):
        cls = ' class="%s"' % node['options']['class']
    glob_txt = node['options'].get('glob')
    regexp = node['options'].get('regexp')
    desc_ext = node['options'].get('desc_ext')
    content = unicode("<ul %s>" % cls)
    for filename in filenames:
        if glob_txt and not fnmatch.fnmatch(filename, glob_txt):
            continue
        if regexp and not regexp.match(filename):
            continue
        fullpath = os.path.join(directory, filename)
        if not os.path.isfile(fullpath):
            continue
        if filename.startswith('.'):
            continue
        relpath = os.path.relpath(fullpath, root)
        ext = os.path.splitext(relpath)[1]
        if ext == desc_ext:
            continue
        link = unicode("<a href=\"%s\">%s</a>") % (relpath, filename)
        if desc_ext:
            desc_path = fullpath + desc_ext
            if os.path.isfile(desc_path):
                with codecs.open(desc_path, 'r', encoding='utf-8') as desc_fd:
                    link += unicode("<span>%s</span>") % desc_fd.read()
        content += unicode("<li class=\"%s\">%s</li>\n") % (ext, link)
    content += "</ul>"

    self.body.append(content)


def visit_folder_node(self, node):
    render_directory_html(self, node, node['directory'], node['root'], node['options'])


def depart_folder_node(self, node):
    return
