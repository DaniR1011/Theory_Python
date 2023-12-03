variable_global = 'Soy Global'

def probar_scope():
 variable_local = 'Soy Local'
 print(variable_local)
 variable_global = 'Soy global desde otro scope'
 print(variable_global)

probar_scope()
# print(variable_local)