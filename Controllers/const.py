FORMAT = 'To add a valid purchase statement please follow the given format:\n\n"<i>! item name, price</i>"'
COMMANDS = ['start', 'help']
REGEX_PURCHASE = "^[!]\s*?[ěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮĚÓůa-zA-Zа-яА-Я\s]*,\s*?\d*?$" # optional flags: gm
TABLESEP = '=====\n'
