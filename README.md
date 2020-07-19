# Charles The Chatbot

## Changes
For this project, I made an (almost) complete system overhaul from A2. The conversation agent has been completely changed along with a handful of added features from the "buffet" of features.

### Object Dependencies
(question_answers.pickle / root_dict.pickle / sent_tokenizer.pickle)
Pickled objects referenced throughout the project.
Question_Answers for the conversation topics and questions/answers.
root_dict to keep the language uniform between user input and stored question/answers.
sent_tokenizer used to tokenize sentences into an array of words.

### Config
(config.py)
Initialize/Update pickle dependencies.

### GUI
(GUI.py)
Simple Tkinter GUI that uses a message frame to display the chat history.

Alot of the source code is refactored from this article with the server components stripped: https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170

### Spell Checker
(spell.py)
Peter Norvig's Spell Corrector: http://norvig.com/spell-correct.html
This is an implementation of Norvig's spell corrector algorithm, is used to check spelling of user input, used along with POS Tagger.

### Tag and Tokenize / POS Tagger
(tagNtokenize.py)
This is used to tokenize a string into an array of words. And then loops over the array and double checks the spelling of each word in the list. Then using NLTK's POS Tagger, the tokenized string is then tagged with the following tags:

*Courtesy of sentdex (pythonprogramming.net)*

        CC Coordinating conjunction
        CD Cardinal number
        DT Determiner
        EX Existential there
        FW Foreign word
        IN Preposition or subordinating conjunction
        JJ Adjective
        JJR Adjective, comparative
        JJS Adjective, superlative
        LS List item marker
        MD Modal
        NN Noun, singular or mass
        NNS Noun, plural
        NNP Proper noun, singular
        NNPS Proper noun, plural
        PDT Predeterminer
        POS Possessive ending
        PRP Personal pronoun
        PRP$ Possessive pronoun
        RB Adverb
        RBR Adverb, comparative
        RBS Adverb, superlative
        RP Particle
        SYM Symbol
        TO to
        UH Interjection
        VB Verb, base form
        VBD Verb, past tense
        VBG Verb, gerund or present participle
        VBN Verb, past participle
        VBP Verb, non­3rd person singular present
        VBZ Verb, 3rd person singular present
        WDT Wh­determiner
        WP Wh­pronoun
        WP$ Possessive wh­pronoun
        WRB Wh­adverb


### Correlation Coefficient
(correlation_cf.py)
This is the algorithm designed to take in to lists tokenized and tagged strings and computes a coefficient over the interval [0, 1] that denotes the similiarity/correlation between them. This is used to cross-reference the user input with question answers and returns the answer associated with the question with the highest correlation coefficient.

## List of Features
### Created Simple GUI
	As discussed above.
### Added extra topics into config quesiton_answers
	Charles can talk a bit about basketball along with more details on the football topic, and some superficial conversations for other sports.
### Add Spell Checker that corrects user inputs to most closest answer
	As discussed above.
	There isn't sample conversation, this is more behind the scenes. It corrects the misspelled words and computes the correlation coefficient using the corrected words.
### POS Tagger
	This was implemented in Assignment 2, but utilized along with spell checker and Named Entity Recognition. The tagged list is used in the correlation coefficient algorithm. 
### Named Entity Recognition
	This was implemented, but does not have a particular use as of right now. The only use is, if charles can not find any response that relates to the input. If the input has a 'PERSON' or 'GPE' named entity, charles will ask about the named entity, but the output is not stored as of right now.
	Sample Conversation:
		>>  Mike is a basketball player. 		(An input that isn't related to any question in question_answers)
		Charles>> Who is Mike?
## Correlation coefficient
	This algorithm is used to determine the correlation between two tagged and tokenized lists. It uses a method I call "Trickle-Down Weight Distribution" to distribute the weights of the correlations of nouns/verbs/etc.. This took more time and effort to come up with and implement than anything else in this assignment. 
