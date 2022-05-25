from ctypes.wintypes import RGB

from .models import Quizz
import matplotlib.pyplot as plt


def QuizzPontuacao(input):
    user_score = 0

    if input.pergunta1 == "New Orleans":
        user_score += 1

    if input.pergunta2 == "Jogador de basebol":
        user_score += 1

    if input.pergunta3 == "Livery Stable Blues":
        user_score += 1

    if input.pergunta4 == "Ella Fitzgerald":
        user_score += 1

    if input.pergunta5 == "Trompete":
        user_score += 1

    return user_score


def info_user(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizzPontuacao(quizz)

    return dados


def draw_graph(objetos):
    # creating the dataset
    dados = info_user(objetos)

    user = list(dados.keys())
    pontuacao = list(dados.values())

    color = RGB(255,185,15)

    plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.barh(user, pontuacao)

    plt.ylabel("Nome dos Jogadores")
    plt.xlabel("Quizz Jazz Pontuação")
    plt.title("Pontuação")
    plt.savefig('portfolio/static/portfolio/images/grafico_final.png')
