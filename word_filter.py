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
            if node.children is None or word[i] not in node.children:
                node.children = {word[i]: (Node(), i == index_end)}
            else:
                if i == index_end:
                    node.children[word[i]] = (node.children[word[i]], True)

            node = node.children[word[i]][0]

    def is_contain(self, message):
        root = self.root
        len_msg = len(message)
        for i in range(len_msg):
            parent = root
            index = i
            while index < len_msg and parent.children is not None and message[index] in parent.children:
                (parent, flag_end) = parent.children[message[index]]
                if flag_end:
                    return True
                index += 1
        return False

    def filter(self, message):
        msg_new = []
        root = self.root
        len_msg = len(message)
        i = 0
        flag_continue = False
        while i < len_msg:
            parent = root
            index = i
            while index < len_msg and parent.children is not None and message[index] in parent.children:
                (parent, flag_end) = parent.children[message[index]]
                if flag_end:
                    # print(sMsg[i:j + 1])
                    msg_new.append(u'*' * (index - i + 1))  # 关键字替换
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


if __name__ == '__main__':
    dfa = Dfa(('吓得', '女儿', '派出所'))
    dfa.add_word('乱咬')
    msg = '四处乱咬乱吠，吓得家中 11 岁的女儿躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死'
    print(dfa.filter(msg))
    print(dfa.is_contain(msg))
