import mks

while True:
    text = input('mks> ')
    if text == 'e': break
    result, error = mks.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)