# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network watcher",
)
class __CMDGroup(AAZCommandGroup):
    """Manage the Azure Network Watcher. Network Watcher assists with monitoring and diagnosing conditions at a network scenario level. To learn more visit https://learn.microsoft.com/azure/network-watcher/.
    """
    pass


__all__ = ["__CMDGroup"]
