#cb 252.A
pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string  = "Grizzly_Adams@Sasquatch.com"
match = re.match(pattern, search_string)

if match:
  domain = match.groups()[0]
  print(domain)
