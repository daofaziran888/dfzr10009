"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import strategy as router_strategy
from app.routers import engine as router_engine
from app.routers import delivery as router_delivery
from app.routers import inspect as router_inspect
from app.routers import cost as router_cost
from app.routers import efficiency as router_efficiency
from app.routers import resource as router_resource
from app.routers import crawlrule as router_crawlrule
from app.routers import datasource as router_datasource
from app.routers import cleaning as router_cleaning
from app.routers import storage as router_storage
from app.routers import monitor as router_monitor
from app.routers import format as router_format
from app.routers import retrylog as router_retrylog
from app.routers import robotflow as router_robotflow
from app.routers import datatag as router_datatag

ROUTERS = [router_strategy, router_engine, router_delivery, router_inspect, router_cost, router_efficiency, router_resource, router_crawlrule, router_datasource, router_cleaning, router_storage, router_monitor, router_format, router_retrylog, router_robotflow, router_datatag]
