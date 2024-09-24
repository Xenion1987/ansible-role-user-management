# Role: `user-management`

Manage users and their SSH public key enrollment via Ansible.

- [Role: `user-management`](#role-user-management)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
    - [User variables](#user-variables)
    - [`authorized_keys` variables](#authorized_keys-variables)
      - [`**/host_vars/*`](#host_vars)
    - [`sudoers` variables](#sudoers-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)

## Requirements

None

## Role Variables

### User variables

| Name                                       | Type   | Default                         | Description                                                                                                                                                                                                                            |
| ------------------------------------------ | ------ | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_management_default_primary_group`    | `str`  | `null`                          | Custom primary user group                                                                                                                                                                                                              |
| `user_management_default_secondary_groups` | `list` | `[]`                            | Custom secondary user groups                                                                                                                                                                                                           |
| `user_management_default_sudo_mode`        | `str`  |                                 | Installs `sudo` if set to `sudo`                                                                                                                                                                                                       |
| `user_management_default_shell`            | `str`  |                                 | Default user's shell                                                                                                                                                                                                                   |
| `user_management_default_home_root`        | `str`  |                                 | Custom `$HOME` root path                                                                                                                                                                                                               |
| `user_management_users`                    | `list` |                                 | List of users to be managed                                                                                                                                                                                                            |
| `user_management_users.absolute_home_path` | `str`  |                                 | Optionally set the user's home directory.                                                                                                                                                                                              |
| `user_management_users.groups_append`      | `bool` | `true`                          | If `true`, add the user to the groups specified in groups. If `false`, user will only be added to the groups specified in `secondary_groups`, removing them from all other groups.                                                     |
| `user_management_users.home_create`        | `bool` | `true`                          | Unless set to false, a home directory will be made for the user when the account is created or if the home directory does not exist.                                                                                                   |
| `user_management_users.home_move`          | `bool` | `false`                         | If set to `true` when used with `home:` , attempt to move the user's old home directory to the specified directory if it isn't there already and the old home exists.                                                                  |
| `user_management_users.name`               | `str`  |                                 | User's Linux login name.                                                                                                                                                                                                               |
| `user_management_users.primary_group`      | `str`  | `user_management_users.name`    | Optionally sets the user's primary group (takes a group name).                                                                                                                                                                         |
| `user_management_users.state`              | `str`  |                                 | User's state (`present` or `absent`).                                                                                                                                                                                                  |
| `user_management_users.secondary_groups`   | `list` | `user_management_users.name`    | List of groups user will be added to. By default, the user is removed from all other groups. Configure `groups_append` to modify this. When set to an empty string `''`, the user is removed from all groups except the primary group. |
| `user_management_users.shell`              | `str`  | `user_management_default_shell` | Optionally set the user's shell.                                                                                                                                                                                                       |
| `user_management_users.userdel_force`      | `bool` | `false`                         | This only affects `state=absent`, it forces removal of the user and associated directories on supported platforms.                                                                                                                     |
| `user_management_users.userdel_remove`     | `bool` | `false`                         | This only affects 'state=absent', it attempts to remove directories associated with the user.                                                                                                                                          |

### `authorized_keys` variables

| Name                                    | Type   | Default | Description                                                                                                                                                                                                                             |
| --------------------------------------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_management_users.custom_ssh_from` | `list` |         | `from=""` value added to `authorized_keys` if user has `{{user_management_users.ssh_public_key}}` defined. If `user_management_default_ssh_from` or `custom_ssh_from` is defined and not set to `'*'`, all values will be concatenated. |
| `user_management_users.ssh_public_key`  | `str`  | `''`    | The SSH public key(s), as a string or (since Ansible 1.9) url (e.g. `https://github.com/username.keys`)                                                                                                                                 |

#### `**/host_vars/*`

| Name              | Type   | Default | Description                                                                                                                                                                                                                                                            |
| ----------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_ssh_from` | `list` |         | `from=""` value added to `authorized_keys` for each user having `{{user_management_users.ssh_public_key}}` defined. If `user_management_default_ssh_from` or `user_management_users.custom_ssh_from` is defined and not set to `'*'`, all values will be concatenated. |

### `sudoers` variables

| Name                                        | Type   | Default | Description                                                                                                                        |
| ------------------------------------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `user_management_manage_sudoers_groups`     | `bool` | `false` | Enable or disable sudoers management for groups                                                                                    |
| `user_management_sudoers_groups`            | `list` | `[]`    | A list of sudoers configurations for users                                                                                         |
| `user_management_sudoers_groups.name`       | `str`  |         | The name of the sudoers rule                                                                                                       |
| `user_management_sudoers_groups.group`      | `str`  | `null`  | The name of the group for the sudoers rule. This option cannot be used in conjunction with `user`.                                 |
| `user_management_sudoers_groups.commands`   | `list` |         | The commands allowed by the sudoers rule. Multiple can be added by passing a list of commands. Use `ALL` for all commands.         |
| `user_management_sudoers_groups.nopassword` | `bool` | `false` | Whether a password will be required to run the `sudo`'d command                                                                    |
| `user_management_sudoers_groups.state`      | `str`  |         | Whether the rule should exist or not                                                                                               |
| `user_management_manage_sudoers_users`      | `bool` | `false` | Enable or disable sudoers management for users                                                                                     |
| `user_management_sudoers_users`             | `list` | `[]`    | A list of sudoers configurations for users                                                                                         |
| `user_management_sudoers_users.name`        | `str`  |         | The name of the sudoers rule                                                                                                       |
| `user_management_sudoers_users.user`        | `str`  | `null`  | The name of the user for the sudoers rule. This option cannot be used in conjunction with `group`.                                 |
| `user_management_sudoers_users.commands`    | `list` |         | The commands allowed by the sudoers rule. Multiple can be added by passing a list of commands. Use `ALL` for all commands.         |
| `user_management_sudoers_users.nopassword`  | `bool` | `false` | Whether a password will be required to run the `sudo`'d command                                                                    |
| `user_management_sudoers_users.state`       | `str`  |         | Whether the rule should exist or not                                                                                               |
| `user_management_default_ssh_from`          | `list` | `[]`    | Default, global `from=""` value added to `authorized_keys` for each user having `{{user_management_users.ssh_public_key}}` defined |


## Dependencies

```yaml
collections:
  - ansible.posix
  - community.general
dependencies: []
```

## Example Playbook

```yaml
---
- name: Play for managing linux users
  hosts: all
  become: true
  gather_facts: true

  # Requires role 'user-management' mentioned in 'requirements.yml'
  roles:
    - role: user-management
      vars:
        user_management_default_secondary_groups: [playground]
        user_management_users:
          - name: john.doe
            state: present
            ssh_public_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDW6k6qtP1YfJ7eOSN1zDf8C6lTJuV+ethOvEJwTKJrGoQrKKukVfedjUL+e7XMszVT57iiV8rC+syZsJ6wkwJR2ahOUlU9hACbRc+X5mmVROLKlO+NaxrbMzsTJXeCJK6Oo+05f2kSPqGfjV3CZSq4Xv5mUMhaDkGUg/rqG5BIdqFDwirqxbUbPOIYeosLT1tbgxHvOTwsUqulEZS5h8mOt1Hahi1ZrfUOyharJvpc5rzYk/hq1zwTXTNtArOLCaSbvY+o61BAsnQBzg6Z+Elyrox53kWW8c0MuG0iPfehqW20eE9xZVBQfwutLmMHMNeUD2UwLDfxnoVXIlgn5T4Z4F2uMyKWKl9IsoIuguizX98SuASEXg4wsAEf2MSCxwk7AGO3yCgqRsnm7sIEEdvxUIewcuZn1ZtN0c3UjcsqRnoXgBOXpynsRStdZTPTM+o1LGma+Wp8FkMH1ZnuQ+BrCQ1ENKcS4oeTcG91Ud9Yiu/qfWVU64RrYpz0JvHWoApdzM73Xro2Sz9BuQH5uSCIya8PNEqGdH1GRDxbDkv41+scWwq/5i5CSlWmNogU377tPld9hqJJA//eniErgKO/QSJKmaDDzFe+eQh6F2Kn/NUVKqbPHbDlkYAZGT37L5iCOG1By55wwnemz40GS2Wo+a4nViDJGhuFty+4yR8fWQ== ansible-playground_20231122_194549
        user_management_manage_sudoers_users: true
        user_management_sudoers_users:
          - name: 30-john.doe
            user: john.doe
            commands:
              - ALL
            nopassword: true
            state: present
        user_management_manage_sudoers_groups: true
        user_management_sudoers_groups:
          - name: 20-playground
            group: playground
            commands:
              - ALL
            nopassword: true
            state: present
```
