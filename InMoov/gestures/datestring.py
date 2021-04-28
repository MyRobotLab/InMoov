def datestring (display_format="%a, %d %b %Y %H:%M:%S", datetime_object=None):
  if datetime_object is None:
    datetime_object = datetime.utcnow()
  return datetime.strftime(datetime_object, display_format)