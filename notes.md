# Valheim Server Fuzzer Notes

## Message Segment Dissection

### Messages 0 - 4

|Byte #|Byte Sequence|Possible Variable|Notes|
|---|---|---:|:---|
|<code>[-]</code>|`0x`| | |
|<code>[0]</code>|`0x2<0-3>` or `0x80`|`msgId` or `msgTypeId`|Iterates from `0x20` to `0x23` per conversation message. Messages after initial communication have `0x80` as this byte. This may indicate a message type identifier?|
|<code>[1:7]</code>|`0x0d 23 2d 87 90 11`| ? |This sequence only appears in the first 4 messages. Msg 0 only contains `0x0d 23 2d 87 90` in bytes `[3:7]` |
|<code>[8:15]</code>|Varies per connection| `ConnId` | Only appears to need to be echo'd into output Msg 4 in bytes `[8:15]`. |
|<code>-</code>|`0xff f2 03 05`| ? |Repeated 3 times in output Msg 4 bytes `[16:19]`,`[66:69]`,`[92:95]`.|
af 01 22 62 08 01 12 20