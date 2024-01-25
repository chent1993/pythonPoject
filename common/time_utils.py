# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 16:09
# @Author  : chentian
# @File    : time_utils.py
# @Software: PyCharm
import datetime
import time


class TimeUtils:
    unit = 3600

    @classmethod
    def get_now(cls):
        cur_time = int(time.time())
        return cur_time

    @classmethod
    def get_last_hour_start(cls):
        cur_time = int(time.time())
        return cur_time - (cur_time % cls.unit) - cls.unit

    @classmethod
    def get_last_hour_end(cls):
        cur_time = int(time.time())
        return cur_time - (cur_time % cls.unit) - 1

    @classmethod
    def get_format_time(cls, int_time):
        """
        时间戳转换为时间格式
        """
        time_array = time.localtime(int_time)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    @classmethod
    def get_int_time(cls, formatted_time):
        """
        时间戳转换为时间格式
        """
        time_array = time.strptime(formatted_time, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(time_array))

    @classmethod
    def current_time(cls):
        """
        获取当前时间,****-**-** **:**:**格式
        """
        cur_time = int(time.time())
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cur_time))

    @classmethod
    def current_day(cls):
        """
        获取当前日期-天,********格式
        """
        cur_time = int(time.time())
        print(time.localtime(cur_time))
        return time.strftime("%Y%m%d", time.localtime(cur_time))

    @classmethod
    def get_yesterday(cls):
        """
        获取昨天日期-天,********格式
        """
        yesterday = datetime.date.today() + datetime.timedelta(-1)
        return yesterday.strftime('%Y%m%d')

    @classmethod
    def get_current_hour(cls):
        return datetime.datetime.now().hour

    @classmethod
    def get_current_weekend(cls):
        return datetime.datetime.now().weekday()

    @classmethod
    def get_current_monday(cls):
        '''
        获取本周一日期
        :return:
        '''
        today = cls.current_day()
        aa =  cls.get_current_weekend()
        return str(int(today) - cls.get_current_weekend())

    @classmethod
    def get_current_end_hour(cls):
        """
        获取当前时间,********_**格式
        :return:
        """
        cur_time = int(time.time())
        return time.strftime("%Y%m%d_%H", time.localtime(cur_time))
if __name__ == '__main__':
    t = TimeUtils()
    print(type(t.get_current_monday()))
    print(t.current_day())

