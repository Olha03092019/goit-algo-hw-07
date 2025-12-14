# Кожен об’єкт Comment є вузлом дерева
class Comment:
    def __init__(self, text,author):
        self.text = text
        self.author = author
        # список replies містить дочірні вузли
        self.replies = []
        self.is_deleted = False

    def add_reply(self,text):
        self.replies.append(text)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level

        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)

if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)
    reply1.remove_reply()
    reply2_1 = Comment("Захоплюючий сюжет та персонажі, за яких хочеться вболівати", "Бодя")
    reply2.add_reply(reply2_1)
    reply1_2 = Comment("Можливо це просто не ваша книга", "Бодя")
    reply1.add_reply(reply1_2)
    root_comment.display()
