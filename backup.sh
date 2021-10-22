#!/bin/bash

# Procedure to create RIA-backup and GitLab siblings. 
# If these siblings already exist then they are skipped. 

set -e -u

echo "Creating RIA sibling..."
echo
echo "Please enter the URL for the RIA backup sibling e.g."
echo "ssh://ssh.soton.ac.uk:/research/datasets/"
read -p 'URL for RIA backup: ' riaurl

datalad create-sibling-ria -s ria-backup --existing skip ria+$riaurl

echo "Creating gitlab sibling..."
echo
echo "Please enter your GitLab project location. Should take the form of"
echo "<Project>/<dataset>"
read -p 'GitLab project location: ' gitlabproj

datalad create-sibling-gitlab -s gitlab --site soton --project $gitlabproj \
	--publish-depends ria-backup --existing skip
	
git config -f .datalad/config "datalad.get.subdataset-source-candidate-origin" \
	"ria+${riaurl}#{id}"

datalad save -m "Configure backup siblings and subdataset retrieval"
