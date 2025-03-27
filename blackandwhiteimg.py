from PIL import Image, ImageDraw, ImageFont

img = Image.open("Images/jpn.jpg")

img2 = img.convert("L")

img2.save("Images/black_white_pic.jpg")



# Open an existing image
image = Image.open('Images/jpn.jpg')  # Replace with your image file path
draw = ImageDraw.Draw(image)



font = ImageFont.truetype("/home/emobilis/Downloads/Oleo_Script.zip",50)  # You can specify a font, e.g., ImageFont.truetype("arial.ttf", 50)
text = "Hello World"

bbox = draw.textbbox(0,0 ,text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
image_width, image_height = image.size
x = image_width/2 - text_width/2
y = image_height/2 - text_height/2




