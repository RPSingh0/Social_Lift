if __name__ != "__main__":
    import requests
    import json

    def send_sms(message, number):
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers={number}"
        headers = {
            'authorization': "wc1j7PSEbB5HUCFrMuakDdWyg9hYT8A3VvOIxm6KNQt0Xf2LJzg3V8clhv0nZ7Li1qaEGIFQKxRMHsOy",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        status = response.json()
        if status['return'] == True:
            return "Sucess"
        else:
            return "Message cant be sent!"
