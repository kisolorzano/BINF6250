# Introduction
Markov Chains are multiple series of states that transition between one another. Each Markov chain is dependent on the _Markov Property_ in that the sequential states is not dependent on the previous state and a probabilisitic prediction is made to predict the next state. 

This code, written using Jupyter Notebooks breaks down modeling Markov Chains with Seussian text. The ```build_markov_model``` function constructs the Markov model and displays the nth order. The ```get_next_word```  and ```generate_random_text``` functions calculate the conditional property that will predict the next word (state) from the text to create a string of words. Following these functions, we begin with sample text from Dr. Seuss's book "One Fish, Two Fish, Red Fish, Blue Fish." If there are no errors with the code, we proceed with running the entirety of the book. To further train the Markov model, I used all of Shakespearean sonnets to analyze.   

# Pseudocode
Put pseudocode in this box: 

```
def build_markov_model():
  CREATE initial (beta) and end state
  CREATE a loop to measure the length of words
  CREATE conditions for the Markov model
  INCREMENT the Markov model

def build_markov_model() - Nth Order:
  ALTER code from previous function to include the Nth order (the order is a mutable value) 
  MODIFY variable to represent the various states
  MODIFY variable to represent the prediction for the next word

def next_word():
  CALCULATE conditional probabilities between state transitions
  USE np.random.choice to simulate the random predictions

def generate_random_text():
  CREATE the random text based on the text given
  BREAK if the text reaches the end state

*One Fish, Two Fish, Red Fish, Blue Fish*
  OPEN the source text
  RUN the functions created

*Choice of Text*
  CREATE function to clean up the source text
    SONNET CRITERIA: 14 lines, 10 syllables each, 3 quatrains and 1 couplet, ABAB CDCD EFEF GG rhyme scheme
    MY ATTEMPT: 14 lines + inclusion of old English language (e.g. ov'er) 
  OPEN the source text
  RUN function to manipulate the data
  RUN Markov model functions 
```

# Successes
Concept Comprehension: I was able to comprehend the project at hand and develop pseudocode as a foundation for my concrete code. I have provided a state diagram of the text "One Fish, Two Fish, Red Fish, Blue Fish". I attempted to emulate a state diagram for the Shakespearean sonnets, but came to realize quick that this would be to complex. 

Creation of Pseudocode: The pseudocode was tough to create despite the template given. I broke it down by function and tried to integrate coding language with the concepts. 


# Struggles
Independent Work: During the Add/Drop period, both of my initial group mates dropped the course. This led to challenges in logistics and expectations of my involvement of the project. Completing this project as an individual created a struggle in time management.  

Completion of Project: The current project remains incomplete and does require future revisions. Completing the project is a current struggle as I try to navigate generating the code.  

Generating Code: My background is not in coding and my experience stems from the coding courses provided from this program. I think part of me was ambitious to try and take on sonnets as well as they have complex criteria, from deciphering old English language, a rhyming scheme and a specific format. Also, this is my first time using Jupyter Notebooks, which posed as an initial challenge.  


# Personal Reflections
## Group Leader
The overall project was difficult to complete as an individual. The unfortunate situation at hand allowed me to reflect and apply this situation to real-world contexts. By attempting this project by myself, I was able to learn about resilience, project management and adaptability. In comparison to the real-world, there are opportunities for collaboration that may fall through (e.g. a person is unable to be on the project due to an already existing overbearing workload or a person goes on unexpected leave and takes a time of absence). This project also allowed me to personally assess my coding capabilities and where I can seek improvement. 

I am open to all feedback within the peer review process as I have mentioned that this project is incomplete. After meeting with the Professor, I was reassured about the expectations of what I am required to turn in. I believe given the time frame and the circumstances, I was able to make a significant amount of progress. Moving forward, I hope to improve my communication about my involvement in the project and improve my technical coding skills in Python. 

# Generative AI Appendix
As per the syllabus
