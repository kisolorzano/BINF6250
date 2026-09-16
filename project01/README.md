# Introduction
This project takes a Variant Call Format (.vcf) file and detects if there are rare variants within the file by checking with the gnomAD database. If rare variants are found, it is checked with the names of the diseases associated with the variant. The final output is a readable file of the tallied number of occurrences that specific disease is observed. 

# Pseudocode
Put pseudocode in this box:

```
Input: .vcf file 
Output: the number of times the rare variant appears in various known diseases. 

Goal: Take a Variant Call Format file, parse the information to create a more readable file that lists the diseases tied to the rare variant. 
 
Pseudocode Steps 
1)	Utilize the template provided to understand which functions to use. 
2)	Input the source file into the directory with the script. 
3)	Create a function that takes the input of a string and remove the following 
  a.	Leading or trailing whitespaces
  b.	The tab-delimited values 
  c.	Meta-information 
4)	Focus on the INFO column for the information to be parsed, we want to extract information from AF_EXAC and CLNDLN
5)	Create a dictionary to store the information in. 
  a.	Remove the semi-colons to separate key-value pairs
  b.	Remove the equal sign to have separate keys and values
6)	Check for AF_EXAC key, noting that the data is a float. 
  a.	If there is no AF_EXAC keys in a line, continue checking each line 
  b.	Ensure that the data is a float and if the rare variant has a number <= to 0.0001
    i.	Check for CLNDLN key, if missing, return an empty list
      (1) Remove the pipe (|) to separate the diseases into a list
      (2) Filter and remove values that are "not specified" or "not provided"
      (3) Return a list of the results
7)	Read the source file to be inputted
  a. Create an additional dictionary to count the number of times a disease is observed. 
  b. Open the file 
  c.	Read the file line by line 	
    i.	Do NOT use readlines, use one that will read it one at a time, not all at once.
    ii. Ensure that when the file is read line by line, the count remains
  d.	Must go through the previous function- we want the function parse_line to be repeated with each line. 
  e.	Print the results when complete 

```

# Successes
Asynchronous Version Control (GitHub PR Workflow): The team executed a professional GitHub collaboration model. 
We built a structural baseline code with TODO blocks, allow other members to review, push executable code concurrently and then merge. 
We created, peer reviewed, offered correction and aligned pseudocode with our functional code. 

# Struggles
Github: As novel Github users, navigating the platform and learning all of its capabilities. We had trouble in the beginning on learning how to merge branches and commit changes. As the course continues on, we will probably endure some additional struggles, but this will be a learning experience. 

# Personal Reflections
## Group Leader: Kailey Solorzano
This project is a valuable exercise in collaborating across time zones, navigating GitHub, and emulating professional workflows of bioinformatics projects in industry. To construct a collaborative environment, each team member independently reviewed the project instructions to ensure a shared understanding of the objectives. Following the creation of a dedicated GitHub repository, we proceeded to work asynchronously toward project completion. A synchronous virtual meeting was held to discuss pull requests, address challenges encountered within GitHub, and establish a strategy for finalizing the project.

Throughout this process, I gained insight into how teams can work concurrently while maintaining effective communication, delivering constructive feedback at the group level, and employing diverse approaches to problem-solving. Additionally, I learned the importance of leveraging individual strengths and weaknesses to advance the project toward its best possible outcome.

## Other member: Trang Do 
I found the exposure to GitHub and collaborative workflows highly valuable. While the technical coding aspect of the assignment was straightforward, the real takeaway was learning how to code concurrently and integrate our changes seamlessly. For this project, I found it helpful to work asynchronously—understanding the project on our own time—and then meet to peer-review our work and navigate GitHub together. In the future, I anticipate encountering projects where live coding and real-time feedback are necessary, and I look forward to practicing that as well. My goal is to become well-versed in different collaboration styles and learn as much from them as possible.

# Generative AI Appendix
Used Claude AI (Sonnet 5) to navigate GitHub architecture, code review, and polish language. 
