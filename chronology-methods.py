import os
import csv

#File name: chronology-methods.py
#Author: Anna Christoffersen
#Date: 12/30/19
#Description: A program containing methods used to analyze Shakespeare's
#use of rare words.

#*The size parameter in the compareTextsStr, compareTextsInt, compareFolder,
#and observedLinks methods refers to two different ways of calculating
#observed overlap. Using the "small" method, a word's overlap between two texts
#is equal to the word's no. of occurences in the text where it occurs the least.
#In the "large" method, a word's overlap is equal to (word's no. of occurences
#in Text A) * (word's no. of occurenes in Text B).

#Reads the contents of a file, outputting a dictionary of the file's words.
#Input the full filepath of the .txt file to be read.
def readFile(in_file):
    name = in_file
    temp_dict = {}
    final_dict = {}
    in_file = open(in_file, encoding='utf-8', errors='strict')
    data = in_file.read().replace(",","").split() 

    #Tallys the amount of times a word appears in the text
    for word in data:
        if word in temp_dict:
            temp_dict[word] = temp_dict[word]+1
        else:
            temp_dict[word] = 1

    sorted_keys = sorted(temp_dict.keys())
    #This loop strips "\ufeff" from words where it appears
    for word in sorted_keys:
        if word.startswith("\ufeff"):
            count = temp_dict[word]
            word = word.replace("\ufeff","")
            if word in temp_dict:
                count += temp_dict[word]
            final_dict.update({word:count})
        else:
            final_dict.update({word:temp_dict[word]})
            
    return final_dict

#Reads the contents of a folder, outputting a list where each file in the
#folder is a single dictionary.
#Input the full filepath of a folder containing only .txt files.
def readFolder(in_folder):
    texts = []

    for file in os.listdir(in_folder):
        if file.endswith('.txt'):
            texts += [readFile(in_folder+"/"+file)]           
    return texts

#Reads the contents of a folder, outputting a single dictionary of all words
#contained in the files of that folder.
#Input the full filepath of a folder containing only .txt files.
def makeSingleDict(in_folder):
    single_dict = {}
    texts = readFolder(in_folder)

    for text in texts:
        single_dict = {x: single_dict.get(x, 0) + text.get(x, 0) for x in set(single_dict).union(text)}
    return single_dict

#Outputs a dictionary of rare words in a specified folder.
#Inputs: in_folder is the full filepath of a folder containing only .txt files.
#lower is an integer specifying the lowest number of occurences qualifying
#a token as rare. upper is an integer specifying the highest number of
#occurences qualifying a token as rare.
def findDictionary(in_folder, lower, upper):
    temp_dict1 = {}
    temp_dict2 = {}
    rw_dict = {}
    data = makeSingleDict(in_folder)

    #Adds words that occur within specified bounds to the dictionary
    for key in data.keys():
        if(data[key] >= lower and data[key] <= upper):
            temp_dict1.update({key:data[key]})
    data = readFolder(in_folder)
    
    #This loop checks that a word appears in more than one play
    for word in temp_dict1.keys():
        wc = 0
        for play in data:
            if word in play:
                wc +=1
            if wc == 2:
                temp_dict2.update({word:temp_dict1[word]})
                continue

    #Sorts the dictionary
    sorted_keys = sorted(temp_dict2.keys())
    for i in sorted_keys:
        rw_dict.update({i:temp_dict2[i]})       
    return rw_dict

#Outputs the integer number of rare words in a text based on the inputted
#rare word dictionary.
#Inputs: in_file is the full filepath of the .txt file to be read. diction is a
#rare-word dictionary.
def findIntRareWords(in_file, rw_dict):
    rw_count = 0
    text = readFile(in_file)

    for word in text:
        if word in rw_dict:
            rw_count += text[word]
            
    return rw_count

