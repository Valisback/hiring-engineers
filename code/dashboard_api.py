from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.log_query_definition_group_by import LogQueryDefinitionGroupBy
from datadog_api_client.v1.model.log_query_definition_group_by_sort import LogQueryDefinitionGroupBySort
from datadog_api_client.v1.model.log_query_definition_search import LogQueryDefinitionSearch
from datadog_api_client.v1.model.logs_query_compute import LogsQueryCompute
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
from datadog_api_client.v1.model.query_value_widget_definition_type import QueryValueWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest

from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_sort import WidgetSort

body = Dashboard(
    layout_type=DashboardLayoutType("ordered"),
    title="This Dashboard was created with an API call!",
    widgets=[
        Widget(
            definition=TimeseriesWidgetDefinition(
                type=TimeseriesWidgetDefinitionType("timeseries"),
                requests=[
                    TimeseriesWidgetRequest(
                        profile_metrics_query=LogQueryDefinition(
                            compute=LogsQueryCompute(aggregation="sum", facet="@prof_core_cpu_cores"),
                            search=LogQueryDefinitionSearch(query="avg:my_metric{host:vagrant}"),
                            group_by=[
                                LogQueryDefinitionGroupBy(
                                    facet="service",
                                    limit=10,
                                    sort=LogQueryDefinitionGroupBySort(
                                        aggregation="sum", order=WidgetSort("desc"), facet="@prof_core_cpu_cores"
                                    ),
                                )
                            ],
                        )
                    )
                ],
            )
        ), 
        Widget(
            definition=QueryValueWidgetDefinition(
                type=QueryValueWidgetDefinitionType("query_value"),
                requests=[
                    QueryValueWidgetRequest(
                        profile_metrics_query=LogQueryDefinition(
                            compute=LogsQueryCompute(aggregation="sum", facet="@prof_core_cpu_cores"),
                            search=LogQueryDefinitionSearch(query="avg:my_metric{host:vagrant}"),
                            group_by=[
                                LogQueryDefinitionGroupBy(
                                    facet="service",
                                    limit=10,
                                    sort=LogQueryDefinitionGroupBySort(
                                        aggregation="sum", order=WidgetSort("desc"), facet="@prof_core_cpu_cores"
                                    ),
                                )
                            ],
                        )
                    )
                ],
            )
        )
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.create_dashboard(body=body)

    print(response)