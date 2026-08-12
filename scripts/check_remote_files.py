import os
import subprocess
import sys

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, cwd=os.getcwd()).strip()

# get tracked files
tracked = run('git ls-files').splitlines()
# get remote files in origin/main
try:
    remote = run('git ls-tree -r --name-only origin/main')
    remote_files = set(remote.splitlines())
except subprocess.CalledProcessError as e:
    print('ERROR: could not list remote files:', e)
    remote_files = set()

# find tracked files not in remote
not_in_remote = [f for f in tracked if f not in remote_files]

# find large files >100MB
large_files = []
for dirpath,_,filenames in os.walk(os.getcwd()):
    # skip .git directory
    if os.path.abspath(dirpath).startswith(os.path.abspath(os.path.join(os.getcwd(), '.git'))):
        continue
    for fn in filenames:
        path = os.path.join(dirpath, fn)
        try:
            size = os.path.getsize(path)
        except Exception:
            continue
        rel = os.path.relpath(path, os.getcwd())
        if size > 100*1024*1024:
            large_files.append((rel, size))
        elif size > 50*1024*1024:
            large_files.append((rel, size))

print('STATUS:')
if run('git status --porcelain') == '':
    print('  Working tree: clean')
else:
    print('  Working tree: has changes (run git status)')

print('\nTracked files not present on origin/main:')
if not_in_remote:
    for f in not_in_remote:
        print('  -', f)
else:
    print('  None')

print('\nLocal files >100 MB:')
if large_files:
    for f,s in sorted(large_files, key=lambda x:-x[1]):
        print('  -', f, f"({s/1024/1024:.2f} MB)")
else:
    print('  None')

# exit with code 0
sys.exit(0)
