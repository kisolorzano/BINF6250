# Introduction
This project takes a Variant Call Format (.vcf) file and detects if there are rare variants within the file by checking with the gnomAD database. If rare variants are found, it is checked with the names of the diseases associated with the variant. The final output is a readable file of the tallied number of occurrences that specific disease is observed. 

# Pseudocode
Put pseudocode in this box:

```
Input: .vcf file 
Output: results of the diseases associated with the variant and its quantification of how much it appears. 

Goal: Take a Variant Call Format file and parse the information to create a more readable file that lists the diseases tied to the rare variant. 
 
Pseudocode Steps 
1)	Utilize the template provided to understand which functions to use. 
2)	Input the source file into the directory with the script. 
3)	Read the .vcf line by line and remove any extra information
  a.	Leading or trailing whitespaces
  b.	The tab-delimited values 
  c.	Meta-information 
4)	 Focus on the INFO column for the information to be parsed 
5)	Create a dictionary to store the information in. 
  a.	Remove the semi-colons to separate key-value pairs
  b.	Remove the equal sign to have separate keys and values
6)	Check for AF_EXAC key, noting that the data is a float. 
  a.	If there is no AF_EXAC key, end the process 
  b.	Ensure that the data is a float and if the rare variant has a number >= to 0.0001
    i.	Create a list of the associated diseases in CLNDN 
    ii.	Remove values that are “not specified” or “not provided”
  c.	If the variant is not rare, create an empty list
7)	Check for the CLNDLN key, nothing that the data are strings
  a.	If there is no CLNDLN key, end the process
  b.	With the diseases that are pipe separated, remove them. 
8)	Read the source file to be inputted
  a.	Open the file 
  b.	Read the file line by line 	
    i.	Do NOT use readlines, use one that will read it one at a time, not all at once. 
  c.	Must go through the previous function- we want the function parse_line to be repeated with each line. 
  d.	Create another dictionary to count the number of times a disease is observed 
  e.	Print the results when complete 

```

# Successes
Asynchronous Version Control (GitHub PR Workflow): The team executed a professional GitHub collaboration model. 
We built a structural baseline code with TODO blocks, allow other members to review, push executable code concurrently and then merge. 
We created, peer reviewed, offered correction and aligned pseudocode with our functional code. 

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member: Trang Do 
I found the exposure to GitHub and collaborative workflows highly valuable. While the technical coding aspect of the assignment was straightforward, the real takeaway was learning how to code concurrently and integrate our changes seamlessly. For this project, I found it helpful to work asynchronously—understanding the project on our own time—and then meet to peer-review our work and navigate GitHub together. In the future, I anticipate encountering projects where live coding and real-time feedback are necessary, and I look forward to practicing that as well. My goal is to become well-versed in different collaboration styles and learn as much from them as possible.

# Generative AI Appendix
Used Claude AI to navigate Git architecture and code review. 
