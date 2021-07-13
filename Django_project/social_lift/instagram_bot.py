if __name__ != "__main__":
    import os
    from PIL import Image
    from instabot import Bot
    import shutil
    from time import sleep

    def insta_post(caption, media, size, email, password):
        """Agruements:\n
            1. caption [str] -> caption for the post\n
            2. media [raw str] -> file path of media to be uploaded *(image only)\n
            3. size [tuple] -> dimentions of the image to be uploaded *(default : 1080x1080)\n
            4. email [str] -> email of the user\n
            5. password [str] -> password of user's email\n\n

            Retuns:[str] object\n
                1. Posted, if the post was successfully created.\n
                2. Cannot post, if the post creation was unsuccessful\n"""

        # Here shutil.rmtree command is used to delete the config folder created by the instabot, so that is cannot interfear with the program
        shutil.rmtree("./config", ignore_errors=True, onerror=None)
        # print(os.getcwd())
        # print(media)
        try:
            bot = Bot()
            im1 = Image.open(media)
            newsize = size
            im1 = im1.resize(newsize)

            # Here it searches and deletes the upload.jpg.REMOVE_ME file so that the folder contains only one file of that type
            if os.path.exists("upload.jpg.REMOVE_ME"):
                os.remove("upload.jpg.REMOVE_ME")
            else:
                pass

            im1.save("upload.jpg")

            bot.login(username=email, password=password)
            bot.upload_photo("upload.jpg", caption=caption)
            sleep(10)
            return "Posted"
        except:
            return "Cannot post!"


# Type of Instagram Post  Aspect Ratio    Instagram Post Size

# Square Photo             1:1             1080 x 1080px
# Landscape Photo          1.91:1          1080 x 608px
# Portrait Photo           4:5             1080 x 1350px
# Instagram Stories        9:16            1080 x 1920px
# IGTV Cover Photo         1:1.55          420 x 654px
# Instagram Square Video   1:1             1080 x 1080px
# Instagram Landscape Video 1.91:1         1080 x 608px
# Instagram Portrait Video 4:5             1080 x 1350px
