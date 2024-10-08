from django.db import migrations
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ManyToManyDescriptor,
)

plugin = {
    "python_module": {
        "health_check_schedule": None,
        "update_schedule": None,
        "module": "download_file_from_uri.DownloadFileFromUri",
        "base_path": "api_app.analyzers_manager.observable_analyzers",
    },
    "name": "DownloadFileFromUri",
    "description": "performs an http request to an uri and download the file through the http proxy",
    "disabled": False,
    "soft_time_limit": 60,
    "routing_key": "default",
    "health_check_status": True,
    "type": "observable",
    "docker_based": False,
    "maximum_tlp": "RED",
    "observable_supported": ["url"],
    "supported_filetypes": [],
    "run_hash": False,
    "run_hash_type": "",
    "not_supported_filetypes": [],
    "model": "analyzers_manager.AnalyzerConfig",
}

params = [
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "http_proxy",
        "type": "str",
        "description": "http proxy url",
        "is_secret": True,
        "required": True,
    },
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "header_user_agent",
        "type": "str",
        "description": "http header user-agent field",
        "is_secret": False,
        "required": True,
    },
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "header_cookies",
        "type": "str",
        "description": "http header cookies field (e.g. $Version=1; Skin=new;)",
        "is_secret": False,
        "required": True,
    },
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "header_content_type",
        "type": "str",
        "description": "http header content-type field",
        "is_secret": False,
        "required": True,
    },
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "header_accept",
        "type": "str",
        "description": "http header accept field",
        "is_secret": False,
        "required": True,
    },
    {
        "python_module": {
            "module": "download_file_from_uri.DownloadFileFromUri",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "timeout",
        "type": "int",
        "description": "http requests timeout",
        "is_secret": False,
        "required": True,
    },
]

values = [
    {
        "parameter": {
            "python_module": {
                "module": "download_file_from_uri.DownloadFileFromUri",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "header_user_agent",
            "type": "str",
            "description": "http header user-agent field",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "DownloadFileFromUri",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/125.0.2535.92",
        "updated_at": "2024-06-19T10:23:03.145744Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "download_file_from_uri.DownloadFileFromUri",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "header_cookies",
            "type": "str",
            "description": "http header cookies field (e.g. $Version=1; Skin=new;)",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "DownloadFileFromUri",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "",
        "updated_at": "2024-06-19T10:23:03.145744Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "download_file_from_uri.DownloadFileFromUri",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "header_content_type",
            "type": "str",
            "description": "http header content-type field",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "DownloadFileFromUri",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "application/octet-stream",
        "updated_at": "2024-06-19T10:23:03.145744Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "download_file_from_uri.DownloadFileFromUri",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "header_accept",
            "type": "str",
            "description": "http header accept field",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "DownloadFileFromUri",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "application/octet-stream",
        "updated_at": "2024-06-19T10:23:03.145744Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "download_file_from_uri.DownloadFileFromUri",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "timeout",
            "type": "int",
            "description": "http requests timeout",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "DownloadFileFromUri",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": 50,
        "updated_at": "2024-06-19T10:23:03.145744Z",
        "owner": None,
    },
]


def _get_real_obj(Model, field, value):
    def _get_obj(Model, other_model, value):
        if isinstance(value, dict):
            real_vals = {}
            for key, real_val in value.items():
                real_vals[key] = _get_real_obj(other_model, key, real_val)
            value = other_model.objects.get_or_create(**real_vals)[0]
        # it is just the primary key serialized
        else:
            if isinstance(value, int):
                if Model.__name__ == "PluginConfig":
                    value = other_model.objects.get(name=plugin["name"])
                else:
                    value = other_model.objects.get(pk=value)
            else:
                value = other_model.objects.get(name=value)
        return value

    if (
        type(getattr(Model, field))
        in [ForwardManyToOneDescriptor, ForwardOneToOneDescriptor]
        and value
    ):
        other_model = getattr(Model, field).get_queryset().model
        value = _get_obj(Model, other_model, value)
    elif type(getattr(Model, field)) in [ManyToManyDescriptor] and value:
        other_model = getattr(Model, field).rel.model
        value = [_get_obj(Model, other_model, val) for val in value]
    return value


def _create_object(Model, data):
    mtm, no_mtm = {}, {}
    for field, value in data.items():
        value = _get_real_obj(Model, field, value)
        if type(getattr(Model, field)) is ManyToManyDescriptor:
            mtm[field] = value
        else:
            no_mtm[field] = value
    try:
        o = Model.objects.get(**no_mtm)
    except Model.DoesNotExist:
        o = Model(**no_mtm)
        o.full_clean()
        o.save()
        for field, value in mtm.items():
            attribute = getattr(o, field)
            if value is not None:
                attribute.set(value)
        return False
    return True


def migrate(apps, schema_editor):
    Parameter = apps.get_model("api_app", "Parameter")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    if not Model.objects.filter(name=plugin["name"]).exists():
        exists = _create_object(Model, plugin)
        if not exists:
            for param in params:
                _create_object(Parameter, param)
            for value in values:
                _create_object(PluginConfig, value)


def reverse_migrate(apps, schema_editor):
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    Model.objects.get(name=plugin["name"]).delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("api_app", "0062_alter_parameter_python_module"),
        ("analyzers_manager", "0099_analyzer_config_spamhaus_wqs"),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]
