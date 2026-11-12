import { useEffect, useState } from 'react'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const fallbackCards = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
const fallbackModules = [{"name": "采集策略配置", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集引擎调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集结果交付", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集质量巡检", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集成本核算", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集效能分析", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集资源规划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "网页抽取规则", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集源管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集数据清洗", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集存储管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集监控大屏", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集格式转换", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集重试日志", "created": 0, "pending": 0, "abnormal": 0}, {"name": "RPA流程模板", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采集数据标注", "created": 0, "pending": 0, "abnormal": 0}]

export default function Overview() {
  const [cards, setCards] = useState<Overview['cards']>(fallbackCards)
  const [moduleRows, setModuleRows] = useState<Overview['modules']>(fallbackModules)

  useEffect(() => {
    fetchJson<Overview>('/api/overview')
      .then((payload) => {
        setCards(payload.cards)
        setModuleRows(payload.modules)
      })
      .catch(() => undefined)
  }, [])

  return (
    <section className="page">
      <header className="page-head">
        <div>
          <h2>运营概览</h2>
          <p className="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
        </div>
      </header>
      <div className="stat-row">
        {cards.map((card) => (
          <article key={card.label} className="stat-card">
            <span className="stat-label">{card.label}</span>
            <strong className="stat-value">{card.value}</strong>
          </article>
        ))}
      </div>
      <table className="data-table">
        <thead>
          <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
        </thead>
        <tbody>
          {moduleRows.map((row) => (
            <tr key={row.name}>
              <td>{row.name}</td>
              <td>{row.created}</td>
              <td>{row.pending}</td>
              <td>{row.abnormal}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
