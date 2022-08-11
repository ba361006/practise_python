from prometheus_api_client import PrometheusConnect  # type: ignore
from datetime import datetime, timedelta


end = datetime.now()
start = end - timedelta(minutes=1)
# total = await prometheus_client.custom_query_range(query, start, end, "60")

connection = PrometheusConnect("http://127.0.0.1:9090")
response = connection.custom_query(
    "vmware_vm_cpu_usage_average"
)
print(response)

# query = "sum(rate(node_network_transmit_bytes_total[2m])) + sum(rate(node_network_receive_bytes_total[2m]))"  # pylint: disable=line-too-long
# response = connection.custom_query_range(
#     query,
#     start,
#     end,
#     "60",
#     None
# )
    
# print(response)