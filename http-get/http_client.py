'''
create time : 11/23/20 02:38 
author : hcai
'''
import requests
import optparse


def get_params():
    PARAMS = {"key1":"value1",
              "key2": "value2",
              "key3": "value3",
              "key4": "value4",
              "key5": "value5",
              "key6": "value6"}
    return PARAMS

def get_headers():
    headers = {'user-agent': 'myapp/10.0.1'}
    return headers

def get_filename():
    filename = {"name:":"demo.html"}

def get_cookies():
    cookies = {"cookies":"testonly"}
    return cookies

if __name__ == '__main__':
    myParser = optparse.OptionParser()
    myParser.add_option("-f", "--file", help="Config file")
    myParser.add_option("-t", "--host", help="server host ip")
    myParser.add_option("-p", "--port", help="server port number")
    (opts, args) = myParser.parse_args()

    # set server ip and port
    host = opts.host
    port = opts.port
    if not port:
        port = 80
    port = int(port)

    # set request parameters
    params = get_params()
    headers = get_headers()
    filename = get_filename()
    cookies = get_cookies()
    response = requests.get(url = "http://%s:%s"%(host, port), cookies = cookies, headers=headers, params=params, files = filename)
