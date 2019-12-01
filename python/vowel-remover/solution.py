def shortcut( s ):
  vowels = ('a','e','i','o','u')
  return ''.join([x for x in s if x not in vowels])