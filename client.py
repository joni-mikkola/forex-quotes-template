import quickfix as fix
import quickfix44 as fix44


class QuoteClient():
    def quote(self, session_id, symbol):
        message = fix.Message()
        message.getHeader().setField(fix.BeginString(fix.BeginString_FIX44))
        message.getHeader().setField(fix.MsgType(fix.MsgType_MarketDataRequest))

        message.setField(fix.MDReqID('1'))
        message.setField(fix.SubscriptionRequestType(
            fix.SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES))
        message.setField(fix.MarketDepth(1))
        message.setField(fix.NoMDEntryTypes(2))
        message.setField(fix.MDUpdateType(
            fix.MDUpdateType_INCREMENTAL_REFRESH))

        group = fix44.MarketDataRequest().NoMDEntryTypes()
        group.setField(fix.MDEntryType(fix.MDEntryType_BID))
        message.addGroup(group)
        group.setField(fix.MDEntryType(fix.MDEntryType_OFFER))
        message.addGroup(group)
        new_pairs = [symbol]
        message.setField(fix.NoRelatedSym(len(new_pairs)))

        requestSymbol = fix44.MarketDataRequest().NoRelatedSym()
        for pair in new_pairs:
            requestSymbol.setField(fix.Symbol(pair))
            message.addGroup(requestSymbol)
        fix.Session.sendToTarget(message, session_id)
