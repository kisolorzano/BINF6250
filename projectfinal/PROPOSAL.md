# __Profiling Hidden Markov Models for Antibiotic Resistance__

## __Research Question__

*Description*: Beta-lactamase is an enzyme produced by bacteria that reduces and destroys the efficacy of beta-lactamase antibiotics such as penicillin. The use of a profile Hidden Markov Model (HMM) vgt5 will detect divergent family members within beta-lactamase to determine homologous evolutionary relationships between classes that identify potential resistant genes. 


*Reasoning*: Antibiotic resistance is a persistent issue within Public Health due to overuse, misuse, stopping a treatment preemptively and within current agricultural practices. Hospitals and clinical settings often perform bacterial sequencing of genes to detect the resistant genes and new variants. This provides a basis for creating and understanding antibiotics. With Bioinformatics, a common issue is reproducibility. By generating a result similar to existing papers, this can validate current research findings. 

*Algorithm Classes*: Hidden Markov Models, Dynamic Programming 

*Algorithms*: Profile-HMMs, Viterbi Algorithm 

*Justification*: 

A profile HMM will provide a comparison between each of the beta-lactamase classes- A, B, C and D. Class A is known to cause antibiotic resistance. This algorithm will provide insight into the homology of the classes and will maximize the data sets to view patterns and conservation of genes. 

A Viterbi Algorithm is a dynamic programming technique used in HMMs, which is used to determine the most likely order of hidden states. The use of this algorithm will be to identify the mutations and or structural variations in beta-lactamase as well as determine evolutionary relationships between classes of the enzyme. 

## __Data Plan__

*Databases*: The Comprehensive Antibiotic Resistance Database (CARD), National Center for Biotechnology Information (NCBI)

*Data type*: FASTA files

*Paper Supplement(s)*: 

Keshri, V., Panda, A., Levasseur, A., Rolain, J. M., Pontarotti, P., & Raoult, D. (2018). Phylogenomic Analysis of β-Lactamase in Archaea and Bacteria Enables the Identification of Putative New Members. Genome biology and evolution, 10(4), 1106–1114. https://doi.org/10.1093/gbe/evy028

Silveira, M. C., Azevedo da Silva, R., Faria da Mota, F., Catanho, M., Jardim, R., R Guimarães, A. C., & de Miranda, A. B. (2018). Systematic Identification and Classification of β-Lactamases Based on Sequence Similarity Criteria: β-Lactamase Annotation. Evolutionary bioinformatics online, 14, 1176934318797351. https://doi.org/10.1177/1176934318797351

*Synthetic Data*: None at this moment. Once the pseudocode is written, there will be drafted synthetic data to mimic several seqeunces. 

*Licensing or access considerations*: 

- Using Explorer for sequence alignment tools.
- Citing databases with proper citation for using certain datasets.
- *Question*: In several papers, there is mention of using the HMMER tool, would the goal be to create something similar? 

*A brief “prototype data” plan*:

For testing and debugging, 

- I will start with synthetic data (or a Toy Alignment) similar to the data we used in Project 04.
- Classes of beta-lactamases each have different genetic origins. For example in Class A, TEM-1 is inherent to *E. Coli* and SHV-1 is inherent to *K. pneumoniae*. As a secondary test data-set, I would test different variations of the enzyme within the class.


The prototype relates to the real, more complex dataset because it provides a solid foundation to test the initial code. It breaks the complexity of  algorithmic thinking into smaller more reasonable problems. Starting with a Toy Alignment builds the core of each function without having to deal with the large overload of data as the initial input. With the prototype data, this will provide clarity in conceptual learning of Profile HMMs and Dynamic Programming, create a visible code to debug, and maximize optimization. 

## __Success Criteria__

*Define what “success” looks like for your project*: Success for my project will be producing some type of output. Ideally, the output would be the Profile HMM for the various classes of beta-lactamases. Along the way, I would also like to produce sample outputs from the test data to visualize each step for myself and the reviewer. True success for me is defined as being able to understand the project conceptually and create a functioning algorithm. Currently, there are tools that facilitate running these algorithms, but being able to take a step back and understand the origin creates a new level of thinking when answering complex biological questions. 

