import metaknowledge as mk

RC = mk.RecordCollection('.')
for i, R in enumerate(RC, start = 1):
    print('Working on Record number: {}'.format(i), end = '\r')
    with open("imetrics_tm/{}-{}.txt".format(R.id[:3],R.id[4:]), 'w') as f:
        f.write(R.get('AB', ''))
print('\nDone')