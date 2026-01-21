# Alx_DjangoLearnLab
# advanced_features_and_security
# Article Permissions & Groups Setup

## Custom Permissions
The Article model defines the following custom permissions:

- can_view   – View article details
- can_create – Create new articles
- can_edit   – Edit existing articles
- can_delete – Delete articles

These permissions are defined in Article.Meta.permissions and created
automatically during database migration.

## Groups Configuration

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

Groups are managed via the Django Admin panel.

## Permission Enforcement
Views are protected using Django’s @permission_required decorator:

Example:
@permission_required("articles.can_edit", raise_exception=True)

Unauthorized access results in a 403 Forbidden response.

## Best Practices
- Assign permissions via groups, not directly to users
- Use settings.AUTH_USER_MODEL for all user relationships
- Keep permission names consistent (can_view, can_create, etc.)
