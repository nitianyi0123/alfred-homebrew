import subprocess
from workflow import Workflow, PasswordNotFound


def get_all_packages():
    cmd, err = subprocess.Popen(['/usr/local/bin/brew', 'search'], stdout=subprocess.PIPE).communicate()
    return cmd


def get_installed_packages():
    cmd, err = subprocess.Popen(['/usr/local/bin/brew', 'list', '--versions'], stdout=subprocess.PIPE).communicate()
    return cmd


def get_info():
    cmd, err = subprocess.Popen(['/usr/local/bin/brew', 'info'], stdout=subprocess.PIPE).communicate()
    return cmd

if __name__ == '__main__':
    wf = Workflow()
    wf.cache_data('brew_all', get_all_packages())
    wf.cache_data('brew_installed', get_installed_packages())
    wf.cache_data('brew_info', get_info())
