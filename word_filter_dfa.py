class Node(object):
    def __init__(self):
        self.children = None


class Dfa(object):
    def __init__(self, list_words):
        self.root = None
        self.root = Node()
        for word in list_words:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        index_end = len(word) - 1
        for i in range(len(word)):
            if node.children is None:
                # init with type dict {word[i]:end_mark, ...}
                node.children = {word[i]: (Node(), i == index_end)}
            elif word[i] not in node.children:
                node.children[word[i]] = (Node(), i == index_end)
            else:
                if i == index_end:
                    node.children[word[i]] = (node.children[word[i]], True)

            node = node.children[word[i]][0]

    def is_contain(self, message):
        len_msg = len(message)
        for i in range(len_msg):
            parent = self.root
            index = i
            while index < len_msg and parent.children is not None and message[index] in parent.children:
                (parent, flag_end) = parent.children[message[index]]
                if flag_end:
                    return True
                index += 1
        return False

    def filter(self, message):
        msg_new = []
        len_msg = len(message)
        i = 0
        flag_continue = False
        while i < len_msg:
            parent = self.root
            index = i
            while index < len_msg and parent.children is not None and message[index] in parent.children:
                (parent, flag_end) = parent.children[message[index]]
                if flag_end:
                    # print(sMsg[i:j + 1])
                    msg_new.append(u'*' * (index - i + 1))  # replace word with *
                    i = index + 1
                    flag_continue = True
                    break
                index += 1
            if flag_continue:
                flag_continue = False
                continue
            msg_new.append(message[i])
            i += 1
        return ''.join(msg_new)

    def display_node(self, node, indent):
        ind = '\t' * indent
        if node.children is not None:
            for key in node.children:
                print(ind, '{', key, ':', node.children[key][1])
                self.display_node(node.children[key][0], indent + 1)
                print(ind, '}')
        return

    def display(self):
        print('{')
        self.display_node(self.root, 0)
        print('}')


if __name__ == '__main__':
    # test case in chinese
    words_list = ('敏感词', '用例')
    msg = '敏感词过滤测试用例'

    dfa = Dfa(words_list)
    # if message contains words need to filter
    print(dfa.is_contain(msg))
    # message after filtering
    print(dfa.filter(msg))

    # test case in english
    dfa.add_word('test')
    dfa.add_word('tea')
    dfa.add_word('case')
    msg_en = 'test case in english'

    dfa.display()

    print(dfa.is_contain(msg_en))
    print(dfa.filter(msg_en))
