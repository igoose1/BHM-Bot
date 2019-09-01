from models import Post, Admin


order = (
    'photos',
    'name',
    'year',
    'regisseur',
    'overview',
    'conclusion'
)


def new(bot, update):
    post = Post(
        Post.author.telegram_id == update.message.from_chat.id
    )
    post.author.state = 'conf' + order[0]
    post.save()
    fill(bot, update)


def fill(bot, update):
    post = Post.get(
        Post.author.telegram_id == update.message.from_chat.id
    )
    now_ind = order.index(post.author.state[len('conf'):])
    next_ind = now_ind + 1
    post.author.state = None if next_ind >= len(order) else order[next_ind]

    if post.author.state is not None:
        attr = getattr(post, order[now_ind])
        attr = update.message.text
        update.message.reply(
            'Fill {field_name} field'.format(
                field_name=order[next_ind]
            )
        )
    else:
        update.message.reply(
            'Success!'
        )

    post.save()
