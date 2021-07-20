from config.log import logger


if __name__ == "__main__":
    logger.info("Okay Info")


    def custom_sink(message):
        return {
            "message": message
        }

    logger.add(custom_sink, serialize=True)
    logger.info("custom sink")
