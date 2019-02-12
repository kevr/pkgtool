#!/usr/bin/env python3
import sys, os
import click

SCRIPT_DIR=os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])))

paths = [
  os.path.join(SCRIPT_DIR, "share/templates"),
  "/usr/share/pkgtool/templates",
  "/usr/local/share/pkgtool/templates",
]

def find_template_path():
  for path in paths:
    if os.path.exists(path) and os.path.isdir(path):
      return path

def get_template(template_type):
  path = find_template_path()
  template = os.path.join(path, "PKGBUILD.%s" % template_type)
  if not os.path.exists(template):
    return None
  with open(template) as f:
    return f.read().rstrip()

def make_template(template_type, project_name):
  template = get_template(template_type)
  if not template:
    click.echo('project_type %s is invalid' % template_type)
    exit(1)
  return template.replace('%PROJECT_NAME%', project_name)

@click.group()
@click.pass_context
def create(ctx):
  pass

@create.command('create')
@click.argument('project_type')
@click.argument('project_name')
def create_project(project_type, project_name):
  if os.path.exists('./PKGBUILD'):
    click.echo('A PKGBUILD already exists in this directory, quitting.')
    return
  template = make_template(project_type, project_name)
  with open('./PKGBUILD', 'w') as f:
    f.write(template)

def main():
  create()
  return 0

if __name__ == '__main__':
  e = main()
  exit(e)


