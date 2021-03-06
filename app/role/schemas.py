from app import ma
from app.core.base_schema import BaseSchema
from app.permission.schemas import PermissionSchema
from app.role.models import Role, RolePermission


class RolePermissionSchema(ma.ModelSchema, BaseSchema):
    permission = ma.Nested(
        PermissionSchema(only=('name', 'description',)))

    class Meta:
        model = RolePermission


class RoleSchema(ma.ModelSchema, BaseSchema):
    permissions = ma.List(ma.Nested(
        RolePermissionSchema(only=('permission',))))

    class Meta:
        model = Role
