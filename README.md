# Dataset Setup Procedures

This repository is a DataLad dataset containing procedures for setting up a DataLad dataset. 

There are procedures to:

- Add a `README`
- Add a `.gitignore` file
- Add a `/code` folder and `README`
- Set up an RIA backup and associated GitLab sibling 
- Add licenses for data and code

## Installation 

### Requirements
- DataLad - [installation instructions](https://anaconda.org/conda-forge/datalad) 
- python-gitlab - [installation instructions](https://python-gitlab.readthedocs.io/en/stable/install.html)

Please go through the following steps to set your machine up to run the procedures:
1. Create a GitLab account. These procedures are currently configured to use the University of Southampton's [GitLab instance](https://git.soton.ac.uk) 
2. You will need to generate a personal access token for GitLab [here](https://git.soton.ac.uk/-/profile/personal_access_tokens).
3. Create a `python-gitlab config file`. Copy and paste the following into a text file, inserting your personal access token in the appropriate field:

```
[soton] 
url = https://git.soton.ac.uk
private_token = [insert token here] 
```		
4. Save this file in your `home` directory (`~`) as `.python-gitlab.cfg`

### Installing the procedures

1. Create a new DataLad dataset for your project:

```
datalad create new-dataset
```

2. Go into your new dataset 

```
cd new-dataset
```

3. Clone this repository into `.datalad/procedures`

```
datalad clone -d . https://github.com/nhuneke/dataset-setup-procedures .datalad/procedures
```

4. Check installation was successful 

```
datalad run-procedure --discover
```

This should produce the following output:

```
setup (/Users/user1/new-dataset/.datalad/procedures/setup.sh) [executable]
add-licenses (/Users/user1/new-dataset/.datalad/procedures/add-licenses.py) [executable]
add-code (/Users/user1/new-dataset/.datalad/procedures/add-code.py) [executable]
backup (/Users/user1/new-dataset/.datalad/procedures/backup.sh) [bash_script]
add-gitignore (/Users/user1/new-dataset/.datalad/procedures/add-gitignore.py) [python_script]
add-readme (/Users/user1/new-dataset/.datalad/procedures/add-readme.py) [executable]
```

## Usage

Each procedure can be run individually to complete a specific task, or as a group for initial set up of a new dataset.

### Backup

This procedure creates a remote indexed archive (RIA) backup and associated GitLab sibling. Before running this procedure ensure you have completed the [setup as above](#requirements). 

Run the procedure from within your dataset with:

```
datalad run-procedure backup
```

Complete the URL for the RIA backup and the project address for the Gitlab sibling when prompted. If you don't know these then ask your supervisor. 

You can check this procedure has run correctly with 

```
datalad siblings
```

You should see `ria-backup`, `ria-backup-storage` and `gitlab` siblings. Publishing to the `gitlab` sibling is dependent on the `ria-backup` sibling, so that if you run

```
datalad push --to gitlab
``` 

your dataset will be backed up to both the RIA and GitLab siblings. 

### Add README

This procedure adds a `README` template to your dataset. From within your dataset, run

``` 
datalad run-procedure add-readme
```

### Add gitignore

This procedure adds a `.gitignore` template to your dataset. From within your dataset, run

``` 
datalad run-procedure add-gitignore
```

### Add code directory

This procedure adds a `/code` directory with an accompanying `README` template and instructs the annex to send all contents of `/code` to git. From within your dataset, run

```
datalad run-procedure add-code
```

### Run as a group

The above procedures can also be run as a group with a single command for complete initial set up. From within your dataset, run

```
datalad run-procedure setup
```

### Add Licenses

This procedure is not included in the initial setup group as not all datasets will be shared and so need a license. Further, the licenses chosen for this procedure might not be appropriate for all datasets. 

This procedure adds a `CC-BY 4.0` license to the dataset and an `MIT` license to the code directory in the form of a `LICENSE` file. 

If you plan to share your dataset, code, or both, and these licenses are appropriate, then from within your dataset, run

```
datalad run-procedure add-licenses
```

## Contributing

Contributions welcome. Please use the following procedure:

1. On GitHub, fork a copy of this repository into your userspace
2. Install that copy locally using
```
datalad clone <https://github.com/url/of/fork.git>
```
3. Make changes. Save changes and push the branch to your fork
```
datalad save -m '<message>'
datalad push --to origin
```
4. Send a pull request
