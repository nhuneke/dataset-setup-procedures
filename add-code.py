#!/usr/bin/env python3

"""
Procedure to add code directory
"""

import sys
import os
import os.path as op
from datalad.distribution.dataset import require_dataset

ds = require_dataset(
	sys.argv[1],
	check_installed=True,
	purpose="Add code directory")
	
os.mkdir('code')

codepath = op.join(ds.path, 'code')

readmecontent = """\
# [Replace with Title of Dataset] - Custom code

This directory contains custom code for the above dataset. All scripts are written such
that they can be executed from the root of the dataset, and are only using
relative paths for portability.

## Contents

List the contents with instructions for the purpose and use of each script. For example,

#### convert2nifti.sh
Script to convert source DICOMS to NIfTI format. Run with the following command:
```
$ bash code/convert2nifti.sh
```
Enter subject ID's when prompted separated by spaces, e.g ```sub-01 sub-02 etc...```

Software required to run: 
- DataLad
- dcm2niix
- dcm2bids

#### co2_bids_config.json
JSON file describing configuration for `dcm2bids`.
"""

attributes = op.join(codepath, '.gitattributes')
open(attributes, 'a').close()  # create .gitattributes

# instruct annex to ignore files in directory
with open(attributes, 'a+') as attrs:
	attrs.write('* annex.largefiles=nothing\n')  
	attrs.close()
	
ds.save(
	attributes,
	)

file = op.join(codepath, 'README.md')
open(file, 'a').close()  # create README

# write README
with open(file, 'w') as f:
	f.write(readmecontent)
	f.close()

ds.save(
	file,
	message = "Add code directory"
	)