# -*- coding: utf-8 -*-

import json
import requests



class BaseRequest:

    def send_get(self, url, data, header=None, cookie=None,verify=False):
        """
        Requests发送Get请求
        :param url：请求地址
        :param data：Get请求参数
        :param cookie：cookie参数
        :param header：header参数
        :param verify: 是否验证ca证书
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header,verify=verify)
        return response

    def send_post(self, url, data, header=None, cookie=None,verify=False):
        """
        Requests发送Post请求
        :param url：请求地址
        :param data：Post请求参数
        :param cookie：cookie参数
        :param header：header参数
        :param verify: 是否验证ca证书
        """
        response = requests.post(url=url, json=data, cookies=cookie, headers=header,verify=verify)
        return response

    def send_put(self,url, data, header=None, cookie=None,verify=False):
        """
        Requests发送PUT请求
        :param url: 请求地址
        :param data: 请求参数
        :param header: header参数
        :param cookie: cookie参数
        :param verify: 是否验证ca证书
        :return:
        """
        response = requests.put(url=url, json=data, cookies=cookie, headers=header, verify=verify)
        return response
    def send_delete(self,url, data, header=None, cookie=None,verify=False):
        """
        Requests发送DELETE请求
        :param url: 请求地址
        :param data: 请求参数
        :param header: header参数
        :param cookie: cookie参数
        :param verify: 是否验证ca证书
        :return:
        """
        response = requests.delete(url=url, data=data, cookies=cookie, headers=header, verify=verify)
        return response
    def run_main(self, method, url, data, header, cookie=None,verify=False):
        """
        :param method: 请求方法
        :param url: 请求地址
        :param data: 请求参数
        :param header: header参数
        :param cookie: cookie参数
        """
        try:
            result = ''
            if method.upper() == 'GET':
                result = self.send_get(url, data, header, cookie,verify)
            elif method.upper() == 'POST':
                result = self.send_post(url, data, header, cookie,verify)
            elif method.upper() == 'PUT':
                result = self.send_put(url,data,header, cookie,verify)
            elif method.upper() == 'DELETE':
                result = self.send_delete(url, data, header, cookie, verify)
            return result
        except Exception as e:
            logger.exception('请求主函数调用失败：{}'.format(e))



    def upload_file(url, headers, file):
        try:
            # headers
            payload = {}
            response = requests.request("POST",url=url,files=file, headers=headers,data=payload)
            r = json.loads(response.text)
        except Exception as e:
            print(e)
            return '出错了,请看错误，错误是{}'.format(e)
        return r