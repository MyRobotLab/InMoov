def to_bytestring (s):
  if s:
    if isinstance(s, str):
      return s
    else:
      return s.encode('utf-8')