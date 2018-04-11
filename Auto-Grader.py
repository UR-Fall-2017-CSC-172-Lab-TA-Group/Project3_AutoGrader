# Auto-Grader.py
# Created by Kelvin Ferreiras
# Created on Nov. 16, 2017
# Last Modification on Nov. 18, 2017
# This program autogrades project 3 for CSC-172 on Huffman encoding and decoding

import subprocess
import glob
import os
import shlex

currentFile = 'Auto-Grader'
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)

# Take the name of all the .zip files into a list
list_files=glob.glob(dirPath+ "/*.zip")

# Iterate on every .zip file
for currentFile in list_files:
    try:
        # Unzip the file
        name_of_file=os.path.basename(currentFile)
        subprocess.call(['unzip', '-o', ''+name_of_file])

        list_of_basename_elements = name_of_file.split('_', 5)
        dir_name=list_of_basename_elements[5].split('.')
        dir_name=dir_name[0]

        # Move files necessary for testing into working directory
        subprocess.call('cp ../Materials/BinaryIn.java ./', shell=True, cwd=dir_name)
        subprocess.call('cp ../Materials/BinaryOut.java ./', shell=True, cwd=dir_name)
        subprocess.call('cp ../Materials/Huffman.java ./', shell=True, cwd=dir_name)
        subprocess.call('cp ../Materials/HuffmanSubmitTest.java ./', shell=True, cwd=dir_name)
        subprocess.call('cp ../Materials/ur.jpg ./', shell=True, cwd=dir_name)
        subprocess.call('cp ../Materials/freq_key.txt ./', shell=True, cwd=dir_name)

        # Compile java files and run the test
        subprocess.call('javac *.java', shell=True, cwd=dir_name)
        subprocess.call('java HuffmanSubmitTest', shell= True, cwd=dir_name)

        grade = 0

        # Compare compressed and the decompressed output file with the original file
        cmd_pic = 'diff -s ur.jpg ur_decode.jpg'
        cmd_pic = shlex.split(cmd_pic)
        output_pic = subprocess.Popen(cmd_pic, stdout=subprocess.PIPE, cwd=dir_name).communicate()[0].rstrip().decode(
            'ascii')

        # If both files are identical, give full credit
        if (output_pic.__contains__('identical')):
            grade += 100
        # If both files are not identical, check if frequency table is correct. If so, give partial credit

        else:
            cmd_freq = 'diff -s freq.txt freq_key.txt'
            args_freq = shlex.split(cmd_freq)
            output_feq = subprocess.Popen(args_freq, stdout=subprocess.PIPE, cwd=dir_name).communicate()[0].rstrip().decode(
                'ascii')

            if (output_feq.__contains__('identical')):
                grade += 30

        # Record grade in the GradeBook text file
        gradebook = open('GradeBook.txt', 'a')
        gradebook.write("NetId: "+ list_of_basename_elements[2] + "    Grade: "+grade.__str__()+"\n")
        gradebook.flush()


    except FileNotFoundError:
        print("error")