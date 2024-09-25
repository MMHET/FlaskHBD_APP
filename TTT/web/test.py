import random

selected_images = []

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

def testit():
    selected_images = count_select()
    
    return print(selected_images)

testit()

'''
@all_funcs.route('/')
def all_funcs_route():
    # Pass the selected image to the template
    selected_image = count_select()
    #print(selected_image)
    return render_template('render.html', image_selct=selected_image)
'''       