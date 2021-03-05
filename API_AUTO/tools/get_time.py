import time
import datetime
import requests


class GetTime:

    def sec_time(self):
        raw_time = time.time()
        sec_time = int(raw_time)
        return sec_time

    def msec_time(self):
        raw_time = time.time()
        msec_time = int(raw_time * 1000)
        return msec_time


if __name__ == '__main__':
    msec_time = GetTime().msec_time()
    url = "https://test.paquapp.com/user/login/4/"
    req_body = {
        "client_public_key": "-----BEGIN PUBLIC KEY----- MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQDb9p5cO/x0IRewabjTczgLSI/X WgzhjPxP3pa6qiyjuEybhqpfBqbCTw2taQflVys4efe8iijDoTOVKRt28iiv4yOX kUYK3CMJ9H6Xk4cXfI9DcK0bdwUJTWtoprUmd+Ea0H3yLrrMJPAR/c6rcRkp0AHR hnxmi4MsBMDBzGkidQIBEQ== -----END PUBLIC KEY-----",
        "code": "1234",
        "device_identify": "ACB720E2-47D1-490C-972D-C4CE4D0DB4D5",
        "device_model": "iPhone 6",
        "device_token": "b5e20664a5324154f2dee18ace91bea27851e5fabc7f101ee6ccbe5ace0cf580",
        "net_status": 1,
        "platform": "iOS",
        "screen_height": "667",
        "screen_width": "375",
        "sign": "ff9ace93ff47815cd6d46e2835f9a67c",
        "system_version": "12.4.2",
        "tel": "15188888888",
        "ts": msec_time,
        "version": "5.1.0"
    }
    res = requests.post(url=url, data=req_body, verify=False)
    print(res.json())
