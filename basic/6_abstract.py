# -*- coding: utf-8 -*-
import abc


class Model:
    def __init__(self, name: str):
        self.name = name


class Client:
    def __init__(self, name: str):
        self.name = name

    def connect(self):
        print(f"Client {self.name} connects")

    def disconnect(self):
        print(f"Client {self.name} disconnects")

    def power_command(self):
        print(f"Cleint {self.name} power_command")
        return True


class VMwareBase(abc.ABC):
    class_name = "VM"

    @abc.abstractmethod
    def check_connectivity(self) -> bool:
        raise NotImplementedError(f"{self} check_connectivity hasn't implemented")

    def base_power_on(self, model: Model, client: Client):
        try:
            done = client.power_command() and self.check_connectivity()
        except Exception as error:
            print(f"error from _power_on: {error}")

        if done:
            print(f"{self.class_name} {model} has powered on")
        else:
            print(f"{self.class_name} {model} couldn't power on")


class VMsVmware(VMwareBase):
    def check_connectivity(self) -> bool:
        print("VMsVmware check connectivity")
        return True

    def power_on(self):
        vm = Model("vm")
        client = Client("vm")
        try:
            client.connect()
            self.base_power_on(vm, client)
        except Exception as exc:
            print("VMsVmware power on error")
        finally:
            client.disconnect()


VMsVmware().power_on()
