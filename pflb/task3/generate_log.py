import datetime
import random
import os


filename = 'log.log'

date = datetime.datetime.now()

with open(filename, 'a', encoding='utf8') as f:
    f.write('META DATA:\n')
    vol = random.randint(1, 1000)
    f.write('{}\n'.format(vol))
    f.write('{}\n'.format(random.randint(1, vol//4)))
    while os.stat(filename).st_size < 1048576:
        f.write('{}Z – [username{}] - wanna {} {}l\n'.format(
            date.isoformat(),
            random.randint(1, 100),
            random.choice(('top up', 'scoop')),
            random.randint(1, vol)
        ))
        date += datetime.timedelta(0, random.randint(0, 1800))

