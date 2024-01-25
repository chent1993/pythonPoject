import os
import random
import yaml
import json
from configparser import ConfigParser
from common.log import Logger



class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        Logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        Logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_json(self, file_path):
        Logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        Logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        Logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        Logger.info("读到数据 ==>>  {} ".format(data))
        return data


    def load_dirfile(self,path):
        """
        返回目录下的所有文件名
        :param path:
        :return:
        """
        return os.listdir(path)

    def random_dirfile(self,path,num=1):
        """

        :param path: 指定返回哪个路径下所有文件
        :param num: 指定返回文件名个数，默认值：1
        :return:
        """
        dirfiles = self.load_dirfile(path)
        if len(dirfiles)<num:
            return dirfiles
        return random.sample(dirfiles,num)


data = ReadFileData()

if __name__ == '__main__':
    print(data.random_dirfile('/file'))