import random
from flask import Blueprint, render_template

all_funcs = Blueprint('all_funcs', __name__, template_folder='TTT/web/static')

def count_select(num_images=12):
    # List of image files and their correct answers
    available_images = [(f'/static/temp/{i}.PNG', name) for i, name in enumerate(['czech', 'namibia', 'Kenya', 'algeria', 'combodia', 'chad', 'ecuador', 'india', 'liechtenstein', 'st.lucia', 'reunion', 'madagascar'], start=1)]
    
    # Randomly select the required number of unique images
    selected = random.sample(available_images, num_images)
    
    # Return both images and their associated correct answers
    return selected

# Route for the home page
@all_funcs.route('/')
def all_funcs_route():
    # Get 12 unique images along with their correct answers
    selected_images = count_select(12)  # This returns a list of (image, answer) tuples
    images = [img for img, _ in selected_images]   # Extract image URLs
    answers = [answer for _, answer in selected_images]  # Extract the correct answers
    
    # Pass both images and answers to the template
    return render_template('render.html', images=images, answers=answers)


'''
## This is is the first iteration that works sim
import random

from flask import Blueprint, render_template

all_funcs = Blueprint('all_funcs',__name__,template_folder='C:/Users/loswe/Desktop/HBD26/TT7/web/static')

#global list1, list2
global selected_images

selected_images =[]

def count_select():
    # List of possible image files
    available_images = [f'/static/temp/{i}.PNG' for i in range(1, 13)]
    
    # Check which images have not been selected yet
    remaining_images = [img for img in available_images if img not in selected_images]
    
    # If all images are used, reset the list of selected images
    if not remaining_images:
        selected_images.clear()
        remaining_images = available_images
    
    # Randomly select an image from the remaining ones
    image_selct = random.choice(remaining_images)
    
    # Add the selected image to the list of already selected images
    selected_images.append(image_selct)
    
    return image_selct

# Route for the home page
@all_funcs.route('/')
def all_funcs_route():
    # Pass the selected image to the template
    selected_image = count_select()
    #print(selected_image)
    return render_template('render.html', image_selct = selected_image)
       
'''



















## Original code down here
'''
def count_select():
    selc_num = random.randint(1, 12)
    
    image_selct =('/static/temp/{}.PNG'.format(selc_num))
    
    return image_selct


count_select()

@all_funcs.route('/')

def all_funcs():
    
    return render_template('render.html', image_selct = 'image_selct')

'''


'''
def test():
    num1 = random.randint(0, 3)
    
    return print(num1)

test()


def image_pick():
    selc_num = random.randint(1, 12)
    
    image_selct =('/static/temp/{}.PNG'.format(selc_num))
    
    return image_selct
   
   
   

def count_select():
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    selc_num = random.choice(list1)
    
    for i in range(list1):
        if list1[i] == selc_num:
            list1.remove(selc_num)
            if selc_num == 1:
            
            
              
                
'''    

