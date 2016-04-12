from alertshandler.helpers import get_image_from_url
from PIL import Image
import ipdb

# Create your views here.
def process():
    while True:
        url='http://192.168.1.107:8080/shot.jpg'
        img = get_image_from_url(url)
        ipdb.set_trace()


