# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "snapshot wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/snapshots/{}", "2017-03-30"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.snapshot_name = AAZStrArg(
            options=["-n", "--name", "--snapshot-name"],
            help="The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The max name length is 80 characters.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SnapshotsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class SnapshotsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "snapshotName", self.ctx.args.snapshot_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2017-03-30",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.managed_by = AAZStrType(
                serialized_name="managedBy",
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.creation_data = AAZObjectType(
                serialized_name="creationData",
                flags={"required": True},
            )
            properties.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            properties.encryption_settings = AAZObjectType(
                serialized_name="encryptionSettings",
            )
            properties.os_type = AAZStrType(
                serialized_name="osType",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )

            creation_data = cls._schema_on_200.properties.creation_data
            creation_data.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            creation_data.image_reference = AAZObjectType(
                serialized_name="imageReference",
            )
            creation_data.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            creation_data.source_uri = AAZStrType(
                serialized_name="sourceUri",
            )
            creation_data.storage_account_id = AAZStrType(
                serialized_name="storageAccountId",
            )

            image_reference = cls._schema_on_200.properties.creation_data.image_reference
            image_reference.id = AAZStrType()
            image_reference.lun = AAZIntType()

            encryption_settings = cls._schema_on_200.properties.encryption_settings
            encryption_settings.disk_encryption_key = AAZObjectType(
                serialized_name="diskEncryptionKey",
            )
            encryption_settings.enabled = AAZBoolType()
            encryption_settings.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            disk_encryption_key = cls._schema_on_200.properties.encryption_settings.disk_encryption_key
            disk_encryption_key.secret_url = AAZStrType(
                serialized_name="secretUrl",
                flags={"required": True},
            )
            disk_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _WaitHelper._build_schema_source_vault_read(disk_encryption_key.source_vault)

            key_encryption_key = cls._schema_on_200.properties.encryption_settings.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _WaitHelper._build_schema_source_vault_read(key_encryption_key.source_vault)

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_source_vault_read = None

    @classmethod
    def _build_schema_source_vault_read(cls, _schema):
        if cls._schema_source_vault_read is not None:
            _schema.id = cls._schema_source_vault_read.id
            return

        cls._schema_source_vault_read = _schema_source_vault_read = AAZObjectType()

        source_vault_read = _schema_source_vault_read
        source_vault_read.id = AAZStrType()

        _schema.id = cls._schema_source_vault_read.id


__all__ = ["Wait"]
