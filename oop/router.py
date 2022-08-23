class HypervisorRule(QueryRule):
    # pylint: disable=too-many-instance-attributes
    hostname = FilterLike.new_class(Hypervisor.hostname)
    mgmt_ip = FilterEqual.new_class(Hypervisor.mgmt_ip)
    virtualization_provider = FilterEqual.new_class(Hypervisor.virtualization_provider)
    provisioned_status = FilterEqual.new_class(Hypervisor.provisioned_status)
    os_state = FilterEqual.new_class(Hypervisor.os_state)
    total_vcpus = FilterMinMax.new_class(Hypervisor.total_vcpus)
    total_memory = FilterMinMax.new_class(Hypervisor.total_memory)
    


async def hypervisor_describe_all(
    self,
    query_rule: HypervisorRule = Depends(HypervisorRule.parse),
):
    pass