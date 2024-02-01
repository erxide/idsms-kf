import subprocess

def get_all_users():
    try:
        resultat_commande = subprocess.check_output(['getent', 'passwd'], universal_newlines=True)
        lignes_utilisateurs = resultat_commande.strip().split('\n')
        utilisateurs = [ligne.split(':')[0] for ligne in lignes_utilisateurs]
        return utilisateurs

    except subprocess.CalledProcessError as e:
        print(f"\033[31mError : \033[0m{e}")
        exit(2)