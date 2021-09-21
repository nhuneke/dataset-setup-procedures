#!/usr/bin/env python3

"""
Procedure to add README template
"""

import sys
import os.path as op
import re
from datalad.distribution.dataset import require_dataset

ds = require_dataset(
	sys.argv[1],
	check_installed=True,
	purpose="Add README")

# Get dataset id (pythonised GREP)	
with open('.datalad/config', "r") as conf:
	for line in conf:
		if re.search('id = ', line):
			id = line

readmecontent = """\
# [Replace with Title of Dataset]

## General information

This is a DataLad dataset ({}). Include 
an overall summary of the dataset here, e.g. This dataset contains x data for n
participants who completed a, b, c tasks.

## References and Links

Include references to publications or other relevant links (e.g. OSF projects) here.

## Dataset Content

### Data

Describe what and where the data are.

### Code
- All custom code is located in `code/`.
- Describe contents briefly.
- An accompanying README is present in the `code/` folder.

## DataLad datasets and how to use them

This repository is a [DataLad](https://www.datalad.org/) dataset. It provides
fine-grained data access down to the level of individual files, and allows for
tracking future updates. In order to use this repository for data retrieval,
[DataLad](https://www.datalad.org/) is required. It is a free and open source
command line tool, available for all major operating systems, and builds up on
Git and [git-annex](https://git-annex.branchable.com/) to allow sharing,
synchronizing, and version controlling collections of large files.

More information on how to install DataLad and [how to install](http://handbook.datalad.org/en/latest/intro/installation.html)
it can be found in the [DataLad Handbook](https://handbook.datalad.org/en/latest/index.html).

### Get the dataset

A DataLad dataset can be `cloned` by running

```
datalad clone <url>
```

Once a dataset is cloned, it is a light-weight directory on your local machine.
At this point, it contains only small metadata and information on the identity
of the files in the dataset, but not actual *content* of the (sometimes large)
data files.

### Retrieve dataset content

After cloning a dataset, you can retrieve file contents by running

```
datalad get <path/to/directory/or/file>
```

This command will trigger a download of the files, directories, or subdatasets
you have specified.

DataLad datasets can contain other datasets, so called *subdatasets*.  If you
clone the top-level dataset, subdatasets do not yet contain metadata and
information on the identity of files, but appear to be empty directories. In
order to retrieve file availability metadata in subdatasets, run

```
datalad get -n <path/to/subdataset>
```

Afterwards, you can browse the retrieved metadata to find out about subdataset
contents, and retrieve individual files with `datalad get`.  If you use
`datalad get <path/to/subdataset>`, all contents of the subdataset will be
downloaded at once.

### Stay up-to-date

DataLad datasets can be updated. The command `datalad update` will *fetch*
updates and store them on a different branch (by default
`remotes/origin/master`). Running

```
datalad update --merge
```

will *pull* available updates and integrate them in one go.

### Find out what has been done

DataLad datasets contain their history in the ``git log``.  By running ``git
log`` (or a tool that displays Git history) in the dataset or on specific
files, you can find out what has been done to the dataset or to individual
files by whom, and when.
""".format(id)

file = 'README.md'
open(file, 'a').close()

with open(file, 'w') as f:
	f.write(readmecontent)
	f.close()

ds.save(message="Add README template")