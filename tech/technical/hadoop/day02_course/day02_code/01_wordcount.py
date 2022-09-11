from mrjob.job import MRJob

class WordCount(MRJob):
    """重写mapper()和reducer()两个方法"""
    def mapper(self, _, line):
        # _: 每行行首的偏移量,一般不用
        # line: 每行具体的内容
        for word in line.split():
            yield word, 1

    # shuffle & sort过程(我们看不见)
    # are 1
    # how 1 1
    # what 1
    # twink 1 1 1
    def reducer(self, key, values):
        # key: map&shuffle&sort之后的word
        # values:map&shuffle&sort之后的序列
        yield key,sum(values)

if __name__ == '__main__':
    WordCount.run()




















