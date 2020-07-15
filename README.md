# Shakespeare Rare Word Chronology
This project orders Shakespeare's works based on his use of rare words, or words occurring between 2 and 11 times in at least two different texts.  

## Data Organization
Within the "Data" folder, users may identify the focus of an iteration folder by its [acronym](https://github.com/achristo402/shakespeare-chronology/blob/master/misc-files/acronyms.md).  

Within iteration folders, users may identify the purpose of a file or folder by its suffix:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**_text_list:** Texts used in a specific iteration.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**_small_test:** Within this folder, a word's observed overlap between two texts is equal to its lowest occurrence in either. For example, if a word occurs 2 times in Text A and 6 times in Text B, the word's observed value is 2. Likewise, a word which occurs 5 times in Text A and 3 times in Text B would have an observed value of 3. The essay uses data from the small test in its analysis.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**_rarewords_by_text:** This folder contains a file for each text in the iteration; it lists the rare words which occur in that text and the number of times they appear there.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**_large_test:** Within a folder, a word's observed occurrences between two texts is defined as (no. occurrences in Text A)*(no. occurrences in Text B). For example, if a word occurs 2 times in Text A and 6 times in Text B, the word's observed value is 12. A word occurring 5 times in Text A and 3 times in Text B would have an observed value of 15.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**_dictionary:** This is a dictionary of rare words compiled in this iteration. Rare words are split into sections according to their number of occurrences, from 2 to 11, and within each section they are organized alphabetically.  

  The file organization in the _small_test and _large_test folders is identical, and described here:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**text_comparisons:** This folder contains a file for every text in the iteration, in which it is compared to every other text to find shared rare words. The content of each file is organized alphabetically by text, and lists the number of total links, number of 2-6 links, and the number of 7-11 links, as well as a list of the shared 2-6 and 7-11 links and their observed overlap.   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**statistics:** This contains the statistical tests conducted on an iteration, and the data used in those tests. These files should be opened in Excel.  

## Usage
chronology-methods.py contains the methods used to analyze Shakespeare's use of rare words in this paper. To study texts with these methods, users must supply them in a csv format, stripped of all punctuation except for apostrophes (this, is, the, proper, csv, format). In our research, we also removed stage directions, scene and act labels, and unspoken character names.

## Authors  
Douglas Bruster  
Anna Christoffersen  
