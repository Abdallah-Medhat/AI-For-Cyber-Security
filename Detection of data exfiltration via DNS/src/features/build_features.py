#import Libraries
import tldextract
from collections import Counter
import math
#FQDN_count
# return total count of characters in FQDN expect '.'
def FQDN_count(record_domain):
    count_characters=0
    for i in record_domain:
        if i!='.':
            count_characters+=1
    return count_characters
#aa=FQDN_count("aaAB.123")
#print(aa)
#subdomain_length
# return Count of characters in subdomain expect '.'
def subdomain_length(record_domain):
    Count_characters_subdomain=0
    ext=tldextract.extract(record_domain)
    ext_subdomain=ext.subdomain
    if ext_subdomain:
        for i in ext_subdomain:
            if i!='.':
                Count_characters_subdomain+=1
    return Count_characters_subdomain
#aa=subdomain_length('http://forums.news.cnn.com/')
#print(aa)
#aa=subdomain_length('http://cnn.com/')
#print(aa)
# upper
# return Count of uppercase characters
def upper(record_domain): 
    count_uppercase_characters=0
    for i in record_domain:
        if i.isupper():
            count_uppercase_characters+=1
    return count_uppercase_characters
#aaaa=upper("AABBcccd")
#print(aaaa)
# lower
# return Count of lower characters
def lower(record_domain): 
    count_lower_characters=0
    for i in record_domain:
        if i.islower():
            count_lower_characters+=1
    return count_lower_characters
#aaaaa=lower("AABBcccd")
#print(aaaaa)
# numeric
# return Count of numerical characters
def numeric(record_domain):
    count_numbers=0
    for i in record_domain:
        #if i.isnumeric()
        if i.isdigit():
            count_numbers+=1
    return count_numbers
#aaaaaa=numeric('abbb123.3')
#print(aaaaaa)
# return entropy of query name
# entropy
def entropy(record_domain):
    entropy_record_domain=[]
    count_each_characters=Counter(record_domain)
    length_record_domain=float(len(record_domain))
    for count_value in count_each_characters.values():
        entropy_record_domain.append((count_value/length_record_domain * math.log2(count_value/length_record_domain)))
    return -sum(entropy_record_domain)
#aaaaaaa=entropy('aaaaaabbb')
#print(aaaaaaa)
# special
#return Number of special characters; special characters such as dash,underscore and equal
def special(record_domain):
    count_special_characters= 0
    for i in record_domain:  
        if (i.isalpha()):
            continue
        elif (i.isdigit()):
            continue
        else: 
            count_special_characters += 1
    return count_special_characters
#aaaaaaaa=special('http://cnn.com/ ')
#print(aaaaaaaa)
# labels
#return number of labels separated by dots
def labels(record_domain):
    count_labels=0
    for i in record_domain:
        if i=='.':
            count_labels+=1
    return count_labels+1
#b=labels('www.scholar.google.com')
#print(b)            
# labels_max
#return maximum label length
def labels_max(record_domain):
    len_labels=[]
    labels=record_domain.split('.')
    for i in labels:
        len_labels.append(len(i))
    max_len=max(len_labels)
    max_index=len_labels.index(max_len)
    return(len_labels[max_index])
#bb=labels_max('www.scholar.google.com')
#print(bb)
# labels_average
# return average label length
def labels_average(record_domain):
    len_labels=[]
    labels=record_domain.split('.')
    for i in labels:
        len_labels.append(len(i))
    sum_len_labels=sum(len_labels)
    average_len_labels=sum_len_labels/len(len_labels)
    return average_len_labels
#bbb=labels_average('www.scholar.google.com')
#print(bbb)
# longest_word
def longest_word(record_domain):
    len_labels=[]
    labels=record_domain.split('.')
    for i in labels:
        len_labels.append(len(i))
    max_len=max(len_labels)
    max_index=len_labels.index(max_len)
    return(labels[max_index])
#bbbb=longest_word('www.scholar.google.com')
#print(bbbb)
#sld
def sld(record_domain):
    ext=tldextract.extract(record_domain)
    sld = ext.domain
    return sld
#bbbbb=sld('www.scholar.google.com')
#print(bbbbb)
#len
#return Length of domain and subdomain
def len_domaind_subdomain(record_domain):
    ext=tldextract.extract(record_domain)
    len_domaind_subdomain=len(ext.subdomain)+len(ext.domain)
    return len_domaind_subdomain
#bbbbbb=len_domaind_subdomain('www.scholar.google.com')
#print(bbbbbb)
#subdomain
# return Whether the domain has subdomain or not
def subdomain(record_domain):
    ext=tldextract.extract(record_domain)
    ext_subdomain=ext.subdomain
    if ext_subdomain:
        return 1
    else:
        return 0
#bbbbbbb=subdomain('http://forums.news.cnn.com/')
#print(bbbbbbb)
#bbbbbbb=subdomain('http://cnn.com/')
#print(bbbbbbb)