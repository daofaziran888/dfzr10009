# 全链路数据采集运营平台

面向数据采集运营团队的全链路采集运营平台。覆盖采集策略配置、采集引擎调度、采集结果交付、采集质量巡检、采集成本核算、采集效能分析与采集资源规划的完整运营链路。

这是一个前后端分离的管理平台：前端 React + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 React + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 采集策略配置 | `strategy` | 采集策略 | 策略编号、目标站点、采集深度 |
| 采集引擎调度 | `engine` | 引擎节点 | 节点编号、节点地址、运行状态 |
| 采集结果交付 | `delivery` | 交付记录 | 记录编号、采集策略、交付格式 |
| 采集质量巡检 | `inspect` | 巡检任务 | 任务编号、巡检对象、巡检类型 |
| 采集成本核算 | `cost` | 成本账单 | 账单编号、核算周期、引擎费用 |
| 采集效能分析 | `efficiency` | 效能报告 | 报告编号、分析维度、采集量 |
| 采集资源规划 | `resource` | 资源计划 | 计划编号、资源类型、当前用量 |
| 网页抽取规则 | `crawlrule` | 抽取规则 | 规则编号、入口地址、页面选择器 |
| 采集源管理 | `datasource` | 采集源 | 源编号、源名称、源类型 |
| 采集数据清洗 | `cleaning` | 清洗规则 | 规则编号、目标字段、清洗类型 |
| 采集存储管理 | `storage` | 存储策略 | 策略编号、存储路径、文件格式 |
| 采集监控大屏 | `monitor` | 监控指标 | 指标编号、指标名称、当前数值 |
| 采集格式转换 | `format` | 转换模板 | 模板编号、输入格式、输出格式 |
| 采集重试日志 | `retrylog` | 重试记录 | 记录编号、失败任务、异常类型 |
| RPA流程模板 | `robotflow` | 流程模板 | 模板编号、模板名称、适用场景 |
| 采集数据标注 | `datatag` | 标注任务 | 任务编号、数据记录、标注类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数据采集、爬虫与RPA
