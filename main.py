# import json
import logging
# from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction

logger = logging.getLogger(__name__)

#My screen can only cope with a selection of 12 items max, so keep you screen size in mind when defining lists.

mySymbols = {
    '-->'   : [ '↦', '⇀', '⇁', '⇉', '⇛', '⇝', '⇢', '⇥', '⇨', '➡', '⟶'],
    '<--'   : [ '↤', '↼', '↽', '⇇', '⇚', '⇜', '⇠', '⇤', '⇦', '⬅', '⟵' ],
    '<->'   : [ '⇹', '⇼', '⥎', '⥐', '⇋', '⇌', '⇄', '↹', '⬌', '⟷' ],
    'UP>'   : [ '↥', '↾', '↿', '⇈', '⇞', '⇡', '⇧', '⥣', '⤊', '⟰', '⬆' ],
    'DN>'   : [ '↧', '⇂', '⇃', '⇊', '⇟', '⇣', '⇩', '⥥', '⤋', '⟱', '⬇' ],
    'O>'    : [ '⮊', '⮈', '⮉', '⮋', '⭮', '⭯', '⮌', '⮎', '⮍', '⮏' ],
    'CHECK' : [ '✓', '✔', '☑', '✗', '✘', '☒'],
    'FRAC'  : [ '½', '⅓', '⅔', '¼', '¾' , '⅛', '⅜', '⅝', '⅞', '‰', '‱'],
    'HEART' : [ '💗', '💓', '💔', '💟', '💕', '💖', '💘', '💝', '💞' ],
    'MATH'  : [ 'π', '∞', 'Σ', '÷', '±', 'Ω', 'μ', 'λ', 'ρ' ],
    'SUBNUM': [ '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉' ],
    'SUPNUM': [ '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹' ],
    'SEX'   : [ '♂', '♀', '⚥', '⚤', '⚣', '⚢', '☿' ],
    'MEDIA' : [ '◀️', '⏪', '⏮️', '⏭️', '⏩', '▶️', '⏸️', '⏯️', '⏺️', '⏹️', '⏏️' ],
    'ZODIAC': [ '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓' ],
    'ROMAN' : [ 'Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', 'Ⅼ', 'Ⅽ', 'Ⅾ', 'Ⅿ' ],
    'TRADE' : [ '©', '®', '℗', '™', '℠', '㋏' ],
    'MAC'   : [ '⌘', '⌃', '⌥', '⇧', '⇪', '⌫', '⏏', '⎋', '␣', '↩']
}
#'' : [ '', '' ],

class SymbolExtension(Extension):

    def __init__(self):
        super(SymbolExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        tmpSymbols = []
        tmpKey = event.get_argument()
        if tmpKey == None:
            return RenderResultListAction([ExtensionResultItem(icon='images/icon.png', name='Please specify the desired symbol set', on_enter=DoNothingAction())])
        elif tmpKey.upper() in mySymbols:
            for tmpMatch in mySymbols[tmpKey.upper()]:
                tmpSymbols.append(
                    ExtensionResultItem(icon='images/icon.png',
                                        name=tmpMatch,
                                        description='Copy ' + tmpMatch + ' to clipboard', on_enter=CopyToClipboardAction(tmpMatch)))
            return RenderResultListAction(tmpSymbols)
        else:
            return RenderResultListAction([ExtensionResultItem(icon='images/icon.png', name='Unknown code...', on_enter=DoNothingAction())])


if __name__ == '__main__':
    SymbolExtension().run()
