框架说明: 本框架可实现接口的自动化测试 流程介绍:自动化测试用例编写=》自动化执行测试用例
主要技术：pytest+requests+allure
目录结构介绍及使用方法：
//框架执行与配置目录
├── run.py                      // 框架执行函数                
├── pytest.ini                  // pytest.ini 

//配置文件目录
├── config
│   └── 项目集1 
│       └── production.yaml         //线上环境配置，以多个项目为维度进行配置
│       └── test.yaml               //测试环境配置
│   └── 项目集2 
│       └── production.yaml         //线上环境配置，以多个项目为维度进行配置
│       └── test.yaml               //测试环境配置
│       └── prepare.yaml            //灰度环境配置

//api接口分层目录
├── api
│   └── 项目集1         
│            └── 项目名 1              
│                └── 模块1                          
│                     └── 接口 pytest文件 
│                └── 模块2                          
│                     └── 接口 pytest文件 
│            └── 项目名 2              
│                └── 模块1                          
│                     └── 接口 pytest文件 
│                └── 模块2                          
│                     └── 接口 pytest文件 

//case分层目录
├── case
│   └── 项目集1         
│            └── 项目名 1              
│                └── 模块1                          
│                     └── 接口 pytest文件 
│                └── 模块2                          
│                     └── 接口 pytest文件 
│            └── 项目名 2              
│                └── 模块1                          
│                     └── 接口 pytest文件 
│                └── 模块2                          
│                     └── 接口 pytest文件 

//data目录
├── data
│   └── 项目集1         
│            └── 项目名 1              
│                └── data文件
│            └── 项目名 2              
│                └── data文件
│   └── 项目集2         
│            └── 项目名 1              
│                └── data文件
│            └── 项目名 2              
│                └── data文件

//log日志目录
├── log
│   └── 日期1（XXXX-XX-XX）    
│       └── 项目集1-项目名.log
│       └── 项目集1-项目名2.log   
│       └── 项目集2-项目名1.log
│       └── 项目集2-项目名2.log     
│            
│   └── 日期2（XXXX-XX-XX）    
│       └── 项目集1-项目名.log
│       └── 项目集1-项目名2.log   
│       └── 项目集2-项目名1.log
│       └── 项目集2-项目名2.log  

//report测试报告目录
├── report
│   └── 日期1（XXXX-XX-XX）      
│       └── allure    
│       └── html    
│   └── 日期2（XXXX-XX-XX）      
│       └── allure    
│       └── html 

//公共功能方法目录
├── common
│   └── log.py                   //框架日志处理
│   └── public_path.py           //框架相关公共使用路径处理
│   └── tools.py                
│       │   │   ├── load_config         //加载解析yaml文件  

//虚拟环境，依赖Virtualenv
├── venv                               //使用方法：1.pip install virtualenv  2.virtualenv venv(创建虚拟环境) 3. .\venv\Scripts\activate(激活虚拟环境)
├── requirements.txt                  //管理依赖包  首次使用：pip install -r requirements.txt
                                      //新增依赖包，执行命令将依赖包加入文件：pip freeze > requirements.txt
