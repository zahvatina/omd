class CountVectorizer:
    '''
    Count vectorizer class
    '''
    def __init__(self):
        self.vocab = set()

    def fit_transform(self, texts: list) -> list:
        '''
        :param texts: list of strings
        :return: list of list
        '''
        texts = list(map(str.lower, texts))
        tokens = set(sum(map(lambda x: x.split(' '), texts), []))
        self.vocab = self.vocab.union(tokens)
        vecs = []
        for text in texts:
            vec_map = {token: 0 for token in self.vocab}
            for token in text.split(' '):
                vec_map[token] += 1
            vecs.append(list(vec_map.values()))
        return vecs

    def get_names(self) -> list:
        '''
        :return: list of strings
        '''
        return list(self.vocab)


if __name__ == '__main__':
    cv = CountVectorizer()
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    count_matrix = cv.fit_transform(corpus)
    print(count_matrix)
    print(cv.get_names())
