# Dataset Setup Procedures

This repository is a DataLad dataset containing procedures for setting up a dataset. 

There are procedures to:

- Add a `README`
- Add a `.gitignore` file
- Add a `/code` folder and `README`
- Set up an RIA backup and associated GitLab sibling 
- Add licenses for data and code

## Installation 

### Requirements
- [DataLad](https://anaconda.org/conda-forge/datalad) 
- [python-gitlab](https://python-gitlab.readthedocs.io/en/stable/install.html) 

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
datalad clone -d . https://moo .datalad/procedures
```

4. Check installation was successful 

```
datalad run-procedure --discover
```
This should produce the following output
```
TO FILL
```

## Usage

Each procedure can be run individually or as a group.

### Running Individually 

#### Backup

##### Set up

Before running this procedure the user needs to do some set up. 
1. You will need a GitLab account. This procedure is currently configured to use the University of Southampton's [GitLab instance](https://git.soton.ac.uk) 
2. `python-gitlab` needs to be installed with `conda install -c conda-forge python-gitlab`
3. You will need to generate a personal access token for GitLab and define this in a `python-gitlab` config file. (Link to instructions for token here) 

Copy and paste the following into a text file, inserting your personal access token in the appropriate field:

	[soton] 
		url = https://git.soton.ac.uk
		private_token = [insert token here] 
		
Save this in your `home` directory (`~`) as `.python-gitlab.cfg`

##### Run the procedure 

Once you have completed the above set up, run the procedure from within your dataset with:

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

#### Add README

This procedure adds a `README` template to your dataset. From within your dataset, run

``` 
datalad run-procedure add-readme
```

#### Add gitignore

This procedure adds a `.gitignore` template to your dataset. From within your dataset, run

``` 
datalad run-procedure add-gitignore
```

#### Add code directory

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

This procedure is not included in the initial setup group as not all datasets will be shared and so need a license. Further, the licenses included might not be appropriate. 

This procedure adds a `LICENSE` file to the main dataset and to the `/code` folder. It adds a `CC-BY 4.0` license for the dataset and a `MIT` license for the code. 

If you plan to share your dataset, code, or both, and these licenses are appropriate, then from within your dataset, run

```
datalad run-procedure add-licenses
```


