- /hypervisors  
- ?hostname=vm-0 -> strings compare using LIKE %  
- &mgmt_ip=1.2.3.4 -> IP are compared by strict equality  
- &virtualization_provider=kvm -> enums by strict equality  
- &min_total_vcpus=4 -> all numbers should have min_name and max_name variants, and named equality check when   appriopriate
- &created_after=2022-10-05 -> date and datetime should both be supported, filter names should be name_after and   name_before
- &sort=hostname,total_vcpus -> coma separated list of Literal strings with field names  
- &sortDirection=asc,desc -> Listerals asc and desc, same amount as in sort names  

- http://localhost:20001/api/v1/hypervisors?hostname=abcd&mgmtip=10.10.10.10&virtualizationProvider=kvm&provisioningStatus=provisioned&osState=online&minTotalVcpus=4&maxTotalVcpus=10&minTotalMemory=1200000000&maxTotalMemory=239675961344&sort=hostname,virtualizationProvider&sortDirection=asc,asc