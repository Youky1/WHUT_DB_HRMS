# 人力资源管理系统

## 项目结构

- 后端：Django3 + MySQL
- 前端：Vue/vuex/vue-router

## 运行

- backend目录下，python manage.py runserver启动后端服务器
- fontend目录下，npm run serve启动前端服务器

## 三大核心功能

- 信息查询
  - 个人信息
  - 公司各职位薪资待遇情况
- 公司业务管理
  - 查看各部门信息
  - 修改部门信息：包括主管和业务内容
  - 查看各职位总人数和已在岗人数
- 人事管理
  - 录用新员工，录入一系列信息
  - 为录用的员工分配职位
  - 调度员工岗位


## 系统页面

- 登录页面
- 主页
  - 左侧是功能菜单
  - 右侧是相应的内容页面
- 个人信息页面
- 公司薪资待遇情况页面
- 部门信息查看页面
- 部门信息修改页面
- 职位统计页面
- 员工录用页面
- 岗位分配页面
- 岗位调度页面
- 辞退员工页面

## 数据库结构

- department表：公司部门信息
  > 主码为Department_id，一个id对应一个部门
- position表：公司各职位信息
  > 主码为Position_id，一个id对应一个职位
- employee表：已录用的员工信息
  > 主码为Employee_id，一个id对应一个员工
- experience表：员工的工作经验
  > 主码为ID，一个员工ID对应任意条工作经验

## 数据库的修改
- employee表中的status属性去掉
- position表中已有的Post_number表示每个职位最多人数，新加一个Post_already属性表示该岗位已有多少人