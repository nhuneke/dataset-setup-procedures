#!/usr/bin/env python3

"""
Procedure to add .gitignore template
"""

import sys
import os.path as op

ds = sys.argv[1]

filepath = op.join(ds.path, '.gitignore')

ignorecontent = """\
# History files
.Rhistory
.Rapp.history

# Session Data files
.RData

# User-specific files
.Ruserdata

# Example code in package build process
*-Ex.R

# RStudio files
.Rproj.user/

# knitr and R markdown default cache directories
*_cache/
/cache/

# Temporary files created by R markdown
*.utf8.md
*.knit.md

# Temporary directory created by dcm2bids
tmp_dcm2bids/
"""

file = open(filepath, 'w+')
file.writelines(ignorecontent)
file.close

ds.save(message="Apply add .gitignore procedure")