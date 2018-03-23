import ansible.constants
import ansible.utils
import ansible.errors

from pytest_ansible.logger import get_logger
from pytest_ansible.module_dispatcher.v2 import ModuleDispatcherV2

log = get_logger(__name__)


class ModuleDispatcherV24(ModuleDispatcherV2):

    def has_module(self, name):
        return ansible.plugins.loader.module_loader.has_plugin(name)
