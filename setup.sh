#!/bin/bash

echo "Running dataset setup..."

datalad run-procedure add-code
datalad run-procedure add-gitignore
datalad run-procedure add-readme
datalad run-procedure backup

datalad save -m "Initial dataset setup"