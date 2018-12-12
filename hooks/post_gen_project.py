#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from distutils.dir_util import remove_tree
import os
import subprocess

# Workaround cookiecutter no support of symlinks
TEMPLATE = 'cookiecutter-terra-front'
SYMLINKS = {
    ".ansible/scripts/setup_vaults.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/setup_corpusops.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/test.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/setup_core_variables.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/call_roles.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/yamldump.py": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/call_ansible.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/edit_vault.sh": "cops_wrapper.sh",  #noqa
    ".ansible/scripts/print_env.sh": "call_ansible.sh",  #noqa
    ".ansible/scripts/setup_ansible.sh": "cops_wrapper.sh",  #noqa
    ".ansible/playbooks/ping.yml": "../../local/terra-front-deploy/.ansible/playbooks/ping.yml",  #noqa
    ".ansible/playbooks/roles/terralegofront_vars": "../../../local/terra-front-deploy/.ansible/playbooks/roles/terralegofront_vars/",  #noqa
    ".ansible/playbooks/roles/terralegofront": "../../../local/terra-front-deploy/.ansible/playbooks/roles/terralegofront",  #noqa
    ".ansible/playbooks/app.yml": "../../local/terra-front-deploy/.ansible/playbooks/app.yml",  #noqa
    ".ansible/playbooks/deploy_key_setup.yml": "../../local/terra-front-deploy/.ansible/playbooks/deploy_key_setup.yml",  #noqa
    ".ansible/playbooks/deploy_key_teardown.yml": "../../local/terra-front-deploy/.ansible/playbooks/deploy_key_teardown.yml",  #noqa
    ".ansible/playbooks/site.yml": "../../local/terra-front-deploy/.ansible/playbooks/site.yml",  #noqa
    "Dockerfile.nginx": "local/terra-front-deploy/Dockerfile.nginx",  #noqa
    "Dockerfile": "local/terra-front-deploy/Dockerfile",  #noqa
}
GITSCRIPT = """
set -ex
if [ ! -e .git ];then git init;fi
git remote rm origin || /bin/true
git remote add origin {{cookiecutter.git_project_url}}
git add .
rm -rf "{{cookiecutter.deploy_project_dir}}"
git add -f local/regen.sh
if [ ! -e "{{cookiecutter.deploy_project_dir}}/.git" ];then
    git submodule add -f "{{cookiecutter.deploy_project_url}}" \
        "{{cookiecutter.deploy_project_dir}}"
fi
"""
MOTD = '''
After reviewing all changes
do not forget to commit and push your new/regenerated project
'''


def sym(i, target):
    print('* Symlink: {0} -> {1}'.format(i, target))
    d = os.path.dirname(i)
    if os.path.exists('local/terra{{cookiecutter.app_suffix}}-deploy'):
        remove_tree('local/terra{{cookiecutter.app_suffix}}-deploy')
    if d and not os.path.exists(d):
        os.makedirs(d)
    if os.path.exists(i) or os.path.islink(i):
        if os.path.isdir(i):
            remove_tree(i)
        else:
            os.unlink(i)
    os.symlink(target, i)


def main():
    for i in SYMLINKS:
        sym(i, SYMLINKS[i])

    subprocess.check_call(GITSCRIPT.format(template=TEMPLATE), shell=True)
    print(MOTD)


if __name__ == '__main__':
    main()
# vim:set et sts=4 ts=4 tw=80:
