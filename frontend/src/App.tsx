import { useState } from 'react'
import { Link, Route, Routes } from 'react-router-dom'

import Overview from './views/Overview'
import StrategyView from './views/strategy'
import EngineView from './views/engine'
import DeliveryView from './views/delivery'
import InspectView from './views/inspect'
import CostView from './views/cost'
import EfficiencyView from './views/efficiency'
import ResourceView from './views/resource'
import CrawlruleView from './views/crawlrule'
import DatasourceView from './views/datasource'
import CleaningView from './views/cleaning'
import StorageView from './views/storage'
import MonitorView from './views/monitor'
import FormatView from './views/format'
import RetrylogView from './views/retrylog'
import RobotflowView from './views/robotflow'
import DatatagView from './views/datatag'

const navItems = [{ label: "运营概览", path: "/" }, { label: "采集策略配置", path: "/strategy" }, { label: "采集引擎调度", path: "/engine" }, { label: "采集结果交付", path: "/delivery" }, { label: "采集质量巡检", path: "/inspect" }, { label: "采集成本核算", path: "/cost" }, { label: "采集效能分析", path: "/efficiency" }, { label: "采集资源规划", path: "/resource" }, { label: "网页抽取规则", path: "/crawlrule" }, { label: "采集源管理", path: "/datasource" }, { label: "采集数据清洗", path: "/cleaning" }, { label: "采集存储管理", path: "/storage" }, { label: "采集监控大屏", path: "/monitor" }, { label: "采集格式转换", path: "/format" }, { label: "采集重试日志", path: "/retrylog" }, { label: "RPA流程模板", path: "/robotflow" }, { label: "采集数据标注", path: "/datatag" }]

export default function App() {
  const [operator] = useState('值班管理员')

  return (
    <div className="app-shell">
      <aside className="app-side">
        <h1 className="app-title">全链路数据采集运营平台</h1>
        <nav className="nav-list">
          {navItems.map((item) => (
            <Link key={item.path} to={item.path} className="nav-item">
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="app-main">
        <header className="app-head">
          <span className="head-desc">面向数据采集运营团队的全链路采集运营平台。覆盖采集策略配置、采集引擎调度、采集结果交付、采集质量巡检、采集成本核算、采集效能分析与采集资源规划的完整运营链路。</span>
          <span className="head-user">当前值班：{operator}</span>
        </header>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/strategy" element={<StrategyView />} />
          <Route path="/engine" element={<EngineView />} />
          <Route path="/delivery" element={<DeliveryView />} />
          <Route path="/inspect" element={<InspectView />} />
          <Route path="/cost" element={<CostView />} />
          <Route path="/efficiency" element={<EfficiencyView />} />
          <Route path="/resource" element={<ResourceView />} />
          <Route path="/crawlrule" element={<CrawlruleView />} />
          <Route path="/datasource" element={<DatasourceView />} />
          <Route path="/cleaning" element={<CleaningView />} />
          <Route path="/storage" element={<StorageView />} />
          <Route path="/monitor" element={<MonitorView />} />
          <Route path="/format" element={<FormatView />} />
          <Route path="/retrylog" element={<RetrylogView />} />
          <Route path="/robotflow" element={<RobotflowView />} />
          <Route path="/datatag" element={<DatatagView />} />
        </Routes>
      </main>
    </div>
  )
}
