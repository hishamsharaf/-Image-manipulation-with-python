#!/usr/bin/env python
# coding: utf-8

# In[2]:


# creating variations based on a single photo and add text.
import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw


# In[5]:


# read image and convert to RGB
image=Image.open("msi_recruitment.gif")
image=image.convert('RGB')
display(image)


# In[6]:


# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(1, 10):
    images.append(enhancer.enhance(i/10))


# In[7]:


# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,(first_image.height+60)*3))


# In[8]:


n = (0.1, 0.5, 0.9)*3


# In[9]:


newimages = []

red, green, blue = image.split()

for i in (0.1, 0.5, 0.9):
    r = red.point(lambda x: x * i)
    out = Image.merge('RGB', (r, green, blue))
    newimages.append(out)
for i in (0.1, 0.5, 0.9):
    g = green.point(lambda x:x*i)
    out_2 = Image.merge('RGB', (red, g, blue))
    newimages.append(out_2)
for i in (0.1, 0.5, 0.9):
    b = blue.point(lambda x:x*i)
    out_3 = Image.merge('RGB', (red, green, b))
    newimages.append(out_3)


# In[10]:


matrix = ( 0, 0, 0, 0,
           0, 0, 0, 0,
           0, 0, 0, 0)
bimg = first_image.convert("RGB", matrix)


# In[48]:


newimages = []

red, green, blue = image.split()

for i in (0.1, 0.5, 0.9):
    r = red.point(lambda x: x * i)
    out = Image.merge('RGB', (r, green, blue))
    newimages.append(out)
for i in (0.1, 0.5, 0.9):
    g = green.point(lambda x:x*i)
    out_2 = Image.merge('RGB', (red, g, blue))
    newimages.append(out_2)
for i in (0.1, 0.5, 0.9):
    b = blue.point(lambda x:x*i)
    out_3 = Image.merge('RGB', (red, green, b))
    newimages.append(out_3)                       


# In[49]:


matrix = ( 0, 0, 0, 0,
           0, 0, 0, 0,
           0, 0, 0, 0)
bimg = first_image.convert("RGB", matrix)


# In[11]:


n = (0.1, 0.5, 0.9)*3
font = ImageFont.truetype(r'fanwood-webfont.ttf', 75) 
channel_no =0
draw = ImageDraw.Draw(bimg)
textimages = []

for i  in n:
    bimg = first_image.convert("RGB", matrix)
    draw = ImageDraw.Draw(bimg)
    text = 'channel {} intensity {}'.format(channel_no, i)
    draw.text((10,390), text, font = font)
    textimages.append(bimg)
    if len(textimages) == 3:
        channel_no += 1
    elif len(textimages) == 6:
        channel_no += 1
        
        
    


# In[12]:


x = 0
y = 60
for img in textimages:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+60
    else:
        x=x+first_image.width


display(contact_sheet)


# In[13]:


# paste the images with different intensity in the coontact sheet
a = 0
b = 0
for img in newimages:
    contact_sheet.paste(img,(a,b))
    if a+first_image.width == contact_sheet.width:
        a=0
        b=b+first_image.height+60
    else:
        a=a+first_image.width


# In[14]:


contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

