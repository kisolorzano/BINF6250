# Conceptual Progress Report 

## Recap 

From the original proposal, I have altered my final project to reflect a passion subject of mine: public health. I will be altering the proposal to the new proposed changes. Here is a brief summary: 

The Aho-Corasick Algorithm is a combinatorial algorithm, similar to Burrows-Wheeler Transform, that focuses on pattern matching a set of 'words' in an input text without having to restart the search for each word. Within Bioinformatics, we can implement this algorithm to search for series of distinct genetic or protein sequences within a massive genome in a single search. Antimicrobial resistance (AMR) is a persistent issue within public health due to rapid mutations selective pressure. With this algorithm I propose to try and identify specific resistance genes found within a single bacterial genome. 

## Inputs, Outputs and Assumptions 

* The expected input:
  * FASTA file, containing known AMR genes
  * FASTA file, bacterial genome
* The expected output:
  * Name of gene
  * Match location
* Key Assumptions:
  * All sequences are uppercase and ambiguous nucleotides are removed.
  * Resistance gene sequences are corrected annotated.
  * Exact sequence matching is used.
  * The trie has a single root node.
  * The patterns being searched are inserted into the trie prior to searching.
  * Several genes may match at the same genomic position.
  * The genome being scanned is being treated as one large string. 

## Pseudocode 

```
class AhoCorasick:

  def __init__(self):
    # Initialize TrieNode attributes
    self.children = {} # dictionary of character and child nodes
    self.output = [ ] # list of matching patterns
    self.fail = None # failure / suffix link

  def build_trie(patterns):
    """
    Build trie from CARD AMR gene sequences.

    Data Structures:
      - trie
      - dictionary of children nodes
      - output list at base nodes
    """

    if patterns is empty

      return empty trie 

    initialize root node

    for each pattern in patterns

      set current to root

    for each character in pattern

      if character not in A, C, G, T

        continue

      if character not in current.children

        create new node

        add node to current.children

      current <- current.children[character]

    append pattern to current.output

    return root

  def build_failure_links(root):
  """
  Construct failure links using Breadth-First Search.

  Data Structures:
  - Queue
  - Trie
  - Failure links
  """

  initialize empty queue

  root.fail <- root

  for each child of root

    child.fail <- root

    enqueue child

  while queue is not empty

    current <- dequeue

    for each character, child in current.children

      fallback <- current.fail

      while fall back does not equal root and character not in fallback.children

        fallback <- fallback.fail

      if character in fallback.children

        child.fail <- fallback.children[character]

      else

        child.fail <- root

      enqueue child

    return root

def build_output_links(root):
    """
    Merge outputs from failure links.
    Data Structures:
      - Queue
      - Output lists
    """

    initialize queue

    add all root children to queue

    while queue is not empty

      current ← dequeue

      current.output ←
        current.output ∪ current.fail.output

      for each child in current.children

        enqueue child

    return root


  def build_automaton(patterns):
    """
    Construct complete Aho-Corasick automaton.
    """

    root ← build_trie(patterns)

    if trie is empty

      return root

    build_suffix_links(root)

    build_output_links(root)

    return root


  def search_mech(genome, patterns):
    """
    Search genome for AMR gene sequences.
    Data Structures:
      - Automaton
      - Dictionary of matches
    """

    if genome is empty

      return empty result

    root ← build_automaton(patterns)

    initialize result dictionary

    current ← root

    for position from 0 to length(genome)-1

      character ← genome[position]

      if character not in {'A','C','G','T'}

        current ← root

        continue

      while current ≠ root
            and character not in current.children

        current ← current.fail

      if character in current.children

        current ← current.children[character]

      else

        current ← root

      if current.output is not empty

        for each matched_pattern in current.output

          append match location to result

    return result


  def report_matches(result):
    """
    Report detected AMR genes and locations.
    """

    if result is empty

      print "No AMR genes detected."

    else

      for each gene in result

        print gene name

        print match positions


if __name__ == "__main__":

  load CARD AMR gene sequences

  load genome sequence

  root ← build_automaton(patterns)

  matches ← search_mech(genome, patterns)

  report_matches(matches)
  

```

