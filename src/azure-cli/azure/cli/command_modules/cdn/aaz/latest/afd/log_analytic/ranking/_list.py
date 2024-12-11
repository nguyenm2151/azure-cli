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
    "afd log-analytic ranking list",
)
class List(AAZCommand):
    """Get log analytics ranking report for AFD profile
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/getloganalyticsrankings", "2024-09-01"],
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
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group. which is unique within the resource group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.custom_domains = AAZListArg(
            options=["--custom-domains"],
            help="The domains to be included.",
        )
        _args_schema.date_time_begin = AAZDateTimeArg(
            options=["--date-time-begin"],
            help="The start datetime.",
            required=True,
        )
        _args_schema.date_time_end = AAZDateTimeArg(
            options=["--date-time-end"],
            help="The end datetime.",
            required=True,
        )
        _args_schema.max_ranking = AAZIntArg(
            options=["--max-ranking"],
            help="The maximum number of rows to return based on the ranking.",
            required=True,
        )
        _args_schema.metrics = AAZListArg(
            options=["--metrics"],
            required=True,
        )
        _args_schema.rankings = AAZListArg(
            options=["--rankings"],
            required=True,
        )

        custom_domains = cls._args_schema.custom_domains
        custom_domains.Element = AAZStrArg()

        metrics = cls._args_schema.metrics
        metrics.Element = AAZStrArg(
            enum={"clientRequestCount": "clientRequestCount", "clientRequestTraffic": "clientRequestTraffic", "errorCount": "errorCount", "hitCount": "hitCount", "missCount": "missCount", "userErrorCount": "userErrorCount"},
        )

        rankings = cls._args_schema.rankings
        rankings.Element = AAZStrArg(
            enum={"browser": "browser", "countryOrRegion": "countryOrRegion", "referrer": "referrer", "url": "url", "userAgent": "userAgent"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.LogAnalyticsGetLogAnalyticsRankings(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class LogAnalyticsGetLogAnalyticsRankings(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getLogAnalyticsRankings",
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
                    "profileName", self.ctx.args.profile_name,
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
                    "customDomains", self.ctx.args.custom_domains,
                ),
                **self.serialize_query_param(
                    "dateTimeBegin", self.ctx.args.date_time_begin,
                    required=True,
                ),
                **self.serialize_query_param(
                    "dateTimeEnd", self.ctx.args.date_time_end,
                    required=True,
                ),
                **self.serialize_query_param(
                    "maxRanking", self.ctx.args.max_ranking,
                    required=True,
                ),
                **self.serialize_query_param(
                    "metrics", self.ctx.args.metrics,
                    required=True,
                ),
                **self.serialize_query_param(
                    "rankings", self.ctx.args.rankings,
                    required=True,
                ),
                **self.serialize_query_param(
                    "api-version", "2024-09-01",
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
            _schema_on_200.date_time_begin = AAZStrType(
                serialized_name="dateTimeBegin",
            )
            _schema_on_200.date_time_end = AAZStrType(
                serialized_name="dateTimeEnd",
            )
            _schema_on_200.tables = AAZListType()

            tables = cls._schema_on_200.tables
            tables.Element = AAZObjectType()

            _element = cls._schema_on_200.tables.Element
            _element.data = AAZListType()
            _element.ranking = AAZStrType()

            data = cls._schema_on_200.tables.Element.data
            data.Element = AAZObjectType()

            _element = cls._schema_on_200.tables.Element.data.Element
            _element.metrics = AAZListType()
            _element.name = AAZStrType()

            metrics = cls._schema_on_200.tables.Element.data.Element.metrics
            metrics.Element = AAZObjectType()

            _element = cls._schema_on_200.tables.Element.data.Element.metrics.Element
            _element.metric = AAZStrType()
            _element.percentage = AAZFloatType()
            _element.value = AAZIntType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
