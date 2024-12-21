from PIL import Image, ImageDraw, ImageFont


def create_frame(width=1080, height=1920, background_color=(255, 255, 255), border_color=(0, 0, 0),
                 border_thickness=0):
    # Create a blank image with the specified background color
    frame = Image.new("RGB", (width, height), background_color)

    # Draw the border
    draw = ImageDraw.Draw(frame)
    for i in range(border_thickness):
        draw.rectangle([i, i, width - 1 - i, height - 1 - i], outline=border_color)

    # Optional: Add text to the frame
    text = "Sample Frame"
    font_size = 40
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    draw.text((text_x, text_y), text, fill=border_color, font=font)

    # Save the frame to a file
    frame.save("frame.png")


# Call the function to create the frame
create_frame()
