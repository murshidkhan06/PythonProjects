import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "https://forms.gle/yiQw2ynPcLVXvHWD7"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
#url.svg("VashiMachineLearning.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('GenerativeAI_MazherBhai.png', scale=6)