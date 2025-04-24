安装指南
========

本指南提供了设置和运行项目前端、后端和数据库的步骤，以及使用 TensorFlow 进行 GPU 加速所需的 CUDA 安装方法。

.. contents::
   :local:
   :depth: 2


前端运行
--------

Vue 环境
^^^^^^^^

项目无需单独安装 Vue.js；`node_modules/` 已包含依赖，依赖列表见 `package.json`。

运行前端
^^^^^^^^

在项目根目录 **smart-coking-system** 打开终端并执行：

.. code-block:: bash

   npm run serve

.. image:: ../_images/前端运行结果1.png
   :alt: 前端运行结果 1

.. image:: ../_images/前端运行结果2.png
   :alt: 前端运行结果 2


后端运行
--------

创建虚拟环境
^^^^^^^^^^^^

.. code-block:: bash

   conda create -n coke python=3.8
   conda activate coke
   conda install -c conda-forge cudatoolkit=11.2
   pip install tensorflow-gpu==2.10
   conda install -c conda-forge cudnn=8.1

.. note::

   如果没有 GPU，`tensorflow-gpu` 可省略。

安装依赖项
^^^^^^^^^^

.. code-block:: bash

   pip install Flask==2.2.2 Flask-Cors==3.0.10 Flask-SQLAlchemy==3.0.2 \
       geatpy==2.7.0 numpy==1.23.4 pandas==1.5.1 PyMySQL==1.0.2 \
       scikit-learn==0.24.2 SQLAlchemy==1.4.44 Werkzeug==2.2.2 \
       memory-profiler==0.61.0

启动后端
^^^^^^^^

.. code-block:: bash

   python login.py

Flask 若成功启动，会监听本机 **5000** 端口。

.. image:: ../_images/后端运行结果.png
   :alt: 后端运行结果


数据库搭建
----------

安装 MySQL
^^^^^^^^^^

下载并安装 MySQL（示例教程： <https://www.jb51.net/database/324331zkx.htm>）。  
安装完记得把 `mysql/bin` 加到 **PATH**。

安装 Navicat Premium Lite
^^^^^^^^^^^^^^^^^^^^^^^^^

下载地址： <https://www.navicat.com.cn/download/navicat-premium-lite>  
这是免费的 MySQL GUI，可视化导入 CSV。

创建数据库并导入数据
^^^^^^^^^^^^^^^^^^^^

#. 新建 MySQL 连接，填用户名和密码。  
#. 创建数据库，例如 ``coaldata``。  
#. 导入示例 ``CoalData_table.csv``，格式选 “csv”。  
#. **高级选项** 勾选 “使用 NULL 替换空字符串”。

.. image:: ../_images/数据库设置1.png
   :alt: 数据库设置 1
.. image:: ../_images/数据库设置2.png
   :alt: 数据库设置 2
.. image:: ../_images/数据库设置3.png
   :alt: 数据库设置 3
.. image:: ../_images/数据库设置4.png
   :alt: 数据库设置 4
.. image:: ../_images/数据库设置5.png
   :alt: 数据库设置 5
.. image:: ../_images/数据库设置6.png
   :alt: 数据库设置 6
.. image:: ../_images/数据库设置7.png
   :alt: 数据库设置 7

更新 Flask 配置
^^^^^^^^^^^^^^

编辑 ``coalData.py``，修改连接串：

.. code-block:: python

   # MySQL URI 形式：mysql://<用户名>:<密码>@127.0.0.1:3306/coaldata?charset=utf8
   app.config['SQLALCHEMY_DATABASE_URI'] = (
       'mysql://root:123456@127.0.0.1:3306/coaldata?charset=utf8'
   )
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
