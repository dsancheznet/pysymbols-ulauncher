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
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)
#My screen can only cope with a selection of 12 items max, so keep that in mind then defining lists.
mySymbols = {
    '-->': [ '↣', '↦', '⇀', '⇁', '⇉', '⇛', '⇝', '⇢', '⇥', '⇨', '➡', '⟶'],
    '<--': [ '↢', '↤', '↼', '↽', '⇇', '⇚', '⇜', '⇠', '⇤', '⇦', '⬅', '⟵' ],
    '<->': [ '⇹', '⇼', '⥎', '⥐', '↹', '⇋', '⇌', '⇄', '⬌', '⟷' ],
    'UP>': [ '↥', '↾', '↿', '⇈', '⇞', '⇡', '⇧', '⥣', '⤊', '⟰', '⬆' ],
    'DN>': [ '↧', '⇂', '⇃', '⇊', '⇟', '⇣', '⇩', '⥥', '⤋', '⟱', '⬇' ],
    'CHECK': [ '✓', '✔', '☑', '✗', '✘', '☒'],
    'FRAC': [ '½', '⅓', '⅔', '¼', '¾' , '⅛', '⅜', '⅝', '⅞', '‰', '‱'],
    'HEART' : [ '💗', '💓', '💔', '💟', '💕', '💖', '💘', '💝', '💞' ],
    'MATH' : [ 'π', '∞', 'Σ', '÷', '±'  ],
    'SUBNUM' : [ '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉' ],
    'SUPNUM' : [ '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹' ],
    'MAC': [ '⌘', '⌃', '⌥', '⇧', '⇪', '⌫', '⏏', '⎋', '␣', '↩']

}

class SymbolExtension(Extension):

    def __init__(self):
        super(SymbolExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        tmpSymbols = []
        if event.get_argument() in mySymbols:
            tmpKey = event.get_argument().upper()
            for tmpMatch in mySymbols[tmpKey]:
                tmpSymbols.append(
                    ExtensionResultItem(icon='images/icon.png',
                                        name=tmpMatch,
                                        description='Copy ' + tmpMatch + ' to clipboard', on_enter=CopyToClipboardAction(tmpMatch)))
        else:
            if event.get_argument() != None:
                logger.debug( "["+event.get_argument()+"] not found ")
        return RenderResultListAction(tmpSymbols)

if __name__ == '__main__':
    SymbolExtension().run()
