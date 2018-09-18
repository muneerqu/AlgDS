#
# Additional loops
# continue Shorten the loop and start again as if it reach the end of the loop block
# break exit the loop prematurely
# else execute of loop ends normally

secret = 'abc.123'
pw = ''
auth = False
count = 0
max_attempts = 7

while pw != secret:
    count += 1
    if count > max_attempts: break
    if count == 3: continue
    pw = input(f'{count}: What is your password: ')
    if count > max_attempts: break
else:
    auth = True
print('Success .. now exiting ...' if auth else ', this auction has been reported ... exiting ...')
