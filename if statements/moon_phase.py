# Write code below 💖

def moon_phase(phase):
  if phase == 'New Moon':
    print('🌑')
  elif phase == 'Waxing Crescent':
    print('🌒')
  elif phase == 'First Quarter':
    print('🌓')
  elif phase == 'Waxing Gibbous':
    print('🌔')
  elif phase == 'Full Moon':
    print('🌕')
  elif phase == 'Waning Gibbous':
    print('🌖')
  elif phase == 'Last Quarter':
    print('🌗')
  elif phase == 'Waning Crescent':
    print('🌘')
  else:
    print('Invalid moon phase')
  return(phase)
answer = moon_phase('New Moon')
print(answer)
  