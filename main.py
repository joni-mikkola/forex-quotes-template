import asyncio
import logging
import quickfix
import quickfix44 as fix44

from model.event import Event, EventType
from client import QuoteClient
from helpers.fixhelper import FixHelper

from model.logger import setup_logger
__SOH__ = chr(1)
setup_logger('logfix', './_logs/quote_message.log')
logfix = logging.getLogger('logfix')


class FixApp(quickfix.Application):
    def __init__(self, config):
        super().__init__()

        self.settings = quickfix.SessionSettings(config)
        self.storefactory = quickfix.FileStoreFactory(self.settings)
        self.logfactory = quickfix.FileLogFactory(self.settings)
        self.initiator = quickfix.SocketInitiator(
            self, self.storefactory, self.settings, self.logfactory)

        self.initiator.start()

    def onCreate(self, sessionID):
        print("onCreate : Session (%s)" % sessionID.toString())

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("Successful Logon to session '%s'." % sessionID.toString())
        asyncio.run_coroutine_threadsafe(queue.put(Event(EventType.LOGIN)), loop)

    def onLogout(self, sessionID):
        print("Session (%s) logout !" % sessionID.toString())

    def toAdmin(self, message, sessionID):
        print("toAdmin")

    def fromAdmin(self, message, sessionID):
        print("fromAdmin")

    def toApp(self, message, sessionID):
        print("toApp")

    def fromApp(self, message, sessionID):
        print("fromApp")


# client = QuoteClient()
queue = asyncio.Queue()
loop = None


async def update():
    while True:
        event: Event = await queue.get()
        if event.type == EventType.LOGIN:
            print("successful login")
            # client.quote(fixApp.sessionID, '1')
        elif event.type == EventType.QUOTE:
            print(f"quote {event.value}")

if __name__ == '__main__':
    fixApp = FixApp('client.cfg')

    loop = asyncio.new_event_loop()
    loop.run_until_complete(update())
    loop.close()