#Outputs a dictionary of the rare words in a specific text, based on the
#inputted rare word dictionary. In the outputted dicionary, the key:value pairs
#are (rare word in text):(rare word's number of appearances in text).
#Inputs: in_file is the full filepath of the .txt file to be read. rw_dict is a
#rare word dictionary.
def findStringRareWords(in_file, rw_dict):
    rw_text = {}
    text = readFile(in_file)

    for word in text:
        if word in rw_dict:
            rw_text.update({word:text[word]})           
    return rw_text

#Compares two texts, outputting a dictionary of rare words they share and how
#many occurences of that rare word they share. In the outputted dictionary, the
#key:value pairs are (rare word shared by two texts):(number of shared
#appearances).
#Inputs: in_file1 is the full filepath of the first .txt file to be compared.
#in_file2 is the full filepath of the second .txt file to be compared.
#rw_dict is a rare word dictionary. size is either "small" or "large"*.
def compareTextsStr(in_file1, in_file2, rw_dict, size):
    rw_comp = {}
    text1 = findStringRareWords(in_file1, rw_dict)
    text2 = findStringRareWords(in_file2, rw_dict)

    if size == "large":
        for word in text1:
            if word in text2:
                overlap = text1[word] * text2[word]
                rw_comp.update({word:overlap})

    if size == "small":
        for word in text1:
            if word in text2:
                if text1[word] == text2[word]:
                    rw_comp.update({word:text1[word]})
                elif text1[word] > text2[word]:
                    rw_comp.update({word:text2[word]})
                elif text1[word] < text2[word]:
                    rw_comp.update({word:text1[word]})
                    
    return rw_comp

#Compares two texts, outputting the total integer number of rare words shared
#between the texts.
#Inputs: in_file1 is the full filepath of the first .txt file to be compared.
#in_file2 is the full filepath of the second .txt file to be compared.
#rw_dict is a rare word dictionary. size is either "small" or "large"*.
def compareTextsInt(in_file1, in_file2, rw_dict, size):
    rw_comp = 0
    text1 = findStringRareWords(in_file1, rw_dict)
    text2 = findStringRareWords(in_file2, rw_dict)

    if size == "large":
        for word in text1:
            if word in text2:
                overlap = text1[word] * text2[word]
                rw_comp += overlap
                              
    if size == "small":
        for word in text1:
            if word in text2:
                if text1[word] == text2[word]:
                    rw_comp += text1[word]
                elif text1[word] > text2[word]:
                    rw_comp += text2[word]
                elif text1[word] < text2[word]:
                    rw_comp += text1[word]
                    
    return rw_comp

#Finds rare words in common between a target text and an entire folder,
#outputting a list where each comparison between the target and a file is a
#single dictionary. In the outputted dictionary, key:value pairs are (rare word
#shared by two texts):(number of shared appearances).
#Inputs: target is the name of the target .txt file (do not put the full
#filepath - just type the name, like "ADO.txt" or "ARDsh.txt"). in_folder
#is the full filepath of a folder containing only .txt files. rw_dict
#is a rare word dictionary. size is "small" or "large"*. 
def compareFolder(target, in_folder, rw_dict, size):
    rw_comp = []
    temp_dict = {}

    for file in os.listdir(in_folder):
        if file.endswith('txt') and file != target:
            print(target)
            print(file)
            temp_dict = compareTextsStr(in_folder+"/"+target, in_folder+"/"+file, rw_dict, size)
            rw_comp += [temp_dict]
            print(temp_dict)
    return rw_comp

#Outputs a list of the integer number of links observed between all texts in a folder.
#Inputs: in_folder is the full filepath of a folder containing only .txt files. rw_dict
#is a rare word dictionary. size is "small" or "large"*. 
def observedLinks(in_folder, rw_dict, size):
        names = [" "]
        obs_links = []

        #Nested loop to compare every file with every other file
        for file1 in os.listdir(in_folder):
            if file1.endswith(".txt"):
                names += [file1.replace(".txt","")]
                temp_obs = [file1.replace(".txt","")]
                for file2 in os.listdir(in_folder):
                    if file2.endswith(".txt"):
                        #Assigns a text's observed value with itself to 0
                        if file1 == file2:
                            temp_obs += str(0)
                            continue
                        #Finds the observed value between two texts
                        else:
                            rw_count = compareTextsInt(in_folder+"/"+file1,in_folder+"/"+file2, rw_dict, size)
                            temp_obs += [str(rw_count)]
                obs_links += [temp_obs]
        obs_links.insert(0,names)
            
        return obs_links

