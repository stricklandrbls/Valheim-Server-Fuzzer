
session_id_server = bytearray([0xde, 0x78, 0x51, 0xc0])
session_id_client = bytearray([0x0a, 0x0b, 0xd8, 0x72])

def build_connect_package():
  c = bytearray([0x20])
  c_filler = bytearray([0x10, 0x00, 0x0d])
  package = c + c_filler + session_id_server
  package += bytearray([0x19, 0x24, 0x66, 0x1c, 0x82, 0xba, 0x02, 0x0, 0x0, 0x20, 0x0b])

  while len(package) < 512:
      package += (bytearray([0x00]))
  print(package.hex())
  return bytes(package)

def build_steamid_package(header_msb=bytes, header_lsb=bytes):
  msg = bytes.fromhex('22')
  msg += header_msb + header_lsb

  data_str = 'fff203050100100122af01226208011220a340ae65bc62e2c9e498d0847beb5b771fd8755df9cc701d4d642d2bc8a9797c21fff203050100100145497890644d491b936450aac0365a0a8101fff20305010010016219737465616d69643a3736353631313938303434343130363233291b39aaf5cf5083b632404f0cd57fbf498f725dd2a7eb4ed1185f4a3ce2ebda3d6b7c259df536156545c1181a6d616f4acf95014a15817e5132a0655d1ba8ee61e1c0bde17a41a0974d0329f5bf3f80ba02000030013a750a3108011220b91fffea8a1a469101de1b9023ccdeebc2b423afef30c9ab75bcd24486ade03a19892e783741b7d629200b28021240d08d945bcc9723b7031c88118ce817c243fa2c916f50bab1b864700a104c86bfca7404e66edd46757b5e94a72b1bc34eb595813a7b5230a1839d3a4581815403'
  ret = msg + bytes.fromhex(data_str)
  print(ret.hex())
  return ret

def capture_header(data=bytes):
  lhs = data[1:8]
  rhs = data[8:16]
  print("Header: [", lhs.hex(), "] [", rhs.hex(), "]")
  return lhs, rhs