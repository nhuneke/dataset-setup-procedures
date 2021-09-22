#!/bin/bash

# Include RIA backup and gitlab siblings here

set -e -u

echo "Creating RIA sibling..."
echo
read -p 'URL for RIA backup: ' riaurl

datalad create-sibling-ria -s ria-backup --existing skip ria+$riaurl

echo "Creating gitlab sibling..."
echo
read -p 'GitLab project location: ' gitlabproj

datalad create-sibling-gitlab -s gitlab --site soton --project $gitlabproj \
	--publish-depends ria-backup --existing skip
