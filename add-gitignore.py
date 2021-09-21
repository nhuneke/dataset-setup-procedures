#!/usr/bin/env python3

"""
Procedure to add .gitignore template
"""

import sys
import os.path as op
from datalad.distribution.dataset import require_dataset

ds = require_dataset(
	sys.argv[1],
	check_installed=True,
	purpose="Add gitignore")

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

file = '.gitignore'
open(file, 'a').close()

with open(file, 'w') as f:
	f.write(ignorecontent)
	f.close()

ds.save(message="Apply add .gitignore procedure")