# Architecture

```
bootstrap -> session -> engine -> writers (registry / disk / mac)
                     \-> snapshot_manager
bootstrap -> ipc.dispatcher -> session
renderer (pywebview) -> preload.bridge -> ipc.dispatcher
native_bridge.clr_loader -> src-native (C# helper)
```

Adapters describe *which* HWID sources a game touches. Writers describe
*how* to read/write each source. The engine glues the two together and
always goes through a snapshot first.
</