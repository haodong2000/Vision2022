---
layout: post
title:  "Make a background image just like mine"
date:   2020-08-13 08:00:40 +0800
category: PythonPosts
---
When I settled down to build the blog used the Theme called `minima`, what concerned me most was the white background which made the website more commercial rather than a personal blog. So I racked my brain to find out a suitable backgroundimage. Inspiration comes in moments. Using mosaic in varous degrees grey as my backgound occured to me just in a small talk with a friend.  
   
Download a picture like a waterfall and make the photos mosaics using a filter in PS may be the most easy way. But like that ???? 🤣🤣🤣 So DISAPPOINTING!!!   
That made me determined to BUILD one from scratch.

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ghozr49nskj30m40em74h.jpg) 


At the very beginning, I made this image totally using PS and Keynote. Drew a from in Keynote, Took a screenshot and open it in PS, and then filled every square using the square brush like that. It drived my eyes ache so much😭. In the end, chose the form in another layer and then deleted it. You can also add several color shapes to make it better. It's a good way with certain advantages(I will mention at the end), but repeating the same work is not a coder should do, right😎?   

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ghoywq43bfj31fm0u0whe.jpg)
   
So, I'll show you how to make a mosaic background using `turtle` in Python. Code is the best explanation.
```python
import turtle as t
import random

t.setup(width = 1600, height = 1000)

t.colormode(255)
t.shape("square")
t.turtlesize(1.8)
t.hideturtle()
t.penup()
t.tracer(0)

# Define a function to draw a line of mosaic
def drawALine(i):
  t.goto(-780,i)
  for i in range(1,40):
      
      # When the values of the three RGB channels are equal, the color is gray
      color = random.randrange(245,255)
      t.color(color,color,color)
      t.stamp()
      t.fd(45)
  

for  i in range(-400, 445, 45):
    drawALine(i)

# Don't quit 
t.done()
```
It's pretty easy so that you can get rid of clicking again and again. The only thing you need to do is `changing several values` in the above code as you want. And you still can make a screenshot and put it into PS to add some color square to make it more dynamic.  
   

But, the second way still has its drawback. In the PS method, we can adjust how frequently the degrees of grey changes by modify few `settings` of brush. But if you use Python method, it seems more complex to meet this require and I haven't found a easy way so far. But it maybe doesn't matter a lot.  

You still can use ways mentioned to make other background consists of regular shape and arrangement. Wish you to have your ideal background images.😜