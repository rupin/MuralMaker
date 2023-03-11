from PIL import Image, ImageOps, ImageDraw, ImageFont

# Load the image file
image = Image.open("mickey.jpeg")
color_tuples=[(252, 252, 252), (250, 250, 250), (255, 254, 252), (253, 253, 253),(250, 249, 3),(248, 247, 245),(251, 250, 248),(251, 250, 248)]
color_names=["Yellow", "Green", "Red", "Purple", "Orange", "Violet", "Black", "White"]
code_words=["A", "B", "C", "D", "E", "F", "G", "H"]
code_count=[0,0,0,0,0,0,0,0]

#oneinchimage = Image.open("oneinch.jpg")

# Define the size of A4 paper in pixels
pa_width, pa_height = 2400, 2400
ia_width, ia_height=2400, 1108

a4_width, a4_height=2480, 3508
# Define the size of the squares in inches
square_size = 1
pixel_offset=40
offset=40

# Define the number of squares in each direction
squares_x, squares_y = 8, 8
square_width = int(pa_width / squares_x)
square_height = int(pa_height / squares_y)

font = ImageFont.truetype('Roboto-Bold.ttf', 80)

# Loop through every 8x11 section of the image
for y in range(0, image.height, squares_y):
    for x in range(0, image.width, squares_x):
        # Crop the section of the image
        section = image.crop((x, y, x+squares_x, y+squares_y))
        
        # Create a new image with the size of an A4 sheet
        #a4_image = Image.new("RGB", (a4_width, a4_height), "white")
        a4_image=Image.open("basetemplate.jpg")
        
        # Calculate the size of each square in pixels
       
         # Define the font and size for the name text
        # Define the font and size for the name text
        # 
        #        

        #reset count of Codes
        code_count=[0]*len(color_tuples)
        
        # Loop through every square and set its color to the corresponding pixel color in the section
        for j in range(squares_y):
            for i in range(squares_x):
                # Get the color of the pixel at the corresponding location in the section
                pixel_color = section.getpixel((i, j))
                #print(pixel_color)

                # Create a new image with the size of a square and set its color
                square_image = Image.new("RGB", (square_width, square_height), "white")
                #print(pixel_color)
                try:
                    a=color_tuples.index(pixel_color)
                    #print(pixel_color, end='')
                    #print("Found at position ", end='')
                    #print(a)
                    codePosition=(int(square_width/2)-30, int(square_height/2)-40)
                    ImageDraw.Draw(square_image).text(codePosition, str(code_words[a]), font=font, fill=(0, 0, 0))
                    code_count[a]=code_count[a]+1
                except ValueError:
                    a="-"
                    #print(pixel_color, end='')
                    #print(" Not Found")
                
                

                
                
                color = "gray"

                # top, right, bottom, left
                border = (1, 1, 1, 1)

                new_img = ImageOps.expand(square_image, border=border, fill=color)
                
                # Paste the square onto the A4 image at the correct location
                a4_image.paste(new_img, (i*square_width +pixel_offset, j*square_height+pixel_offset))
        
        

       
        

        for s in range(len(code_count)):
            if(code_count[s]<10):

                code_count_position=(20+square_width/2+square_width*s, 3010)
            else:
                code_count_position=(10+square_width/2+square_width*s, 3010) 
            print(code_count[s])   

            ImageDraw.Draw(a4_image).text(code_count_position, str(code_count[s]), font=font, fill=(0, 0, 0))

        filename = f"GeneratedImages\mickey_{x}_{y}.jpg"
        a4_image.save(filename, dpi=(300,300))
        exit()
