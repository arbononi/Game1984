from config import lin_terminal, col_terminal

tela_principal = [
    { "lin" :  1, "col" : 2, "value" : "╔" + "═" * (col_terminal - 27) + "╦══════════════════════╗" },
    { "lin" :  2, "col" : 2, "value" : "║" + " " * (col_terminal - 27) + "║ DATA:                ║" },
    { "lin" :  3, "col" : 2, "value" : "╠" + "═" * (col_terminal - 27) + "╩══════════════════════╣" },
    { "lin" :  4, "col" : 2, "value" : "║" + " " * (col_terminal - 4) + "║" },
    { "lin" : lin_terminal - 2, "col" : 2, "value" : "╠" + "═" * (col_terminal - 4) + "╣" },
    { "lin" : lin_terminal - 1, "col" : 2, "value" : "║" + " " * (col_terminal - 4) + "║" },
    { "lin" : lin_terminal, "col" : 2, "value" : "╚" + "═" * (col_terminal - 4) + "╝" }
]

tela_capitulos = [
    { "lin" :  3, "col" : 2, "value" : "╠" + "═" * (col_terminal - 43) + "╦═══════════════╩══════════════════════╣" },
    { "lin" :  4, "col" : 2, "value" : "║" + " " * (col_terminal - 43) + "║                                      ║" },
    { "lin" : lin_terminal - 2, "col": 2, "value" : "╠" + "═" * (col_terminal - 43) + "╩══════════════════════════════════════╣" }
]
rosto = [
    "   ~^~^~^~^~^~^~^~^~^~^~^~^~^~^",
    "  /----------------------------\\",
    " /                              \\",
    "|                                |",
    "|           O         O          |",
    "|                                |",
    "|                >               |",
    "|                                |",
    "|                                |",
    " \\       \______________/       /",
    "  \\                            /",
    "   \\                          /",
    "    \\                        /",
    "     \\                      /",
    "      \\____________________/"
]

legenda_rosto = "O Grande Irmão está vigiando você!". center(38, " ")