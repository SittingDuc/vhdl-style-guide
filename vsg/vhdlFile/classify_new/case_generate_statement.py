
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import case_generate_statement as token

from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import case_generate_alternative

'''
    case_generate_statement ::=
        *generate*_label :
            case expression generate
                case_generate_alternative
                { case_generate_alternative }
            end generate [ *generate*_label ] ;
'''


def detect(iObject, lObjects):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lObjects[iIndex-1].get_value().lower() == 'case':
                return classify(iObject, lObjects)
    except IndexError:
        return iObject
    return iObject


def classify(iObject, lObjects):

    iToken = utils.tokenize_label(iObject, lObjects, token.generate_label, token.label_colon)

    iToken = utils.find_next_token(iToken, lObjects)
    utils.classify_token('case', token.case_keyword, iToken, lObjects)
    iToken += 1

    iToken = utils.classify_subelement_until('generate', expression, iToken, lObjects)

    utils.classify_token('generate', token.generate_keyword, iToken, lObjects)
    iToken += 1

    iToken = utils.detect_submodule(iToken, lObjects, case_generate_alternative)

    ### Classify the closing keywords
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('generate', token.end_generate_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_generate_label)

    return iToken