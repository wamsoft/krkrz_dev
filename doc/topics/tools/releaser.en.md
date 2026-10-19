---
source_hash: 02f7b509b370
---

# Releaser

Kirikiri Z distributions are built with the [standard tools](../../guide/Tools.md).

- Create xp3 archives with the [xp3 archive tool (krkrxp3)](../../guide/Xp3Tool.md). It produces archives in the same format as the Kirikiri 2 Releaser
- Build the distributable executable (embedding command-line options, icon and version information, attaching the xp3, and signing) with the [releaser (krkrrelease)](../../guide/Releaser.md) (Windows only)
- Attaching an xp3 archive to the engine executable also works in Kirikiri Z (the Windows build, and the SDL build on Windows / Linux)

## Replacing the icon
The icon and version information can be replaced with the [releaser](../../guide/Releaser.md).
If you replace them with a general-purpose resource editor, do it **before** attaching the xp3 and signing (replacing them afterward loses the attached xp3 and invalidates the signature).
