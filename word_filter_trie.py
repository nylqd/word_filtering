class Node(object):
    def __init__(self):
        self.value = None
        self.children = {}


class Trie:
    def __init__(self, list_words):
        self.root = Node()
        for word in list_words:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                child = Node()
                node.children[word[i]] = child
            node = node.children[word[i]]

        node.value = word

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return None
            else:
                node = node.children[word[i]]

        return node.value

    def is_contain(self, message):
        len_msg = len(message)
        for i in range(len_msg):
            parent = self.root
            index = i
            while index < len_msg and parent.children is not None and message[index] in parent.children:
                parent = parent.children[message[index]]
                if parent.value is not None:
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
                parent = parent.children[message[index]]
                if parent.value is not None:
                    msg_new.append(u'*' * (index - i + 1))
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
        if node.value is not None:
            print(ind, ':', node.value)
        else:
            for key in node.children.keys():
                print(ind, '{', key)
                self.display_node(node.children[key], indent + 1)
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

    trie = Trie(words_list)

    trie.display()
    # if message contains words need to filter
    print(trie.is_contain(msg))
    # message after filtering
    print(trie.filter(msg))

    # test case in english
    trie.add_word('test')
    trie.add_word('case')
    msg_en = 'test case in english'

    trie.display()
    print(trie.is_contain(msg_en))
    print(trie.filter(msg_en))
