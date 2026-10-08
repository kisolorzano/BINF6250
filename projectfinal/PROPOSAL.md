# __Profiling HMMs for Antibiotic Resistance__

---

## __Research Question__

*Description*: Beta-lactamase is an enzyme produced by bacteria that reduces and destroys the efficacy of beta-lactamase antibiotics such as penicillin. The use of a profile Hidden Markov Model will detect divergent family members within beta-lactamase to determine which class causes antibiotic resistance on the protein-level.   


*Reasoning*: Antibiotic resistance is a persistent issue within Public Health due to overuse and misuse, ceasing a treatment when a patient "feels better" and within current agricultural practices. Hospitals and clinical settings often perform bacterial sequencing of genes to detect the resistant genes and new variants. This provides a basis for creating and understanding antibiotics. With Bioinformatics, a common issue is reproducibility. By generating a result similar to existing papers, this can validate current research findings. 

*Algorithm Class*: Hidden Markov Models, Dynamic Programming 

*Algorithm*: Profile-HMMs, Viterbi Algorithm 

*Justification*: 

A profile HMM will provide a comparison between each of the beta-lactamase classes- A, B, C and D. Class A is known to cause antibiotic resistance. This algorithm will provide insight into the homology of the classes and will maximize the data sets to view patterns and conservation. 

A Viterbi Algorithm is a dynamic programming technique used in HMMs, which is used to determine the most likely order of hidden states. The use of this algorithm will be to identify the mutations and or structural variations in beta-lactamase as well as determine evolutionary relationships between classes of the enzyme. 

## __Data Plan__

*Database*: The Comprehensive Antibiotic Resistance Database. (CARD)

*Data type*: FASTA files- (will include details later)

Paper Supplement(s): 

Keshri, V., Panda, A., Levasseur, A., Rolain, J. M., Pontarotti, P., & Raoult, D. (2018). Phylogenomic Analysis of β-Lactamase in Archaea and Bacteria Enables the Identification of Putative New Members. Genome biology and evolution, 10(4), 1106–1114. https://doi.org/10.1093/gbe/evy028

Silveira, M. C., Azevedo da Silva, R., Faria da Mota, F., Catanho, M., Jardim, R., R Guimarães, A. C., & de Miranda, A. B. (2018). Systematic Identification and Classification of β-Lactamases Based on Sequence Similarity Criteria: β-Lactamase Annotation. Evolutionary bioinformatics online, 14, 1176934318797351. https://doi.org/10.1177/1176934318797351

Synthetic Data: 

*Licensing or access considerations*: CARD + analyzing the FASTA sequence

A brief “prototype data” plan:
What minimal dataset you will use early on for testing and debugging.
How this prototype relates to your ultimate, more realistic dataset.

## __Success Criteria__
Define what “success” looks like for your project:

*Expected outputs*: To create a Profile Model of the different classes of enzymes. Other outputs should include statistical significance, the Viterbi path and pairwise sequence alignments. 

The reasonable result will be in comparison to the paper supplements who conducted similar experiments. 

## __Pitfall Scan__

*Data-related issues*: (e.g., noisy or biased data, missing annotations).

1. Many bacterial datasets from various different databases
   
   Reasoning:

   Strategy:
    
3. issue
   
   Reasoning:

   Strategy:
   
3. issue

   Reasoning:

   Strategy:

*Algorithmic issues*: (e.g., runtime or memory blowup, numerical stability, sensitivity to parameters).

1. issue

   Reasoning:

   Strategy:
   
2. issue
   
   Reasoning:

   Strategy:
   
3. issue

   Reasoning:

   Strategy: 
   
*Evaluation issues*: (e.g., no ground truth, risk of overfitting, misleading metrics).

1. issue
   
   Reasoning:

   Strategy:
   
2. issue
   
   Reasoning:

   Strategy:
   
3. issue
   
   Reasoning:

   Strategy: 
   

## __Planned Repository Structure (Initial Sketch)__

- README / Proposal
- Data Folder
  * FASTA files of datasets selected
- Algorithms Folder
  * Jupyter Notebook of the prototyped code
  * Python scripts of individual functions


## __Generative AI Disclosure (If Used)__
