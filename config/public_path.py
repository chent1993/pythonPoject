# -*- coding: utf-8 -*-

import os


from common.time_utils import TimeUtils


class PublicPath:
    t = TimeUtils()

    BASE_DIR = os.path.dirname(__file__)  # common路径
    PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../', ))  # 测试项目路径
    LOG_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, '../logs', t.get_current_end_hour()))  # 测试日志路径
    REPORT_ALLURE_DIR = os.path.abspath(os.path.join(BASE_DIR, '../reports', t.get_current_end_hour(), 'allure'))  # 测试报告allure路径
    REPORT_HTML_DIR = os.path.abspath(os.path.join(BASE_DIR, '../reports', t.get_current_end_hour(), 'html'))  # 测试报告html路径
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '../data'))  # 测试数据路径


    PROJECT_CONFIG = os.path.abspath(os.path.join(BASE_DIR, '../', "project.yml"))
    ENV_CONFIG = os.path.abspath(os.path.join(BASE_DIR, '../', "env.yml"))
    YAML_CONFIG = os.path.abspath(os.path.join(PROJECT_DIR, 'config'))

