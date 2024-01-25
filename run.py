import os

import pytest

if __name__ == '__main__':
    # 执行case
    # pytest.main()  #
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    os.system('allure generate ./report/xml -o ./report/html --clean')