#Outputs a list of the expected links between all texts in a folder. Expected values are
#calculated by the formula: [(rare words in text 1) * (rare words in text 2)]/(rare words in
#canon.
#Inputs: inFolder is the full file path of a folder containing only .txt files. diction is
#a rare word dictionary. 
def expectedLinks(in_folder, rw_dict):
    names = []
    exp_links = []
    tot_links = 0

    #Calculates the total number of rare words in a folder
    for word in rw_dict:
        tot_links += rw_dict[word]
    #Makes a list of the file names in a folder
    for file in os.listdir(in_folder):
        if file.endswith('txt'):
            names += [file]

    #Nested loop to compare every file with every other file
    for text1 in names:
        temp_exp = [text1.replace(".txt","")]
        text1_links = findIntRareWords(in_folder + '/' + text1, rw_dict)
        for text2 in names:
            #Assigns a text's expected value with itself to 0
            if text2 == text1:
                temp_exp += str(0)
            #Calculates the expected value between two texts
            else:
                text2_links = findIntRareWords(in_folder + '/' + text2, rw_dict)
                temp_exp += [((text1_links/(tot_links)) * text2_links)]
        exp_links += [temp_exp]
    names.insert(0," ")
    exp_links.insert(0,names)
    
    return exp_links

#Outputs a list of the chi-square values for a folder. To run
#this method, observedLinks and expectedLinks must have already been run
#and saved into variables.
#Inputs: obs_links is the list outputted by the observedLinks method. exp_links is
#the list outputted by the expectedLinks method.
def chiSquares(obs_links, exp_links):
    chi = []
    
    for index1,obs_list in enumerate(obs_links):
        #Skips over the row of names in obs_links
        if index1 == 0:
            continue
        exp_list = exp_links[index1]
        for index2,obs in enumerate(obs_list):
            #Assigns a text's name to the first position in the row
            if index2 == 0:
                temp_chi = [obs]
                continue
            obs = float(obs)
            exp = float(exp_list[index2])
            #Assigns a text's chi value with itself to 0
            if exp == 0:
                temp_chi += str(0)
            #Calculates a text's chi value with another text
            else:
                temp_chi += [str((((obs-exp)**2)/exp))]
        chi += [temp_chi]     
    chi.insert(0, obs_links[0])
    
    return chi

#Finds which texts a token appears in, outputting a dictionary with texts containing the token
#and how many times that token appears in the text.
#Inputs: in_folder is the full filepath of a folder containing only .txt files. word is a string
#variable of the target word. 
def whichTexts(in_folder, target_word):
    texts = {}
    
    for file in os.listdir(in_folder):
        if file.endswith('.txt') and "_dictionary" not in file:
            text = readFile(in_folder + "/" + file)
            if target_word in text:
                texts.update({file.replace(".txt",""):text[target_word]})                
    return texts

#Outputs a table with individual words and their number of appearances in each text.
#Inputs: in_folder is the full filepath of a folder containing only .txt files. rw_dict is a
#rare word dictionary.
def indWordTable(in_folder, rw_dict):
    names = []
    word_table = []
    words = list(rw_dict.keys())

    #Nested loop tests every file in a folder for every word in that folder's
    #rare word dictionary
    for file in os.listdir(in_folder):
        temp_list = []
        if file.endswith(".txt"):
            names += [file.replace(".txt","")]
            temp_list += [file.replace(".txt","")]
            text = readFile(in_folder+"/"+file)
            for word in words:
                if word in text.keys():
                    temp_list += [text[word]]
                else:
                    temp_list += [0]
        word_table += [temp_list]       
    words.insert(0," ")
    word_table.insert(0,words)
    
    return word_table
