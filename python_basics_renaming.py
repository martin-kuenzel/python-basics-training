#!/usr/bin/python3
import os

script_dir = os.path.realpath( os.path.dirname(__file__) )
testfiles_in = os.path.join(script_dir,'testfiles_input')
testfiles_out = os.path.join(script_dir,'testfiles_output')

print(f'''
I'm walkin through {testfiles_in} and copy-rename everything into {testfiles_out}
''')

for dirpath, dirnames, filenames in os.walk(testfiles_in,followlinks=False):

    for filename in filenames: 
        outdirpath = dirpath.replace(testfiles_in,testfiles_out)
        file_w_path_old = os.path.join(dirpath,filename)

        if os.path.isfile( file_w_path_old ) and filename.startswith('rename_me'):

            # create path for output only if there really are files to be copied residing in it
            os.makedirs(outdirpath, exist_ok=True)
            
            file_w_path_new = os.path.join( outdirpath, filename.replace('rename_me','me_renamed') )
            print(f'copy-renaming {file_w_path_old} to {file_w_path_new}')
            with open(file_w_path_old,'r',encoding='utf-8') as file_in:
                with open(file_w_path_new,'w',encoding='utf-8') as file_out:
                    file_out.writelines(file_in.readlines())

    if len(dirnames) > 0: 
        print(f'subdirectories {dirnames} are taken into account')
