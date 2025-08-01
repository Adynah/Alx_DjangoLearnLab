# 📚 Role-Based Permissions & Groups Setup

This project implements a custom role-based access system using Django’s Groups and Permissions.

## 👥 User Groups and Their Permissions

### 1. Admin
- **Access Level**: Full access
- **Permissions**:
  - can_view
  - can_create
  - can_edit
  - can_delete
- **User flag**: is_staff = ✅, is_superuser = ✅

---

### 2. Librarian
- **Access Level**: Book management only
- **Permissions**:
  - can_view
  - can_create
  - can_edit
  - can_delete
- **User flag**: is_staff = ✅, is_superuser = ❌

---

### 3. Member
- **Access Level**: Read-only access to book data
- **Permissions**:
  - can_view
- **User flag**: is_staff = ❌, is_superuser = ❌

---

## 🔐 How Permissions Work

Each permission is defined in `bookshelf/models.py` under `Book.Meta.permissions`. They are used to restrict or allow access to views or actions.

| Permission Code | Description             |
|-----------------|-------------------------|
| `can_view`      | View book records       |
| `can_create`    | Add new books           |
| `can_edit`      | Edit book details       |
| `can_delete`    | Delete books            |

---

## ✅ Admin Setup Instructions

1. Go to Django Admin → Groups → Add
2. Name the group (e.g., **Librarian**, **Member**, etc.)
3. Assign the appropriate permissions by filtering for `Book` model permissions:
   - Use `Ctrl/Cmd` to select: `Can view book`, `Can create book`, etc.
4. Save and assign users to these groups from the **Users** section.

---

## 🛠 Developers Note

In your views, you can restrict actions using:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...
