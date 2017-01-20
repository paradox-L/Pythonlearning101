#reduce grammar format: reduce(function, iterable[, initializer])

sum = reduce((lambda x, y: x + y), range(1, 101))
print sum
