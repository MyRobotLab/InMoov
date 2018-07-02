def print_supported_languages ():
  codes = []
  for k,v in supported_languages.items():
    codes.append('\t'.join([k, '=', v]))
  return '\n'.join(codes)