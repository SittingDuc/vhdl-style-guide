

#from vsg.vhdlFile.classify_new import process_declarative_item

'''
    package_declarative_item ::=
        subprogram_declaration
      | subprogram_instantiation_declaration
      | package_declaration
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | signal_declaration
      | variable_declaration
      | file_declaration
      | alias_declaration
      | component_declaration
      | attribute_declaration
      | attribute_specification
      | disconnection_specification
      | use_clause
      | group_template_declaration
      | group_declaration
      | PSL_Property_Declaration
      | PSL_Sequence_Declaration
'''


def detect(iToken, lObjects):
    return iToken
