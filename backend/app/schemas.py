"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class StrategyEntry(BaseModel):
    """采集策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标站点
    field_2: str | None = None  # 采集深度
    field_3: str | None = None  # 页面范围
    field_4: str | None = None  # 字段清单
    field_5: str | None = None  # 更新模式
    field_6: str | None = None  # 优先级
    field_7: str | None = None  # 策略状态

class EngineEntry(BaseModel):
    """引擎节点明细结构。"""

    field_0: str | None = None  # 节点编号
    field_1: str | None = None  # 节点地址
    field_2: str | None = None  # 运行状态
    field_3: str | None = None  # 当前任务
    field_4: str | None = None  # 负载率
    field_5: str | None = None  # 内存占用
    field_6: str | None = None  # 心跳时间
    field_7: str | None = None  # 节点标签

class DeliveryEntry(BaseModel):
    """交付记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 采集策略
    field_2: str | None = None  # 交付格式
    field_3: str | None = None  # 数据条数
    field_4: str | None = None  # 交付渠道
    field_5: str | None = None  # 交付时间
    field_6: str | None = None  # 交付校验
    field_7: str | None = None  # 交付状态

class InspectEntry(BaseModel):
    """巡检任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 巡检对象
    field_2: str | None = None  # 巡检类型
    field_3: str | None = None  # 抽样比例
    field_4: str | None = None  # 巡检周期
    field_5: str | None = None  # 异常标准
    field_6: str | None = None  # 巡检结果
    field_7: str | None = None  # 任务状态

class CostEntry(BaseModel):
    """成本账单明细结构。"""

    field_0: str | None = None  # 账单编号
    field_1: str | None = None  # 核算周期
    field_2: str | None = None  # 引擎费用
    field_3: str | None = None  # 带宽费用
    field_4: str | None = None  # 存储费用
    field_5: str | None = None  # 总金额
    field_6: str | None = None  # 成本趋势
    field_7: str | None = None  # 核算状态

class EfficiencyEntry(BaseModel):
    """效能报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 分析维度
    field_2: str | None = None  # 采集量
    field_3: str | None = None  # 成功率
    field_4: str | None = None  # 平均耗时
    field_5: str | None = None  # 资源利用率
    field_6: str | None = None  # 改进建议
    field_7: str | None = None  # 报告时间

class ResourceEntry(BaseModel):
    """资源计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 资源类型
    field_2: str | None = None  # 当前用量
    field_3: str | None = None  # 预计需求
    field_4: str | None = None  # 扩容计划
    field_5: str | None = None  # 预算金额
    field_6: str | None = None  # 审批状态
    field_7: str | None = None  # 计划状态

class CrawlruleEntry(BaseModel):
    """抽取规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 入口地址
    field_2: str | None = None  # 页面选择器
    field_3: str | None = None  # 正文提取
    field_4: str | None = None  # 分页规则
    field_5: str | None = None  # 编码设置
    field_6: str | None = None  # 重试上限
    field_7: str | None = None  # 规则状态

class DatasourceEntry(BaseModel):
    """采集源明细结构。"""

    field_0: str | None = None  # 源编号
    field_1: str | None = None  # 源名称
    field_2: str | None = None  # 源类型
    field_3: str | None = None  # 接入协议
    field_4: str | None = None  # 认证方式
    field_5: str | None = None  # 连接超时
    field_6: str | None = None  # 采集间隔
    field_7: str | None = None  # 源状态

class CleaningEntry(BaseModel):
    """清洗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 清洗类型
    field_3: str | None = None  # 处理表达式
    field_4: str | None = None  # 空值填充
    field_5: str | None = None  # 异常过滤
    field_6: str | None = None  # 清洗批次
    field_7: str | None = None  # 规则状态

class StorageEntry(BaseModel):
    """存储策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 存储路径
    field_2: str | None = None  # 文件格式
    field_3: str | None = None  # 分片大小
    field_4: str | None = None  # 压缩算法
    field_5: str | None = None  # 过期天数
    field_6: str | None = None  # 归档路径
    field_7: str | None = None  # 策略状态

class MonitorEntry(BaseModel):
    """监控指标明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 指标名称
    field_2: str | None = None  # 当前数值
    field_3: str | None = None  # 历史均值
    field_4: str | None = None  # 波动幅度
    field_5: str | None = None  # 告警阈值
    field_6: str | None = None  # 采样时间
    field_7: str | None = None  # 指标状态

class FormatEntry(BaseModel):
    """转换模板明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 输入格式
    field_2: str | None = None  # 输出格式
    field_3: str | None = None  # 字段映射
    field_4: str | None = None  # 数据类型
    field_5: str | None = None  # 编码转换
    field_6: str | None = None  # 错误处理
    field_7: str | None = None  # 模板状态

class RetrylogEntry(BaseModel):
    """重试记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 失败任务
    field_2: str | None = None  # 异常类型
    field_3: str | None = None  # 重试次数
    field_4: str | None = None  # 重试间隔
    field_5: str | None = None  # 最终结果
    field_6: str | None = None  # 消耗时间
    field_7: str | None = None  # 记录状态

class RobotflowEntry(BaseModel):
    """流程模板明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 模板名称
    field_2: str | None = None  # 适用场景
    field_3: str | None = None  # 操作步骤
    field_4: str | None = None  # 输入参数
    field_5: str | None = None  # 执行环境
    field_6: str | None = None  # 预计耗时
    field_7: str | None = None  # 模板状态

class DatatagEntry(BaseModel):
    """标注任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 数据记录
    field_2: str | None = None  # 标注类型
    field_3: str | None = None  # 标注标签
    field_4: str | None = None  # 标注批次
    field_5: str | None = None  # 标注详情
    field_6: str | None = None  # 复核状态
    field_7: str | None = None  # 任务状态
