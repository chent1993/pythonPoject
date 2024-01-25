
# -*- coding: utf-8 -*-


import os
import sys
import yaml
import logging
import logging.handlers

from config.public_path import PublicPath

'''
Log Level       Numeric value
CRITICAL	    50
ERROR	        40
WARNING	        30
INFO	        20
DEBUG	        10
NOTSET	        0
'''

# config file log level is debug info warn error critical
LOG_LEVEL_DICT = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class InitLogger(object):
    """
    init logger from /project.yml

    file: file handler config, print msg to /var/log/tip/* file
          when enabled is true, add file handler
    console: console handler config, print msg to console
            when enabled is true, add file handler
    """

    def __init__(self, project):
        self.m_file_enabled = True
        self.m_max_log_size = 0
        self.m_file_level = ""
        self.m_file_log_formatter = ""
        self.m_file_config_path = ""
        self.m_back_up_count = 0
        self.m_console_enabled = False
        self.m_console_level = ""
        self.m_console_format = ""
        self.m_log_file_path = ""
        self.parse_config(PublicPath.PROJECT_CONFIG, project)
        self.get_logfile_path()

    def parse_config(self, config_file, project):
        """
        parse log config from config file
        :param config_file: config file
        :return:
        """
        with open(config_file, 'rb') as obj:
            all_configs = yaml.safe_load(obj.read())
            log_config = all_configs["log"]
            # file_handler config
            file_config = log_config['file']
            self.m_file_enabled = file_config['enabled']
            self.m_max_log_size = int(file_config['size'])
            self.m_file_level = file_config['level']
            self.m_file_log_formatter = file_config['format']
            self.m_log_file_path = os.path.abspath(
                os.path.join(PublicPath.LOG_BASE_DIR, all_configs['program'] + "-" + project + '.log'))
            # self.m_file_config_path = file_config['log_path']
            self.m_back_up_count = int(file_config['back_up_count'])

            # console_handler config
            console_config = log_config['console']
            self.m_console_enabled = console_config['enabled']
            self.m_console_level = console_config['level']
            self.m_console_format = console_config['format']

    def get_logfile_path(self):
        """
        generate log file path
        """
        # print("sys.argv[0] ==",sys.argv[0] )
        # log_path = os.path.normpath(sys.argv[0] + ".log").replace("../", "++_")
        # print("log_path ==", log_path)
        # while log_path[0] == "/":
        #     path_list = log_path.split('/')
        #     log_path = path_list[-1]
        # if log_path == ".log":
        #     log_path = "python.log"
        # print("log_path00 ==", log_path)
        # print("self.m_file_config_path ==", self.m_file_config_path)
        # log_path = os.path.join(self.m_file_config_path, log_path)
        # print("log_path1 ==", log_path)
        # self.m_log_file_path = log_path
        path_dir = os.path.abspath(os.path.join(self.m_log_file_path, "../"))
        if not os.path.isdir(path_dir):
            os.mkdir(path_dir)

    def get_logger(self):
        """
        get log logger
        add log handler if enabled is true
        """
        file_logger = logging.getLogger('')
        file_logger.setLevel(logging.DEBUG)

        # init file log
        if self.m_file_enabled:
            file_formatter = logging.Formatter(self.m_file_log_formatter)
            file_handler = logging.handlers.RotatingFileHandler(self.m_log_file_path,
                                                                maxBytes=self.m_max_log_size,
                                                                backupCount=self.m_back_up_count)
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(LOG_LEVEL_DICT[self.m_file_level])
            file_logger.addHandler(file_handler)

        # init console log
        if self.m_console_enabled:
            console_formatter = logging.Formatter(self.m_console_format)
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(console_formatter)
            console_handler.setLevel(LOG_LEVEL_DICT[self.m_console_level])
            file_logger.addHandler(console_handler)

        return file_logger


Logger = InitLogger("pythonProject").get_logger()