*Expected outputs*: To create a Profile Hidden Markov Model of the different classes of enzymes. Other outputs should include statistical significance, the Viterbi path and pairwise sequence alignments. 

The reasonable result will be in comparison to the paper supplements who performed similar analyses. A final comparison will be utilizing the HMMER tool as used within the papers. 

## __Pitfall Scan__

*Data-related issues*: 

1. Redundancy of Datasets- overrepresentation of many bacterial datasets from various different databases. 
   
   Realistic Concern: Databases such as CARD can have an overrepresentation of dominant types of beta-lactamase enzymes such as TEM. Testing for rarer variants may be difficult as they are not sequenced as often. 

   Strategy: With downloading multiple datasets, it may be best to remove duplicates and possibly use some type of cluster technique. 
    
2. Alignment of Sequences- the quality of the multiple alignment. 
   
   Realistic Concern: During multiple sequence alignment, errors can lead to false homologous match states.  

   Strategy: Verify with toy alignment data of the known confirmed conserved regions. If time permits, possibly comparing alignment tools to produce the best output. 
   
3. Annotation Errors- inconsistencies in annotation can cause unwanted noise in the dataset. 

   Realistic Concern: Public sequencing datasets are not always the most accurate- there can be partial fragmented sequences or mislabeled sequences that increases noise in the dataset. 

   Strategy: (I am still trying to figure this out, but here is my idea) Using datasets from two different databases as the positive test for beta-lactamase and another database for the negative test, not beta-lactamase. 

*Algorithmic issues*: (e.g., runtime or memory blowup, numerical stability, sensitivity to parameters).

1. Overfitting the Model - the datasets have too many pre-existing parameters

   Realistic Concern: A limited amount of sequences can cause overfitting. The scores of the matrix will be high, but this may not result in complete accuracy. 

   Strategy: Develop a pseudocount that is proportional to the protein sequences, similar to how 0.25 is often a pseudocount for nucleotides. 
   
2. Global vs Local Alignment 
   
   Realistic Concern: Protein sequences contain additional components such as signal peptides and domains. 

   Strategy: (I believe I need to do further research here too) Would this be similar to Markov chains in that I should create an artificial start and end state? 
   
3. Silent Delete States

   Realistic Concern: There is no residue produced during the delete states. If computational analysis is incorrect, it can miscalculate the states required for the profile HMM. 

   Strategy: Starting with the test data, calculate by hand to test this out visually before constructing the code. 
   
*Evaluation issues*: (e.g., no ground truth, risk of overfitting, misleading metrics).

1. Comparison to HMMER - HMMER utilizes different statistical parameters and weights 
   
   Realistic Concern: HMMER a standard of statistical analysis that can differ from creating an algorithm project from scratch. By trying to conduct a true match, may lead to additional errors on my personal end. 

   Strategy: Honestly, I am unsure what to do here. I need to look more into HMMER. 
   
2. Comparison of Family of Enzymes measures homology and detects for the beta-lactamase genes not strictly for resistance
   
   Realistic Concern: The profile HMM detects homologous relationships; however this does not explicitly state the resistant genes. A detected gene here does not automatically mean antibiotic resistance. 

   Strategy: Pivot the goal to identify potential resistant genes rather than the phenotype. Future analysis would be to use phenotype data to test for resistance. 
   
3. Profile HMM Result vs Pairwise Alignment Result - pairwise alignment serves as the baseline in comparison to the profile HMM
   
   Realistic Concern: Pairwise Alignment is often used as a baseline; however with the profile HMM, this will provide a conflicting assessment. The pairwise will be limited to a single sequence and profile HMM will be using all the training sequences. 

   Strategy: Use Smith-Waterman algorithm? 
   

## __Planned Repository Structure (Initial Sketch)__

- README / Proposal
- Data Folder
  * FASTA files of datasets selected
- Algorithms Folder
  * Jupyter Notebook of the prototyped code
  * Python scripts of individual functions


## __Generative AI Disclosure__

This proposal came from original thought. No AI was used at this time. 
