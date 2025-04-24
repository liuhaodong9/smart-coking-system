程序的修改与维护
====================

本文档基于 Smart-Coking 项目当前部署流程，覆盖 **远程调试、生产部署、Docker 运行** 以及 **Sphinx 帮助文档** 更新等常见场景。

.. contents::
   :local:
   :depth: 2


SSH 远程调试
--------------

1. 启动后端（Flask）

   .. code-block:: bash

      ssh -L 5000:localhost:5000 <USER>@<SERVER_IP>
      如ssh -L 5000:localhost:5000 liuhaodong@211.68.155.21
      conda activate coke
      cd /opt/smart-coking/smart-coking-system/Flask
      python login.py

2. 启动前端（Vue）

   .. code-block:: bash

      ssh -L 8080:localhost:8080 <USER>@<SERVER_IP>
      如ssh -L 8080:localhost:8080 liuhaodong@211.68.155.21
      cd /opt/smart-coking/smart-coking-system/Flask
      npm run serve

3. 本地访问测试

   浏览器访问 `http://localhost:8080`，确认页面与接口均正常。

4. 打包并发布前端静态文件

   .. code-block:: bash

      npm run build
      sudo systemctl reload nginx

5. 后端守护（Gunicorn）

   .. code-block:: bash

      pkill -f gunicorn          # 结束旧进程（可选）
      gunicorn -w 4 -b 0.0.0.0:5000 login:app &

   端口 **5000** 若正常监听，则后端已在后台运行。


生产部署（Gunicorn + Nginx）
-----------------------------

1. 构建并发布前端静态文件

   .. code-block:: bash

      cd /opt/smart-coking/smart-coking-system/Flask
      npm run build
      sudo systemctl reload nginx

   > Nginx 缺省将 `dist/` 挂载到 `/var/www/smart-coking`。若修改，请同步调整 `nginx.conf` 中 `root` 路径。

2. 持久化运行后端服务

   1. 创建服务文件 `/etc/systemd/system/smart-coking.service`：

      .. code-block:: ini

         [Unit]
         Description=Smart-Coking Flask API
         After=network.target

         [Service]
         User=www-data
         Group=www-data
         WorkingDirectory=/opt/smart-coking/smart-coking-system/Flask
         Environment="PATH=/opt/miniconda/envs/coke/bin"
         ExecStart=/opt/miniconda/envs/coke/bin/gunicorn -w 4 -b 0.0.0.0:5000 login:app
         Restart=always
         RestartSec=5

         [Install]
         WantedBy=multi-user.target

   2. 启用并启动服务：

      .. code-block:: bash

         sudo systemctl daemon-reload
         sudo systemctl enable --now smart-coking.service
         sudo systemctl status smart-coking.service


Docker 部署
------------

1. 构建镜像

   .. code-block:: bash

      git clone https://github.com/your-org/smart-coking.git
      cd smart-coking
      docker build -t smart-coking:latest .

2. 运行容器

   .. code-block:: bash

      docker run -d \
        --name smart-coking \
        -p 80:80 \
        -p 5000:5000 \
        -v smart-coking-data:/data \
        --restart=unless-stopped \
        smart-coking:latest

3. docker-compose 示例

   .. code-block:: yaml

      version: "3.9"
      services:
        smart-coking:
          build: .
          ports:
            - "80:80"
            - "5000:5000"
          volumes:
            - smart-coking-data:/data
          restart: unless-stopped
      volumes:
        smart-coking-data:


更新 Sphinx 帮助文档
---------------------

.. code-block:: bash

    cd /opt/smart-coking/smart-coking-system/Flask/docs
    # 在 docs 目录下
    rm -Recurse -Force build          # 或 make clean
    sphinx-build -E -b html source build/html   # 重新完整构建


常见问题排查
--------------

* **端口占用** — `lsof -i :5000` 或 `lsof -i :8080`
* **Nginx 无法加载新静态文件** — 检查 `sudo systemctl reload nginx` 与 `/var/log/nginx/error.log`
* **前端资源路径不正确** — 核对 `vue.config.js` 中的 `publicPath` 是否匹配 Nginx `location`