from PIL import Image

img = Image.open("image.jpg")
resized = img.resize((300, 300))
resized.save("resized.jpg")
print("Image resized!")
