import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

mySymbols = {
    '--->': [ '↣', '↦', '⇀', '⇁', '⇉', '⇛', '⇝', '⇢', '⇥', '⇨', '➡', '⟶'],
    '<---': [ '↢', '↤', '↼', '↽', '⇇', '⇚', '⇜', '⇠', '⇤', '⇦', '⬅', '⟵' ],
    '<-->': [ '⇹', '⇼', '⥎', '⥐', '↹', '⇋', '⇌', '⇄', '⬌', '⟷' ],
    '<UP>': [ '↥', '↾', '↿', '⇈', '⇞', '⇡', '⇧', '⥣', '⤊', '⟰', '⬆' ],
    '<DN>': [ '↧', '⇂', '⇃', '⇊', '⇟', '⇣', '⇩', '⥥', '⤋', '⟱', '⬇' ],
    'CHCK': [ '✓', '✔', '☑', '✗', '✘', '☒'],
    'FRAC': [ '½', '⅓', '⅔', '¼', '¾' , '⅛', '⅜', '⅝', '⅞', '‰', '‱']
    'MACK': [ '⌘', '⌃', '⌥', '⇧', '⇪', '⌫', '⏏', '⎋', '␣' '↩']
}

class SymbolExtension(Extension):

    def __init__(self):
        super(SymbolExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        tmpSymbols = []
        if event.get_argument() in mySymbols:
            for tmpMatch in in mySymbols:
                tmpSymbols.append(ExtensionResultItem(icon='images/icon.png', name=tmpMatch, description='Copy ' + tmpMatch + ' to clipboard', on_enter=CopyToClipboardAction(tmpMatch))))
        return RenderResultListAction(tmpSymbols)

if __name__ == '__main__':
    SymbolExtension().run()
