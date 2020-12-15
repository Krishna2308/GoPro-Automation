# GoPro Automation
# Downloads(to PC) and then deletes all the media from my GoPro 
# To do:
#   - Connect PC to server to store gopro files by date
#   - can this process be automated?
#       - connect to gopro wifi
#       - Run script
#       - Media gets downloaded into appropriate folder connected to server
#       - Downloaded files are deleted

# Import 
from goprocam import GoProCamera, constants
import shutil

# Create GoPro object
goproCamera = GoProCamera.GoPro()

print("Listing Media...\n")
media_list = goproCamera.listMedia(True)
print("\nNumber of media: ", len(media_list))

# Function to delete GoPro media, to be called after downloading media
def delete_media():
    goproCamera.delete("all")

# Download All GoPro media into the respective file(s)
def download_media():
    media = goproCamera.downloadAll()
    for i in media:
        shutil.move('./100GOPRO-{}'.format(i), './media/100GOPRO-{}'.format(i))

print("\nListing Media...\n")
media_list_after = goproCamera.listMedia(True)
print("\nNumber of media: ", len(media_list_after))