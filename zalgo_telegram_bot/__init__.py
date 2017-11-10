# encoding: utf-8

import logging
from uuid import uuid4

from zalgo.zalgo import zalgo

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, MessageHandler, Filters


__title__ = 'zalgo-telegram-bot'
__version__ = '0.1.0'
__license__ = 'GPLv3'


logger = logging.getLogger(__title__)


def on_message(bot, update):
    zalgo_text = zalgo(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=zalgo_text)


def on_inlinequery(bot, update):
    query = update.inline_query.query

    logger.info(query)

    if not query:
        return

    zalgo_text = zalgo(query)

    result = [
        InlineQueryResultArticle(
            id=uuid4(),
            title=query,
            description=zalgo_text,
            input_message_content=InputTextMessageContent(zalgo_text),
        )
    ]
    update.inline_query.answer(result, cache_time=0)


def on_error(bot, update, error):
    logger.warn("Update {} caused error {}".format(update, error))


def main():
    from argparse import ArgumentParser
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

    parser = ArgumentParser()
    parser.add_argument("token")

    args = parser.parse_args()

    updater = Updater(token=args.token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, on_message))
    dispatcher.add_handler(InlineQueryHandler(on_inlinequery))
    dispatcher.add_error_handler(on_error)

    logger.info("Starting")
    updater.start_polling()
    updater.idle()
    logger.info("Terminating")


if __name__ == '__main__':
    main()
