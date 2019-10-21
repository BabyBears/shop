import requests


class Yunpian:

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "_______________________短信内容_______________________"
        }

        response = requests.post(self.single_send_url, data=parmas)
        import json
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = Yunpian("__________________apikey__________________")
    yun_pian.send_sms("2019", "17839222071")