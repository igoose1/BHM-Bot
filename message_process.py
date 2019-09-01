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
    post.author.state = 'conf'
    post.save()
    fill(bot, update)


def fill(bot, update):
    post = Post.get(
        Post.author.telegram_id == update.message.from_chat.id
    )
    now_ind = -1
    if post.author.state != 'conf':
        now_ind = order.index(post.author.state[len('conf'):])
        setattr(post, order[now_ind], update.message.text)
    next_ind = now_ind + 1
    post.author.state = None if next_ind >= len(order) else 'conf' + {order[next_ind]}

    if post.author.state is not None:
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
