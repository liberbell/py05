import sys

print('Number of arguments: ', len(sys.argv), ' arguments.')
print('Arguments ', sys.argv)

sys.argv.remove(sys.argv[0])
print('Arguments ', sys.argv)
