# Shakespeare Rare Word Chronology
This project orders Shakespeare's works based on his use of rare words, or words occurring between 2 and 11 times in
at least two different texts. 

## Data Organization
Within the "Data" folder, users may identify the focus of an iteration folder by its [acronym](https://github.com/achristo402/shakespeare-chronology/misc-files/acronyms.md).

Within iteration folders, users may identify the purpose of a file or folder by its suffix:  
**_text_list:** Texts used in a specific iteration.  
**_small_test:** Within this folder, a word's observed overlap between two texts is equal to its lowest occurence
in either. For example, if a word occurs 2 times in Text A and 6 times in Text B, the word's observed value is 2.
Likewise, a word which occurs 5 times in Text A and 3 times in Text B would have an obeserved value of 3.  
**_rarewords_by_text:** This folder contains a file for each text in the iteration; it lists the rare words which
occur in that text and the number of times they appear there.  
**_large_test:** Within a folder, a word's observed occurences between two texts is defined as (no. occurences
in Text A)*(no. occurences in Text B). For example, if a word occurs 2 times in Text A and 6 times in Text B, 
the word's observed value is 12. A word occuring 5 times in Text A and 3 times in Text B would have an observed value of 15.  
**_dictionary:** This is a dictionary of rare words compiled in this iteration. Rare words are split into sections according to
their number of occurences, from 2 to 11, and within each section they are organized alphabetically.  
  
  The file organization in the _small_test and _large_test folders is identical, and described here:  
  **text_comparisons:** This folder contains a file for every text in the iteration, in which it is 
  compared to every other text to find identify shared rare words. The content of each file is organized
  alphabetically by text, and lists the number of total links, number of 2-6 links, and the number of 7-11 
  links, as well as a list of the shared 2-6 and 7-11 links and their observed overlap.  
  **statistics:** This contains the statistical texts conducted on an iteration, and the data used in those
  tests. These files should be opened in Excel.
