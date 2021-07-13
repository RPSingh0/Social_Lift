if __name__ != "__main__":
    import os
    from PIL import Image
    from instabot import Bot
    import shutil
    from time import sleep

    def insta_post(caption, media, size, email, password):
        shutil.rmtree("./config", ignore_errors=True, onerror=None)
        print(os.getcwd())
        print(media)
        try:
            bot = Bot()
            im1 = Image.open(media)
            newsize = size
            im1 = im1.resize(newsize)

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
