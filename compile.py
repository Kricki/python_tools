#!/usr/bin/env python3

# Example: python compile.py "python_dir" "cpython_dir"
# Compiles all files in "python_dir" to Bytecode (resulting in
# .pyc files) and moves them to "cpython_dir".

import sys
import os
import compileall
import shutil
from distutils import dir_util

python_dir = sys.argv[1]
cpython_dir = sys.argv[2]

# compile Python code to pyc
# "legacy=True": pyc files are created in the same directory as the corresponding py-file (no __pycache__ folder).
compileall.compile_dir(python_dir, legacy=True)

# Move all pyc files to "cpython_dir", while preserving the folder structure.

for root, dirs, files in os.walk(python_dir):
    for file_ in files:
        if file_.endswith(".pyc"):
        #if not file_.endswith(".py"):
            src_file = os.path.join(root, file_)
            dst_dir = os.path.join(cpython_dir, os.path.normpath(root))
            dst_file = os.path.join(dst_dir, file_)
            
            print(src_file)
            print(dst_dir)
            print(dst_file)
            
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                
            shutil.move(src_file, dst_file)



