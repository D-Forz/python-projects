import logging as log


log.basicConfig(level = log.INFO,
                format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt = '%I:%M:%S %p',
                handlers=[
                    log.FileHandler('info.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('message at lvl debug')
    log.info('message at lvl info')
    log.warning('message at lvl warning')
    log.error('message at lvl error')
    log.critical('message at lvl critical')