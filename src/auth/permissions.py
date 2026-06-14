PERMISSIONS = {
    "admin": ["read", "write", "delete", "manage_users", "export_data"],
    "user": ["read", "write", "upload"],
    "guest": ["read"],
    "moderator": ["read", "write", "delete"]
}

def can_delete(role):
    return "delete" in PERMISSIONS.get(role, [])

def can_manage(role):
    return "manage_users" in PERMISSIONS.get(role, [])

def get_permissions(role):
    return PERMISSIONS.get(role, [])
