# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 5.3.0


from . import AWSObject
from . import AWSProperty


class Admins(AWSProperty):
    props = {
    }


class DataLakeSettings(AWSObject):
    resource_type = "AWS::LakeFormation::DataLakeSettings"

    props = {
        'Admins': (Admins, False),
    }


class DataLakePrincipal(AWSProperty):
    props = {
        'DataLakePrincipalIdentifier': (basestring, False),
    }


class DatabaseResource(AWSProperty):
    props = {
        'Name': (basestring, False),
    }


class TableResource(AWSProperty):
    props = {
        'DatabaseName': (basestring, False),
        'Name': (basestring, False),
    }


class DataLocationResource(AWSProperty):
    props = {
        'S3Resource': (basestring, False),
    }


class ColumnWildcard(AWSProperty):
    props = {
        'ExcludedColumnNames': ([basestring], False),
    }


class TableWithColumnsResource(AWSProperty):
    props = {
        'ColumnNames': ([basestring], False),
        'ColumnWildcard': (ColumnWildcard, False),
        'DatabaseName': (basestring, False),
        'Name': (basestring, False),
    }


class Resource(AWSProperty):
    props = {
        'DatabaseResource': (DatabaseResource, False),
        'DataLocationResource': (DataLocationResource, False),
        'TableResource': (TableResource, False),
        'TableWithColumnsResource': (TableWithColumnsResource, False),
    }


class Permissions(AWSObject):
    resource_type = "AWS::LakeFormation::Permissions"

    props = {
        'DataLakePrincipal': (DataLakePrincipal, True),
        'Permissions': ([basestring], False),
        'PermissionsWithGrantOption': ([basestring], False),
        'Resource': (Resource, True),
    }
