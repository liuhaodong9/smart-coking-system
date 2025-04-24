Blender 教程
============

本文档演示如何在 **Blender 4.x** 中，为模型制作渐变贴图、烘焙到纹理，并导出为 **glTF 2.0 / .glb** 文件。

.. contents::
   :local:
   :depth: 1


步骤 1：打开 Shader Editor
-------------------------

#. 切换到 **Shading** 工作区  
   在 Blender 顶部菜单栏点击 **Shading**，即可同时看到 3D 视图与 **Shader Editor**。


步骤 2：选择对象和材质
---------------------

#. **选择模型**  
   在 3D 视图中点击目标对象。  

#. **确认材质**  
   右侧属性栏点击圆球图标（材质）。若对象尚无材质，点击 **New** 新建。


步骤 3：连接渐变到 Principled BSDF
---------------------------------

#. **查看节点**  
   在 Shader Editor 里应能看到 *Principled BSDF* → *Material Output*。  

#. **添加 ColorRamp**  
   `Shift +A` → `Color > ColorRamp`。  

#. **连接节点**  
   将 **ColorRamp** 的 *Color* 接口拖到 *Principled BSDF* 的 **Base Color**。

.. image:: _images/coloramp_to_bsdf.png
   :alt: ColorRamp 连接示意


步骤 4：确保 UV 映射正确
-----------------------

#. 切换到 **UV Editing** 工作区。  
#. 选中对象后按 **Tab** 进入编辑模式。  
#. `A` 全选 → `U` → *Smart UV Project*（或 *Unwrap*）。  
#. 在左侧 UV 编辑窗口调整展平结果。

.. image:: _images/smart_uv_project.png
   :alt: Smart UV Project 操作示意


步骤 5：添加 Image Texture 准备烘焙
----------------------------------

#. 回到 **Shading** 工作区。  
#. `Shift +A` → `Texture > Image Texture`。  
#. 在节点内点击 **New**，命名 *GradientBake*，分辨率 1024×1024。  
#. **暂时** 把 *Image Texture* 的 **Color** 输出连到 *BSDF.Base Color*，替代 ColorRamp。

.. note::

   只有将 *Image Texture* 设为 **激活/高亮**，Blender 才会把烘焙结果写入这张图。


步骤 6：设置 Bake 并执行
-----------------------

#. 右侧 **Render Properties** 设渲染器为 **Cycles**。  
#. 展开 **Bake** 面板：  

   * **Bake Type** 选 **Diffuse**  
   * 取消 *Direct* 与 *Indirect*，只保留 **Color**

#. 确保 *GradientBake* 图像处于选中状态。  
#. 点击 **Bake**，等待进度条完成。

.. image:: _images/bake_settings.png
   :alt: Bake 面板设置


步骤 7：保存烘焙贴图
-------------------

.. code-block:: none

   Image > Save As  ➜  gradient_bake.png


步骤 8：在材质中使用烘焙贴图
---------------------------

#. 确认 *Image Texture* 节点加载了 **gradient_bake.png**。  
#. 让其 **Color** 输出长期连接到 *BSDF.Base Color*。  
#. 可以删除或旁路原 ColorRamp 节点。


步骤 9：导出为 glTF
-------------------

#. 3D 视图中 `A` 或单选对象。  
#. **File ➜ Export ➜ glTF 2.0**。  
#. 关键选项：  

   * **Format** 选 **glTF Binary (.glb)**  
   * 勾选 **Selected Objects**（按需）  
   * **Images** 设为 **Embed**，将贴图嵌入 .glb

.. image:: _images/gltf_export.png
   :alt: glTF 导出设置示意


步骤 10：验证结果
-----------------

* 使用 **Windows 3D Viewer**、Babylon.js *Sandbox* 或任何在线 glTF Viewer 打开导出的 .glb。  
* 检查渐变是否正确，无色偏、无贴图丢失。  