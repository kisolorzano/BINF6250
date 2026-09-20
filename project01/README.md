# Introduction
This project takes a Variant Call Format (.vcf) file and detects whether there are rare variants within the file by checking against the AF_EXAC database. If rare variants are found, it is checked against the names of the diseases associated with the variants. The final output is a dictionary containing each disease name mapped to the number of times it appears across all rare variants in the VCF file. 

# Pseudocode
```
Input: .vcf file (file name clinvar_20190923_short.vcf is hardcoded into the template)
Output: a dictionary mapping each valid disease name to the number of times it appears across all rare variants in the VCF file.

Goal: Take a Variant Call Format file, parse the information to create a more readable file that lists the diseases tied to the rare variant. 
 
Pseudocode Steps 
1)	Utilize the template provided to understand which functions to use. 
2)	Input the source file into the directory with the script. 
3)	Create a function called parse_line() that takes the input of a string and does the following:
  a. Skips parsing meta-information lines that start with ## and CHROM header that starts with #
  b. Splits the line into columns based on tabs (\t) and strips leading or trailing whitespaces
  c. Filters out lines with fewer than 8 columns 
4)	The parse_line() function also identifies the INFO column and splits it by semicolon to get key-value pairs; we want to extract information from AF_EXAC and CLNDN
5)	The parse_line() function then creates a dictionary to store the key-value pairs and does the following:
  a.	Splits each paired list member by the equal sign 
  b.	Assigns the key and value each to the dictionary
6)	The parse_line() function then checks for AF_EXAC key, noting that the data is a float. 
  a.	If there is no AF_EXAC key in a line, return an empty list for this line. 
  b.	Convert the string data to a float and check if the rare variant has a number < 0.0001
    i.	If the number is < 0.0001, check for CLNDN key; if missing, return an empty list. If it exists, do the following:
      (1) Separate the diseases into a list by the pipe (|) 
      (2) Add diseases that are not "not specified" or "not provided" to the ongoing list of valid diseases
      (3) Return the list of valid diseases
    ii. If the number is >= 0.0001, return an empty list
7)	Create a read_file() function to read the VCF source file line by line and count the occurrences of rare diseases using the parse_line() function previously created. This function does the following:
  a. Creates an additional dictionary that will map each disease name to the number of times it is found
  b. Opens the file and reads it line by line
    i.	Do NOT use readlines; use one that will read it one at a time, not all at once.
    ii. Ensure that when the file is read line by line, the count remains
  c.	For every line in the vcf file, we run the parse_line() function and assign the output list to a new variable.
  d. For every disease in that list, we see if it is a key in the disease_counts dictionary
    i. If it exists in the dictionary, we will increase the value by 1 to show another occurrence
    ii. If it does not exist in the dictionary, we will create a new key with the disease name with the value 1.
  e.	Print the dictionary containing the disease names and the number of times they show up.

```
# Output / Results 
The output to the console is as follows: 
```
*insert output here*
```
# Successes
Asynchronous Version Control (GitHub PR Workflow): The team executed a professional GitHub collaboration model. 
We built a structural baseline code with TODO blocks, allowing other members to review, push executable code concurrently, and then merge. 
We created, peer-reviewed, offered corrections, and aligned pseudocode with our functional code. 

# Struggles
GitHub: As novel Github users, navigating the platform and learning all of its capabilities. We had trouble in the beginning learning how to merge branches and commit changes. As the course continues, we will probably endure some additional struggles, but this will be a learning experience. 

# Personal Reflections
## Group Leader: Kailey Solorzano
This project is a valuable exercise in collaborating across time zones, navigating GitHub, and emulating professional workflows of bioinformatics projects in industry. To construct a collaborative environment, each team member independently reviewed the project instructions to ensure a shared understanding of the objectives. Following the creation of a dedicated GitHub repository, we proceeded to work asynchronously toward project completion. A synchronous virtual meeting was held to discuss pull requests, address challenges encountered within GitHub, and establish a strategy for finalizing the project.

Throughout this process, I gained insight into how teams can work concurrently while maintaining effective communication, delivering constructive feedback at the group level, and employing diverse approaches to problem-solving. Additionally, I learned the importance of leveraging individual strengths and weaknesses to advance the project toward its best possible outcome.

## Other member: Trang Do 
I found the exposure to GitHub and collaborative workflows highly valuable. While the technical coding aspect of the assignment was straightforward, the real takeaway was learning how to code concurrently and integrate our changes seamlessly. For this project, I found it helpful to work asynchronously—understanding the project on our own time—and then meet to peer-review our work and navigate GitHub together. In the future, I anticipate encountering projects where live coding and real-time feedback are necessary, and I look forward to practicing that as well. My goal is to become well-versed in different collaboration styles and learn as much from them as possible.

## Other member: Katelyn DSouza
I found this project to be a good introduction to using GitHub for collaborating with other bioinformaticians on a workflow. The coding task itself was relatively straightforward, but there was a bit of a learning curve working with repositories and managing pull requests for the first time. Since this project was simpler, we decided to each work on the code independently, giving everyone a chance to attempt it without help. Our virtual meeting was then crucial for ensuring all pull requests were merged correctly and for putting together a plan to complete the README.
I am looking forward to live coding with future groups as the algorithms become more challenging, since working with a group can allow us to build on each other's ideas and learn more deeply. Overall, this process allowed me to learn how to better work with a team and communicate effectively, especially across different time zones and remotely, to create a strategy, adapt it when necessary, and still practice writing code independently.

# Generative AI Appendix
Used Claude AI (Sonnet 5) to navigate GitHub architecture, code review, and polish language. 
