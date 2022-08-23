# content of test_expectation.py
import enum
from unittest import mock
import pytest
import os

    
    
# this will operate the test case for serveral times with different parameters
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


class vm:
    vcpu: int
    @classmethod
    def make_example(cls, value):
        vm_ = cls()
        vm_.vcpu = value
        return vm_
    
# class hv:
#     vcpu: int
#     @classmethod
#     def make_example(cls, value):
#         hv_ = cls()
#         hv_.vcpu = value
#         return hv_

class hv(str, enum.Enum):
    KVM = "kvm"
    VMware = "vmware"

# the upper decorator, the early the argument is sent to the function
@pytest.mark.parametrize(argnames="mock_vm", argvalues=[vm.make_example(value=4)])
@pytest.mark.parametrize(argnames="mock_hv", argvalues=[hv.KVM, hv.VMware])
def test_patch_with_parametrize(mock_vm, mock_hv: str):
    print()
    print("mock_vm: ", mock_vm.vcpu)
    print("mock_hv ", mock_hv.__class__, mock_hv.value)

    
# python3 -m pytest -s -rx pytest_practise/7_mark_parametrize.py