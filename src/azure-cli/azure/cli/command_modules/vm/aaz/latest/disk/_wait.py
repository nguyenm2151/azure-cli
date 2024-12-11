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
    "disk wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/disks/{}", "2023-04-02"],
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
        _args_schema.disk_name = AAZStrArg(
            options=["-n", "--name", "--disk-name"],
            help="The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DisksGet(ctx=self.ctx)()
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

    class DisksGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName}",
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
                    "diskName", self.ctx.args.disk_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2023-04-02",
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
            _schema_on_200.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
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
            _schema_on_200.managed_by_extended = AAZListType(
                serialized_name="managedByExtended",
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
            _schema_on_200.zones = AAZListType()

            extended_location = cls._schema_on_200.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            managed_by_extended = cls._schema_on_200.managed_by_extended
            managed_by_extended.Element = AAZStrType()

            properties = cls._schema_on_200.properties
            properties.last_ownership_update_time = AAZStrType(
                serialized_name="LastOwnershipUpdateTime",
                flags={"read_only": True},
            )
            properties.bursting_enabled = AAZBoolType(
                serialized_name="burstingEnabled",
            )
            properties.bursting_enabled_time = AAZStrType(
                serialized_name="burstingEnabledTime",
                flags={"read_only": True},
            )
            properties.completion_percent = AAZFloatType(
                serialized_name="completionPercent",
            )
            properties.creation_data = AAZObjectType(
                serialized_name="creationData",
                flags={"required": True},
            )
            properties.data_access_auth_mode = AAZStrType(
                serialized_name="dataAccessAuthMode",
            )
            properties.disk_access_id = AAZStrType(
                serialized_name="diskAccessId",
            )
            properties.disk_iops_read_only = AAZIntType(
                serialized_name="diskIOPSReadOnly",
            )
            properties.disk_iops_read_write = AAZIntType(
                serialized_name="diskIOPSReadWrite",
            )
            properties.disk_m_bps_read_only = AAZIntType(
                serialized_name="diskMBpsReadOnly",
            )
            properties.disk_m_bps_read_write = AAZIntType(
                serialized_name="diskMBpsReadWrite",
            )
            properties.disk_size_bytes = AAZIntType(
                serialized_name="diskSizeBytes",
                flags={"read_only": True},
            )
            properties.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            properties.disk_state = AAZStrType(
                serialized_name="diskState",
                flags={"read_only": True},
            )
            properties.encryption = AAZObjectType()
            properties.encryption_settings_collection = AAZObjectType(
                serialized_name="encryptionSettingsCollection",
            )
            properties.hyper_v_generation = AAZStrType(
                serialized_name="hyperVGeneration",
            )
            properties.max_shares = AAZIntType(
                serialized_name="maxShares",
            )
            properties.network_access_policy = AAZStrType(
                serialized_name="networkAccessPolicy",
            )
            properties.optimized_for_frequent_attach = AAZBoolType(
                serialized_name="optimizedForFrequentAttach",
            )
            properties.os_type = AAZStrType(
                serialized_name="osType",
            )
            properties.property_updates_in_progress = AAZObjectType(
                serialized_name="propertyUpdatesInProgress",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.purchase_plan = AAZObjectType(
                serialized_name="purchasePlan",
            )
            properties.security_profile = AAZObjectType(
                serialized_name="securityProfile",
            )
            properties.share_info = AAZListType(
                serialized_name="shareInfo",
                flags={"read_only": True},
            )
            properties.supported_capabilities = AAZObjectType(
                serialized_name="supportedCapabilities",
            )
            properties.supports_hibernation = AAZBoolType(
                serialized_name="supportsHibernation",
            )
            properties.tier = AAZStrType()
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )
            properties.unique_id = AAZStrType(
                serialized_name="uniqueId",
                flags={"read_only": True},
            )

            creation_data = cls._schema_on_200.properties.creation_data
            creation_data.create_option = AAZStrType(
                serialized_name="createOption",
                flags={"required": True},
            )
            creation_data.elastic_san_resource_id = AAZStrType(
                serialized_name="elasticSanResourceId",
            )
            creation_data.gallery_image_reference = AAZObjectType(
                serialized_name="galleryImageReference",
            )
            _WaitHelper._build_schema_image_disk_reference_read(creation_data.gallery_image_reference)
            creation_data.image_reference = AAZObjectType(
                serialized_name="imageReference",
            )
            _WaitHelper._build_schema_image_disk_reference_read(creation_data.image_reference)
            creation_data.logical_sector_size = AAZIntType(
                serialized_name="logicalSectorSize",
            )
            creation_data.performance_plus = AAZBoolType(
                serialized_name="performancePlus",
            )
            creation_data.security_data_uri = AAZStrType(
                serialized_name="securityDataUri",
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

            encryption = cls._schema_on_200.properties.encryption
            encryption.disk_encryption_set_id = AAZStrType(
                serialized_name="diskEncryptionSetId",
            )
            encryption.type = AAZStrType()

            encryption_settings_collection = cls._schema_on_200.properties.encryption_settings_collection
            encryption_settings_collection.enabled = AAZBoolType(
                flags={"required": True},
            )
            encryption_settings_collection.encryption_settings = AAZListType(
                serialized_name="encryptionSettings",
            )
            encryption_settings_collection.encryption_settings_version = AAZStrType(
                serialized_name="encryptionSettingsVersion",
            )

            encryption_settings = cls._schema_on_200.properties.encryption_settings_collection.encryption_settings
            encryption_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.encryption_settings_collection.encryption_settings.Element
            _element.disk_encryption_key = AAZObjectType(
                serialized_name="diskEncryptionKey",
            )
            _element.key_encryption_key = AAZObjectType(
                serialized_name="keyEncryptionKey",
            )

            disk_encryption_key = cls._schema_on_200.properties.encryption_settings_collection.encryption_settings.Element.disk_encryption_key
            disk_encryption_key.secret_url = AAZStrType(
                serialized_name="secretUrl",
                flags={"required": True},
            )
            disk_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _WaitHelper._build_schema_source_vault_read(disk_encryption_key.source_vault)

            key_encryption_key = cls._schema_on_200.properties.encryption_settings_collection.encryption_settings.Element.key_encryption_key
            key_encryption_key.key_url = AAZStrType(
                serialized_name="keyUrl",
                flags={"required": True},
            )
            key_encryption_key.source_vault = AAZObjectType(
                serialized_name="sourceVault",
                flags={"required": True},
            )
            _WaitHelper._build_schema_source_vault_read(key_encryption_key.source_vault)

            property_updates_in_progress = cls._schema_on_200.properties.property_updates_in_progress
            property_updates_in_progress.target_tier = AAZStrType(
                serialized_name="targetTier",
            )

            purchase_plan = cls._schema_on_200.properties.purchase_plan
            purchase_plan.name = AAZStrType(
                flags={"required": True},
            )
            purchase_plan.product = AAZStrType(
                flags={"required": True},
            )
            purchase_plan.promotion_code = AAZStrType(
                serialized_name="promotionCode",
            )
            purchase_plan.publisher = AAZStrType(
                flags={"required": True},
            )

            security_profile = cls._schema_on_200.properties.security_profile
            security_profile.secure_vm_disk_encryption_set_id = AAZStrType(
                serialized_name="secureVMDiskEncryptionSetId",
            )
            security_profile.security_type = AAZStrType(
                serialized_name="securityType",
            )

            share_info = cls._schema_on_200.properties.share_info
            share_info.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.share_info.Element
            _element.vm_uri = AAZStrType(
                serialized_name="vmUri",
                flags={"read_only": True},
            )

            supported_capabilities = cls._schema_on_200.properties.supported_capabilities
            supported_capabilities.accelerated_network = AAZBoolType(
                serialized_name="acceleratedNetwork",
            )
            supported_capabilities.architecture = AAZStrType()
            supported_capabilities.disk_controller_types = AAZStrType(
                serialized_name="diskControllerTypes",
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_image_disk_reference_read = None

    @classmethod
    def _build_schema_image_disk_reference_read(cls, _schema):
        if cls._schema_image_disk_reference_read is not None:
            _schema.community_gallery_image_id = cls._schema_image_disk_reference_read.community_gallery_image_id
            _schema.id = cls._schema_image_disk_reference_read.id
            _schema.lun = cls._schema_image_disk_reference_read.lun
            _schema.shared_gallery_image_id = cls._schema_image_disk_reference_read.shared_gallery_image_id
            return

        cls._schema_image_disk_reference_read = _schema_image_disk_reference_read = AAZObjectType()

        image_disk_reference_read = _schema_image_disk_reference_read
        image_disk_reference_read.community_gallery_image_id = AAZStrType(
            serialized_name="communityGalleryImageId",
        )
        image_disk_reference_read.id = AAZStrType()
        image_disk_reference_read.lun = AAZIntType()
        image_disk_reference_read.shared_gallery_image_id = AAZStrType(
            serialized_name="sharedGalleryImageId",
        )

        _schema.community_gallery_image_id = cls._schema_image_disk_reference_read.community_gallery_image_id
        _schema.id = cls._schema_image_disk_reference_read.id
        _schema.lun = cls._schema_image_disk_reference_read.lun
        _schema.shared_gallery_image_id = cls._schema_image_disk_reference_read.shared_gallery_image_id

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
