# Plugins

The Plugins class manages **plugins**. You cannot create objects of this class.

## Members

### Methods

- [link](#link)
- [unlink](#unlink)
- [getList](#getlist)
- [canLink](#canlink)

---

### link

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Plugin to link. |

**Description**

Links a plugin

Links (loads) the specified plugin into the Kirikiri engine.

---

### unlink

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Plugin to unlink. |

**Return value**

true if the plugin was unlinked, false otherwise

**Description**

Unlinks a plugin

Unlinks the specified plugin.

Some plugins refuse to be released (for example, while their objects are still in use). If the plugin refuses and unlinking fails, false is returned.

---

### getList

Method

**Return value**

Array containing the names of the linked plugins

**Description**

Gets the list

Gets the list of plugins. The returned array lists plugin names in the order they were linked.

---

### canLink

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | File name of the plugin to check. |

**Return value**

true if the plugin can be linked, false otherwise.

**Description**

Checks whether a plugin can be linked

Checks in advance whether the specified plugin file can be loaded (linked) by the engine.
It does not actually perform [Plugins.link](Plugins.md#link).

Returns false if the plugin is not in the automatic search path or cannot be linked
in the current environment.

**See also:** [Plugins.link](Plugins.md#link)

---
