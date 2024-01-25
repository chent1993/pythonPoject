import json
from configparser import ConfigParser
import pytest
import requests
import yaml


from config.public_path import PublicPath




def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="choose env: test,prod")
    parser.addini('env', help="choose env: test,prod")
    parser.addoption("--user", action="store", help="choose user: free,qihoo")
    parser.addini('user', help="choose user: free,qihoo")

@pytest.fixture(scope='session',autouse=True)
def env_vars(request):

    """
    返回不同环境下变量
    :param request:
    :return:
    """
    config = request.config

    cur_env = config.getini('env') or config.getoption('--env')
    inifile = config.inifile
    conf = ConfigParser()
    conf.read(inifile)
    variables={}
    if conf.has_section(cur_env):
        variables.update(conf.items(cur_env))
    with open(PublicPath.ENV_CONFIG, 'w') as f:
        f.write(yaml.dump(variables, allow_unicode=True))
    return variables

@pytest.fixture(scope='session',autouse=True)
def login():
    return






def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    total = terminalreporter._numcollected
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    success_per = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
    failed_per = len(terminalreporter.stats.get('failed', [])) / terminalreporter._numcollected * 100
    error_per = len(terminalreporter.stats.get('error', [])) / terminalreporter._numcollected * 100
    skipped_per = len(terminalreporter.stats.get('skipped', [])) / terminalreporter._numcollected * 100

    mail = "本次测试收集结果为：\n" \
           "  TOTAL = %s" % total + "\n" \
           + "  PASSED = %s" % passed + "\n" \
           + "  FAILED = %s" % failed + "\n" \
           + "  ERROR = %s" % error + "\n" \
           + "  SKIPPED = %s" % skipped + "\n" \
           + "  SUCCESSFUL_PERCENT = %.2f%%" % success_per + "\n" \
           + "  FAILED_PERCENT = %.2f%%" % failed_per + "\n" \
           + "  ERROR_PERCENT = %.2f%%" % error_per + "\n" \
           + "  SKIPPED_PERCENT = %.2f%%" % skipped_per + "\n" \


    print(mail)
