from users import Utente
from users import Privilegi
from users import Admin




user_1=Utente("Esu","Grappa","esu_gra","esugrappa@gnm.com")
privilegg_1=Privilegi(["Creare","Aggiungere","eliminare","bloccare"])

admin_1=Admin(user_1,privilegg_1)

print(user_1.describe_user())
print(privilegg_1.show_privileges())

