---
source_hash: e824c11ff4ae
---

# Engine Configuration Tool
### Kirikiri Z no longer has a separate engine configuration tool.  
Launching the engine with -userconf starts it as the user-facing engine configuration tool (the settings screen opens in a browser; see [Kirikiri Configuration](../../guide/Configure.md)).  
If your installer registers a shortcut that adds -userconf to the engine's arguments as the engine configuration tool, it works the same way as before.

### No developer engine configuration tool is provided.
To hide an item from the user settings, set "user":false for it in option\_desc\_ja.json, or remove the item altogether.  
If the settings do not show up correctly, the log may report a JSON syntax error, so launch from a console and check the log.  
To apply these changes, you need to rebuild the core or use a tool that can modify resources.  

See also [Adding/Editing Engine Settings](../core/engine_setting.md).
