---
layout: post
title:  "Kindle+Notion English Reading Note"
date:   2020-08-13 08:00:40 +0800
category: PythonPosts
---

## Background
Trying to make *_Reading Notes_* with Notion based on the contents in Kindle's clipping but unwilling to waste time on searching words and copying sentences, I stretch myself to learn related knowledge and code a scipt in Python to make it automatic.
### Format
![](https://tva1.sinaimg.cn/large/008eGmZEly1gmtc219rx1j310q0iy400.jpg)

## Work
1. Get contents from Kindle
  No matter whether you mark a word or a sentence in your kindle, it will add some words to a file `My Clipping.txt` in your Kindle ( `note_path='/Volumes/Kindle/documents/My Clippings.txt' `), conforming to following form (5 lines).  
    ```   
    Book Name
    Pages | Date
  
    word/sentence you have marked
    =========
    ```  
    So it is for us to abstract the note we want.  
    Except for getting the contents:  
    + Divide the content into words/phrases and sentences stored in `words` and `sentences`
    + Delete all contents in `My Clipping.txt` when running the scipt assuming that I will note with notion as soon as having read an article.  
  ( Referring to loadclip.py for details )  
2. Find the sense for words
  I code a simple python-spider to get sense from YoudaoDic web site.  
  ( Referring to getMean.py for details )
3. Add a new note to the Table in Notion.  
  For this part, I use a package [notion-py](https://github.com/jamalex/notion-py). It's comprehensible to treat a notion page as a `tree`.  
  ( Referring to notionNote.py for details )

  [Codes](https://github.com/Ibroad/Notion-English-ReadingNote)
