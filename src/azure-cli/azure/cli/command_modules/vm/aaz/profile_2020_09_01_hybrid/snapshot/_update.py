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
    "snapshot update",
)
class Update(AAZCommand):
    """Update a snapshot.

    :example: Update a snapshot and associate it with a disk access resource.
        az snapshot update --name MySnapshot --resource-group MyResourceGroup --network-access-policy AllowPrivate --disk-access MyDiskAccessID

    :example: Update a snapshot.
        az snapshot update --name MySnapshot --resource-group MyResourceGroup --subscription MySubscription
    """

    _aaz_info = {
        "version": "2019-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/snapshots/{}", "2019-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="The sku name.",
            nullable=True,
            enum={"Premium_LRS": "Premium_LRS", "Standard_LRS": "Standard_LRS", "Standard_ZRS": "Standard_ZRS"},
        )

        # define Arg Group "Encryption"

        _args_schema = cls._args_schema
        _args_schema.disk_encryption_set_id = AAZStrArg(
            options=["--disk-encryption-set-id"],
            arg_group="Encryption",
            help="ID of disk encryption set that is used to encrypt the disk.",
            nullable=True,
        )
        _args_schema.encryption_type = AAZStrArg(
            options=["--encryption-type"],
            arg_group="Encryption",
            help={"short-summary": "Encryption type.", "long-summary": "EncryptionAtRestWithPlatformKey: Disk is encrypted with XStore managed key at rest. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted with Customer managed key at rest."},
            nullable=True,
            enum={"EncryptionAtRestWithCustomerKey": "EncryptionAtRestWithCustomerKey", "EncryptionAtRestWithPlatformKey": "EncryptionAtRestWithPlatformKey"},
        )

        # define Arg Group "Properties"

        # define Arg Group "Snapshot"
        return cls._args_schema

    _args_source_vault_update = None

    @classmethod
    def _build_args_source_vault_update(cls, _schema):
        if cls._args_source_vault_update is not None:
            _schema.id = cls._args_source_vault_update.id
            return

        cls._args_source_vault_update = AAZObjectArg()

        source_vault_update = cls._args_source_vault_update
        source_vault_update.id = AAZStrArg(
            options=["id"],
            help="Resource Id",
            nullable=True,
        )

        _schema.id = cls._args_source_vault_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.SnapshotsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.SnapshotsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
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
                    "api-version", "2019-07-01",
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
            _UpdateHelper._build_schema_snapshot_read(cls._schema_on_200)

            return cls._schema_on_200

    class SnapshotsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                    "api-version", "2019-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

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
            _UpdateHelper._build_schema_snapshot_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("encryption", AAZObjectType)

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("diskEncryptionSetId", AAZStrType, ".disk_encryption_set_id")
                encryption.set_prop("type", AAZStrType, ".encryption_type")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_source_vault_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_snapshot_read = None

    @classmethod
    def _build_schema_snapshot_read(cls, _schema):
        if cls._schema_snapshot_read is not None:
            _schema.id = cls._schema_snapshot_read.id
            _schema.location = cls._schema_snapshot_read.location
            _schema.managed_by = cls._schema_snapshot_read.managed_by
            _schema.name = cls._schema_snapshot_read.name
            _schema.properties = cls._schema_snapshot_read.properties
            _schema.sku = cls._schema_snapshot_read.sku
            _schema.tags = cls._schema_snapshot_read.tags
            _schema.type = cls._schema_snapshot_read.type
            return

        cls._schema_snapshot_read = _schema_snapshot_read = AAZObjectType()

        snapshot_read = _schema_snapshot_read
        snapshot_read.id = AAZStrType(
            flags={"read_only": True},
        )
        snapshot_read.location = AAZStrType(
            flags={"required": True},
        )
        snapshot_read.managed_by = AAZStrType(
            serialized_name="managedBy",
            flags={"read_only": True},
        )
        snapshot_read.name = AAZStrType(
            flags={"read_only": True},
        )
        snapshot_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        snapshot_read.sku = AAZObjectType()
        snapshot_read.tags = AAZDictType()
        snapshot_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_snapshot_read.properties
        properties.creation_data = AAZObjectType(
            serialized_name="creationData",
            flags={"required": True},
        )
        properties.disk_size_bytes = AAZIntType(
            serialized_name="diskSizeBytes",
            flags={"read_only": True},
        )
        properties.disk_size_gb = AAZIntType(
            serialized_name="diskSizeGB",
        )
        properties.encryption = AAZObjectType()
        properties.encryption_settings_collection = AAZObjectType(
            serialized_name="encryptionSettingsCollection",
        )
        properties.hyper_v_generation = AAZStrType(
            serialized_name="hyperVGeneration",
        )
        properties.incremental = AAZBoolType()
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
        properties.unique_id = AAZStrType(
            serialized_name="uniqueId",
            flags={"read_only": True},
        )

        creation_data = _schema_snapshot_read.properties.creation_data
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
        creation_data.source_unique_id = AAZStrType(
            serialized_name="sourceUniqueId",
            flags={"read_only": True},
        )
        creation_data.source_uri = AAZStrType(
            serialized_name="sourceUri",
        )
        creation_data.storage_account_id = AAZStrType(
            serialized_name="storageAccountId",
        )
        creation_data.upload_size_bytes = AAZIntType(
            serialized_name="uploadSizeBytes",
        )

        image_reference = _schema_snapshot_read.properties.creation_data.image_reference
        image_reference.id = AAZStrType()
        image_reference.lun = AAZIntType()

        encryption = _schema_snapshot_read.properties.encryption
        encryption.disk_encryption_set_id = AAZStrType(
            serialized_name="diskEncryptionSetId",
        )
        encryption.type = AAZStrType()

        encryption_settings_collection = _schema_snapshot_read.properties.encryption_settings_collection
        encryption_settings_collection.enabled = AAZBoolType(
            flags={"required": True},
        )
        encryption_settings_collection.encryption_settings = AAZListType(
            serialized_name="encryptionSettings",
        )
        encryption_settings_collection.encryption_settings_version = AAZStrType(
            serialized_name="encryptionSettingsVersion",
        )

        encryption_settings = _schema_snapshot_read.properties.encryption_settings_collection.encryption_settings
        encryption_settings.Element = AAZObjectType()

        _element = _schema_snapshot_read.properties.encryption_settings_collection.encryption_settings.Element
        _element.disk_encryption_key = AAZObjectType(
            serialized_name="diskEncryptionKey",
        )
        _element.key_encryption_key = AAZObjectType(
            serialized_name="keyEncryptionKey",
        )

        disk_encryption_key = _schema_snapshot_read.properties.encryption_settings_collection.encryption_settings.Element.disk_encryption_key
        disk_encryption_key.secret_url = AAZStrType(
            serialized_name="secretUrl",
            flags={"required": True},
        )
        disk_encryption_key.source_vault = AAZObjectType(
            serialized_name="sourceVault",
            flags={"required": True},
        )
        cls._build_schema_source_vault_read(disk_encryption_key.source_vault)

        key_encryption_key = _schema_snapshot_read.properties.encryption_settings_collection.encryption_settings.Element.key_encryption_key
        key_encryption_key.key_url = AAZStrType(
            serialized_name="keyUrl",
            flags={"required": True},
        )
        key_encryption_key.source_vault = AAZObjectType(
            serialized_name="sourceVault",
            flags={"required": True},
        )
        cls._build_schema_source_vault_read(key_encryption_key.source_vault)

        sku = _schema_snapshot_read.sku
        sku.name = AAZStrType()
        sku.tier = AAZStrType(
            flags={"read_only": True},
        )

        tags = _schema_snapshot_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_snapshot_read.id
        _schema.location = cls._schema_snapshot_read.location
        _schema.managed_by = cls._schema_snapshot_read.managed_by
        _schema.name = cls._schema_snapshot_read.name
        _schema.properties = cls._schema_snapshot_read.properties
        _schema.sku = cls._schema_snapshot_read.sku
        _schema.tags = cls._schema_snapshot_read.tags
        _schema.type = cls._schema_snapshot_read.type

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


__all__ = ["Update"]
