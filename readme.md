Useful tool to separate a list of files into a bunch of different stashes. 

Currently, it does not support stashing files with different paths but identical filenames.

Example way to use it: 
python create_stashes.py -l file1 file2 -l file3 path/to

Any files that are not listed in any stash get put in the first stash. So, in this example, we would have at most 3 stashes. 

stash@{0} would contain any files not listed above.
stash@{1} would contain file1 and file2
stash@{2} would contain file3 and path/to
