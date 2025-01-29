 Ansible role: user_management
===

Manage users, their SSH public key enrollment and sudoers files via Ansible on Linux systems.

Requirements
---

- Collections:
  - community.general
- Min. Ansible version: 2.11

Role Variables
---

main
---

| Variable | Type | Required | Choices | Default | Description |
| --- | --- | --- | --- | --- | --- |
| `user_management_default_home_root` | `str` | `false` | | `None` | Custom default `$HOME` root path. Omitted if `null`. |
| `user_management_default_home_move` | `bool` | `false` | `false`, `true` | `false` | If set to `true` when used with `home`, attempt to move the user's old home directory to the specified directory if it isn't there already and the old home exists. |
| `user_management_default_primary_group` | `str` | `false` | | | Custom default primary user group. Omitted if `null`. |
| `user_management_default_secondary_groups` | `list` | `false` | | `[]` | Custom default secondary user groups. Omitted if empty. |
| `user_management_default_secondary_groups_append` | `bool` | `false` | `false`, `true` | `false` | If `true`, add the user to the groups specified in `groups`. <br />If `false`, user will only be added to the groups specified <br />in `groups`, removing them from all other groups. |
| `user_management_default_shell` | `str` | `false` | | `None` | Default user's shell. Omitted if `null`. |
| `user_management_default_ssh_from` | `list` | `false` | | `['*']` | Default, global `from=""` value added to `authorized_keys` for each user having `user_management_users.ssh_public_keys` defined |
| `user_management_install_sudo` | `bool` | `false` | `false`, `true` | `true` | Installs `sudo` if set to `true`. |
| `user_management_manage_sudoers_groups` | `bool` | `false` | `false`, `true` | `false` | Enable or disable sudoers management for groups. |
| `user_management_manage_sudoers_users` | `bool` | `false` | `false`, `true` | `false` | Enable or disable sudoers management for users. |
| `user_management_sudoers_groups` | `list` | `false` | | `[]` | A list of sudoers configurations for groups. |
| `user_management_sudoers_groups.commands` | `list` | `false` | | `[]` | The commands allowed by the sudoers rule. <br />Multiple can be added by passing a list of commands. <br />Use `ALL` for all commands. |
| `user_management_sudoers_groups.group` | `str` | `false` | | | The name of the group for the sudoers rule. <br />This option cannot be used in conjunction with `user`. |
| `user_management_sudoers_groups.name` | `str` | `true` | | `user_management_mygroupname` | The name of the sudoers rule. |
| `user_management_sudoers_groups.nopassword` | `bool` | `false` | `false`, `true` | `false` | Whether a password will be required to run the `sudo`'d command. |
| `user_management_sudoers_groups.state` | `str` | `true` | `absent`, `present` | `present` | Whether the rule should exist or not. |
| `user_management_sudoers_users` | `list` | `false` | | `[]` | A list of sudoers configurations for users. |
| `user_management_sudoers_users.commands` | `list` | `false` | | `[]` | The commands allowed by the sudoers rule. <br />Multiple can be added by passing a list of commands. <br />Use `ALL` for all commands. |
| `user_management_sudoers_users.name` | `str` | `true` | | `user_management_john.doe` | The name of the sudoers rule. |
| `user_management_sudoers_users.nopassword` | `bool` | `false` | `false`, `true` | `false` | Whether a password will be required to run the `sudo`'d command. |
| `user_management_sudoers_users.state` | `str` | `true` | `absent`, `present` | `present` | Whether the rule should exist or not. |
| `user_management_sudoers_users.user` | `str` | `false` | | | The name of the user for the sudoers rule. <br />This option cannot be used in conjunction with `group`. |
| `user_management_users` | `list` | `false` | | `[]` | List of users to be managed. |
| `user_management_users.absolute_home_path` | `str` | `false` | | | Custom `$HOME` root path. Must be specified as absolute path. |
| `user_management_users.custom_ssh_from` | `list` | `false` | | `[]` | `from=""` value added to `authorized_keys` if user has `user_management_users.ssh_public_keys` defined. <br />If `user_management_default_ssh_from` or `custom_ssh_from` is defined and not set to `'*'`, all values will be concatenated. |
| `user_management_users.gecos` | `str` | `false` | | `None` | Optionally sets the description (aka GECOS) of user account: <br />Full Name, Room Number, Work Phone, Home Phone, Other |
| `user_management_users.groups_append` | `bool` | `false` | `false`, `true` | `false` | If `true`, add the user to the groups specified in groups. <br />If `false`, user will only be added to the groups specified in `secondary_groups`, removing them from all other groups. |
| `user_management_users.home_create` | `bool` | `false` | `false`, `true` | `true` | Unless set to false, a home directory will be created for the user when the account is created or if the home directory does not exist. |
| `user_management_users.home_move` | `bool` | `false` | `false`, `true` | `false` | If set to `true` when used with `home:`, attempt to move the user's old home directory to the specified directory if it isn't already there and the old home exists. |
| `user_management_users.name` | `str` | `true` | | `user_management_john.doe` | User's Linux login name. |
| `user_management_users.password` | `str` | `false` | | `None` | If provided, set the user's password to the provided encrypted hash password. To create an account with a locked/disabled password, set this to `!` or `*`. <br />How to generate encrypted passwords: <br />[Ansible Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module) |
| `user_management_users.primary_group` | `str` | `false` | | `user_management_users.name` | Optionally sets the user's primary group (takes a group name). |
| `user_management_users.secondary_groups` | `list` | `false` | | `[]` | List of groups user will be added to. <br />By default, the user is removed from all other groups. <br />Configure `groups_append` to modify this. <br />When set to an empty string `''`, the user is removed from all groups except the primary group. |
| `user_management_users.shell` | `str` | `false` | | `user_management_default_shell` | Overwrites 'user_management_default_shell'. |
| `user_management_users.ssh_public_keys` | `list` | `false` | | `[]` | The SSH public key(s), as a list or (since Ansible 1.9) url. |
| `user_management_users.state` | `str` | `true` | `absent`, `present` | `present` | Whether the account should exist or not, taking action if the state is different from what is stated. |
| `user_management_users.userdel_force` | `bool` | `false` | `false`, `true` | `false` | This only affects `state=absent`. <br />It forces removal of the user and associated directories on supported platforms. |
| `user_management_users.userdel_remove` | `bool` | `false` | `false`, `true` | `false` | This only affects `state=absent`. <br />It attempts to remove directories associated with the user. |

manage_authorized_keys
---

| Variable | Type | Required | Choices | Default | Description |
| --- | --- | --- | --- | --- | --- |
| `item` | `list` | `false` | | `[]` | List of users to be managed. |
| `item.custom_ssh_from` | `list` | `false` | | `[]` | `from=""` value added to `authorized_keys` if user has `user_management_users.ssh_public_keys` defined. <br />If `user_management_default_ssh_from` or `custom_ssh_from` is defined and not set to `'*'`, all values will be concatenated. |
| `item.name` | `str` | `true` | | `user_management_john.doe` | User's Linux login name. |
| `item.ssh_public_keys` | `list` | `false` | | | A list of the SSH public key(s), as a string or (since Ansible 1.9) url. |
| `item.state` | `str` | `true` | `absent`, `present` | `present` | Whether the account should exist or not, taking action if the state is different from what is stated. |



Dependencies
---

None

Example Playbook
---

```yaml
- name: "Play | user_management"
  hosts: all
  roles:
    - role: user_management
```

License
---

BSD, MIT

Author Information
---

Xenion1987 @ Access-InTech