## Complexity and Bottlenecks 

Time Complexity: 

``` O(n), O(m+z) ```

Space Complexity: 

``` O(m+z) ```

Variables Explanation: 

n = length of the text being searched 
m = total length of all the patterns 
z = number of matches reported

Most Expensive Parts of the Algorithm 

1) Trie Construction: increases memory consumption and automaton construction time.
   * FASTA files are large
   * Many resistance genes on a bacterial genome
2) Genome Search: large datasets require substantial runtime
3) Storing Matches: requires a large memory
  * frequent patterns = many match locations = more storage
  * repetitive sequences

Possible Solutions for Improving Performance 

1) Index Only Relevant Genes
2) Store Match Counts rather than Position Index
3) Parallel Processing (I believe we learned something like this in BINF6310) 

## Validation and Testing Plan 

**Hand-crafted Example:** 

Input Patterns: ACT, CAT, CTG, TGA 

Test Genome: ACTGACTGA

Expected Output: 
* "ACT found at positions 0 + 4"
* "CTG found at positions 1 + 5"
* "CAT is not found"
* "TGA found at positions 2 + 6"

Validation Reasoning: 
1) Tests the trie
2) Tests the failure links (if they are connected to the correct nodes)
3) Tests for overlaps and multiple patterns can be reported

**Edge Case Example:**

Input Patterns: [ ] 

Test Genome: ACTGACTGA

Expected Output: 
* "No matches found"

Validation Reasoning: 
1) Check for empty arguments
2) Tests for errors or inconsistences

**Real Data:**

Input Patterns: example of a known resistance gene like mecA 

Test Genome: bacterial reference genome 

Expected output: 
* Location and identity of resistant gene

Validation Reasoning: 
1) Tests on a smaller scale before the larger input 

## Updated Pitfall and Risk Log 

**Data-Related Issues**

1. Redundancy of Datasets
* The CARD database will have highly similar variants of resistant genes
* Consequence: Larger tries, increased memory, nearly identical matches
* Strategy: Remove exact duplicates, track gene families rather than individuals

2. Annotation Errors
* The CARD database may have partial genes, fragmented sequences, mislabeling
* Consequence: Aho-Corasick algorithm will produce an incorrect output
* Strategy: Remove short or fragmented sequences, validate with another database

**Algorithmic-Related Issues**

1) Exact Match Sensitivity 
* The algorithm requires an exact 100% match
* Consequences: Any indels or SNPs and a match can be missed
* Strategy: Disclose the caveat in full transparency

2) Memory Consumption
* Can create a large trie
* Consequences: Running out of storage
* Strategy: Restrict analysis to one AMR family (e.g. beta-lactamase)

**Evaluation Issues**

1) Gene Detection vs Resistance Phenotype
* Detection of a resistance gene does not equal antibiotic resistance phenotype
* Consequence: Will obscure the evaluation of the data
* Strategy: Disclose the caveat in full transparency

2) Comparison to Pairwise alignment
* Detection of exact sequences
* Strategy: Introduce mutations and compare with algorithms such as Smith-Waterman

## Unknown Terms -> Dictionary / Resources 
_Use if needed, I will personally be referring back to these so I have left them here_

* Aho-Corasick Algorithm: https://www.youtube.com/watch?v=XWujo7KQL54&t=632s 
* Breadth-First Search: https://www.codecademy.com/article/breadth-first-search-bfs-algorithm
* Queue / Enqueue in Python: https://medium.com/analytics-vidhya/queue-deque-overview-and-its-implementation-in-python-c36c56b532b8

## Generative AI Disclosure
Used Claude AI, Opus 5. [large language model] to help with formatting the pseudocode, especially with understanding object-oriented programming. 

Justification: I feel that OOP is a useful skill and one that I am still learning about. I am trying to be ambition and learn more about classes and how they work. 
