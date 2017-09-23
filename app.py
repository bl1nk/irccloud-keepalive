#!/usr/bin/env python

from requests import get, post
import urllib

email = ""
password = ""


def init():
    session = auth(email, password)
    stream(session)


def auth(email, password):
    formtoken_headers = {'content-length': '0'}
    token = post('https://www.irccloud.com/chat/auth-formtoken',
                 headers=formtoken_headers).json()['token']
    login_data = {'email': email, 'password': password, 'token': token}
    login_headers = {'x-auth-formtoken': login_data['token']}

    r = post('https://www.irccloud.com/chat/login', data=login_data,
             headers=login_headers)

    return r.json()['session']


def stream(session):
    stream_headers = {'Cookie': 'session=' + session,
                      'User-Agent': 'IRCCloud/1.11 (iPhone; en; iPhone OS 8.0)'}

    r = get('https://www.irccloud.com/chat/stream', headers=stream_headers,
            stream=True)


if __name__ == '__main__':
    init()
