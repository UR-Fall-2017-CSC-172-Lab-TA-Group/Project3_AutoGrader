Auto-Grader for Project 3 of CSC-172 Data Structures and Algorithms

Created by Kelvin Ferreiras
Created on Nov. 16, 2017
Last Modification on Nov. 18, 2017


***************** DESCRIPTION ******************

This program automatically grades student submissions for project 3 of CSC-172 Data Structures and Algorithms on Huffman encoding and decoding. The python script takes zipped submission files from BlackBoards, uncompressed them, and then test their code. 

The testing is done by directing students' code to encode and decode a picture using Huffman trees. The script checks for the accuracy of the output by comparing the original picture with the resulting new picture after the encoding and decoding process. If the output is correct, full points are assigned. If not, the program checks if the frequency table used from constructing the Huffman tree is correct. If so, it assigns partial credit.

Finally, the grades are recoded in a text file.


***************** FILES *********************

*) Auto-Grader.py
	Python Script that conducts the grading
 
*) GradeBook.txt
	Text file used for recording grades

*) Materials

	*) BinaryIn.java
		Base code provided to students and necessary for testing

	*) BinaryOut.java
		Base code provided to students and necessary for testing

	*) Huffman.java
		Base code provided to students and necessary for testing


	*) HuffmanSubmitTest.java
		Test driver

	*) ur.jpg
		Picture used for testing

	*) freq_key.txt
		text file with expected output for the frequency table of the picture used for the test
		

***************** HOW TO RUN ***************** 

1) Get zipped submission files from BlackBoard's Assignment File Download option into the root of the AutoGrade directory.

2) Execute Auto-Grader.py through terminal

3) When execution ends, find grades GradeBook.txt .

Note: Erase all content of GradeBook.txt before each run


***************** INPUT FORMAT *****************

Input will be zipped submission files from BlackBoard's Assignment File Download option in the root of the AutoGrade directory.  

A sample submission file looks like the following:

	Project_3_ jdoe10_attempt2_2017-10-24-13-22-06_Proj3.zip 

Breaking its name down by underscores, form left to right, its components are:

1) Type of assignment
2) Number of assignment
3) Student's NetID
4) Number of assignment
5) Date and Time of submission
6) Name of directory zipped into the file

***************** OUTPUT FORMAT **************** 

Output will be recorded in GradeBook.txt. This text file will have two columns of information:

	First Column	Second Column
	(NetID)		(Grade)

Ex: Student with NetID jdoe10 scores a grade of 100 points, output will look as the following:
	
	jdoe10		100

***************** SAMPLE INPUT **************** 

Five sample zipped submission files are provided here:

	*) 4 of them are fully correct implementations of the project.

	*) 1 of them have faulty encode and decode methods, but produces a correct frequency table.
