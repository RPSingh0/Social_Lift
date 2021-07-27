if __name__ != "__main__":
    import requests
    import json

    def send_sms(message, number):
        """Arguements:\n
            1. message [str] -> Message to be sent.\n
            2. number [str] -> Phone number of the receiver.\n\n

            Returns: [str] object\n
                1. Success, if message sucessfully sent.\n
                2. Message cant be sent, if sent fail.\n"""
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers={number}"
        headers = {
            'authorization': "your auth code",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        status = response.json()
        if status['return'] == True:
            return "Success"
        else:
            return "Message cant be sent!"
