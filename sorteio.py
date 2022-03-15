# MODULO DE SORTEIO
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------

import time
import PySimpleGUI as sg
import random


class Sorteio:
    def __init__(self):
        sg.theme("Reddit")
        self.layout = [
            [sg.Text("Tela de inserção de dados para o sorteio", size=(39, 0))],
            [sg.Text("Insira um valor.", font=("Helvetica", 15), text_color="green", size=30)],
            [sg.Text("(NOME OU NÚMERO):", font=("Helvetica", 15), text_color="green", size=30)],
            [sg.Input(key="dados", size=30, focus=True)],
            [sg.Button('INSERIR', size=10, bind_return_key=True)],
            [sg.Text("VISUALIZAÇÃO DOS DADOS", font=("Helvetica", 15))],
            [sg.Output(background_color="black", font=("Helvetica", 20), text_color="green", key="terminal",
                       size=(40, 10))],
            [sg.Button('SORTEAR', disabled=False, size=20)],
            [sg.Button('FINALIZAR', size=20)]
        ]
        # CRIAR A JANELA
        self.janela = sg.Window('SISTEMA DE SORTEIO.', layout=self.layout).finalize()

    def sistema(self):
        self.lista = []
        while True:
            evento, valores = self.janela.read()
            if evento == "INSERIR":
                while True:
                    self.janela['dados'].update('')
                    self.janela['terminal'].update('')
                    if valores["dados"] in self.lista:
                        print("O VALOR INSERIDO JA EXISTE NA LISTA...")
                        print("INSIRA OUTRO VALOR!")
                        break
                    else:
                        self.lista.append(valores["dados"])
                        print("SUA LISTA É ")
                        print(33 * "--")
                        for i in self.lista:
                            print(i, " - ", end=" ")
                        break
            elif evento == "SORTEAR":
                self.janela['terminal'].update('')
                print("SORTEANDO...")
                time.sleep(5)
                resultado = random.choice(self.lista)
                print(f"Resultado do sorteio é: {resultado}")
            elif evento == sg.WIN_CLOSED:
                break
            elif evento == "FINALIZAR":
                self.janela['terminal'].update('')
                print("SISTEMA FINALIZANDO")
                time.sleep(3)
                break


if __name__ == "__main__":
    sorteio = Sorteio()
    sorteio.sistema()
