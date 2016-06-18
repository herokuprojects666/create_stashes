import subprocess, os, re, argparse, itertools
from subprocess import PIPE

#grab the list of arguments provided in the script

parser = argparse.ArgumentParser(description='Parsing lists of arguments')
parser.add_argument('-l', nargs='+', dest='file_store', action='append', default=[])
results = parser.parse_args()

#output all the unstaged/untracked files

subprocess.Popen(["git", "add", "--all"]).wait()
value = subprocess.Popen(["git", "status"], stdout=PIPE)
output = value.communicate()

#create lists of new files/modified files and combined them into a single list

new_files = filter(lambda x : x.find('new file') != -1, output[0].replace('\t', '').split('\n'))
new_file_names = map(lambda x : list(reversed(x.split(':')))[0].strip(), new_files)
modified_files = filter(lambda x : x.find('modified') != -1, output[0].replace('\t', '').split('\n'))
modified_file_names = map(lambda x : list(reversed(x.split(':')))[0].strip(), modified_files)
total_list = list(itertools.chain(new_file_names, modified_file_names))

#create a list of file lists to iterate over

extracted_args = vars(results)
extracted_list = list(extracted_args['file_store'])
extracted_list.reverse()


for file_list in extracted_list:

    new_list = filter(lambda x : filter(lambda y : x.find(y) != -1, file_list), total_list)

    if new_list:

        subprocess.Popen(["git", "add", "--all"]).wait()

        for file in new_list:
            subprocess.Popen(["git", "reset", file]).wait()

        subprocess.Popen(["git", "commit", "-m", "'fake'"]).wait()

        subprocess.Popen(["git", "add", "--all"]).wait()

        subprocess.Popen(["git", "stash"]).wait()

        subprocess.Popen(["git", "reset", "head~"]).wait()


"""
#comment in back below this point to check out all the files with a certain name in the file path

filenames = []

def walkDirectory(arg1, dirname, files):
    cwd = os.getcwd()
    os.chdir(dirname)
    for file in files:
        if os.path.isfile(file):
            filenames.append(dirname + '/' + file)
    os.chdir(cwd)

os.path.walk('.', walkDirectory, [])

print 'files are ', ', '.join(map(str, filenames))

fileobjects = ' '.join(map(str, filenames)).split(' ')

#replace main.js with the file you're interested in
filtered = filter(lambda x :  list(reversed(x.split('/')))[0] == 'main.js', filenames)

print ', '.join(map(str, filtered))
"""