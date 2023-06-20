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

### Data Messages
<details><summary><b>Header</b></summary>

|Byte #|Byte Sequence|Possible Variable|Notes|
|---|---|---:|:---|
|<code>[0]</code>|`0x80`|`msgTypeId = DATA`| Seems to be an ID for all 'data' messages. |
|<code>[1:4]</code> (**SERVER**)|`0xde 78 51 c0`| ? | Also appears as part of the header in Messages 0-4, following `0x2_ 0d`.|
|<code>[1:4]</code> (**CLIENT**)|`0x0a 0b d8 72`| ? | Part of the response for server 'data' messages. |
|<code>[5]</code>|`0x<02-FF>`| `_count` | Counting for something. This seems to be a sub count for bit `[6]`|
|<code>[6]</code>|`0x<00-??>`| `_count` | Counting for something. This seems to be a super count for bit `[5]`|


</details>